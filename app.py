"""
Dashboard for the gate register checker.
Run:  streamlit run app.py
"""
import datetime as dt
import os
import tempfile

import pandas as pd
import streamlit as st

import logic

st.set_page_config(page_title="Gate Register Check", layout="wide")
st.title("Gate Register Check")
st.caption("Late arrivals, girls not yet arrived, and entries to verify. "
           "Room numbers and codes only - no names or phone numbers.")

# ---- Settings ---------------------------------------------------------------
with st.sidebar:
    uploaded = st.file_uploader("Register CSV (optional)", type="csv")
    h, m = map(int, logic.CURFEW.split(":"))
    curfew_t = st.time_input("Curfew", dt.time(h, m), step=300)
curfew = curfew_t.strftime("%H:%M")

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded.getvalue())
    path = tmp.name

try:
    results = logic.check_all(logic.load_rows(path), curfew)
except Exception as e:
    st.error(f"Could not read the register file: {e}")
    st.stop()

with st.sidebar:
    gate = st.selectbox("Gate", ["All"] + sorted({r["gate"] for r in results
                                                  if r["gate"]}))
    results = [r for r in results if gate == "All" or r["gate"] == gate]
    date = st.selectbox("Date", ["All"] + sorted({r["date"] for r in results
                                                  if r["date"]}))
    results = [r for r in results if date == "All" or r["date"] == date]

late = logic.late_list(results)
not_arrived = logic.not_arrived_list(results)
problems = logic.problem_list(results)

# ---- Counts -----------------------------------------------------------------
c1, c2, c3 = st.columns(3)
c1.metric(f"Late (after {curfew_t.strftime('%I:%M %p')})", len(late))
c2.metric("Not yet arrived", len(not_arrived))
c3.metric("Entries to verify", len({r["line"] for r, _, _ in problems}))

# ---- 1. Late ----------------------------------------------------------------
st.subheader("1. Late arrivals")
if late:
    df = pd.DataFrame([{"Date": r["date"], "Gate": r["gate"],
                        "Room": r["room"], "Student": r["student"],
                        "Back at": r["back"], "Minutes late": r["late_min"]}
                       for r in late])
    st.dataframe(df.style.apply(
        lambda row: ["color: red" if row["Minutes late"] > 10 else ""]
        * len(row), axis=1), hide_index=True)
    st.caption("Red = more than 10 minutes late.")
else:
    st.success("No late arrivals.")

# ---- 2. Not arrived ---------------------------------------------------------
st.subheader("2. Not yet arrived (no arrival time written)")
if not_arrived:
    st.dataframe(pd.DataFrame([{"Date": r["date"], "Gate": r["gate"],
                                "Room": r["room"], "Student": r["student"],
                                "Went to": r["destination"], "Out": r["out"]}
                               for r in not_arrived]), hide_index=True)
    st.caption("Check if she is back. If not, inform the warden.")
else:
    st.success("Everyone has an arrival time.")

# ---- 3. Suspicious / incomplete --------------------------------------------
st.subheader("3. Suspicious / incomplete entries")
if problems:
    st.dataframe(pd.DataFrame([{"CSV line": r["line"], "Date": r["date"],
                                "Room": r["room"], "Type": kind,
                                "Reason": why}
                               for r, kind, why in problems]),
                 hide_index=True)
    st.caption("Verify these in the register or ask the student.")
else:
    st.success("No suspicious or incomplete entries.")

# ---- Report -----------------------------------------------------------------
st.divider()
report = logic.report_text(results, curfew)
st.download_button("Download report for warden", report,
                   file_name=f"gate_report_{curfew.replace(':', '')}.txt")