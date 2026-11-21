"""
Gate register checker - finds 3 things in the register (data.csv):
  1. LATE        - came back after the curfew (and how many minutes late)
  2. NOT ARRIVED - went out, no arrival time written
  3. SUSPICIOUS / INCOMPLETE - entries the guard should verify

Run without the dashboard:
    python logic.py data.csv          (curfew 22:00)curfew means the time of last entry in the hostel if a girl went out
    python logic.py data.csv 20:00    (any curfew)
"""

import csv
import re
import sys

# ---- Settings you can change ------------------------------------------------
CURFEW = "22:00"          # hostel curfew, 24-hour clock
ROLLOVER_GAP_MIN = 180    # a return time with no AM/PM that is 3+ hours
                          # "before" the out time is taken as 12 hours later
                          # (out 5:20 pm, back "12:16" -> 12:16 at night)

DITTO = {"ditto", '"', "''"}
COLUMNS = ["date", "gate", "register", "student", "room", "destination",
           "purpose", "vehicle", "own_risk", "out_time", "return_by",
           "in_time", "guard_out", "guard_in", "note"]


# ---- Time parsing -----------------------------------------------------------
def parse_time(text):
    """
    Handwritten time -> (minutes after midnight, ampm_written, error).
      "1:07 pm" -> 787     "10.00 pm" -> 1320     "900 PM" -> 1260
      "12:21"   -> 741 (no AM/PM: 1-7 = PM, 8-11 = AM, 12 = noon)
      ""        -> None, no error (blank)
      "abc"     -> None, error
    """
    raw = (text or "").strip()
    if raw == "":
        return None, False, None
    t = raw.lower().replace(".", ":").replace(" ", "")

    ampm = None
    if t[-2:] in ("am", "pm"):
        ampm, t = t[-2:], t[:-2]

    if re.fullmatch(r"\d{1,2}:\d{2}", t):
        h, m = map(int, t.split(":"))
    elif re.fullmatch(r"\d{1,2}", t):            # "10 pm"
        h, m = int(t), 0
    elif re.fullmatch(r"\d{3,4}", t):            # "900 PM"
        h, m = int(t[:-2]), int(t[-2:])
    else:
        return None, False, f"unreadable time '{raw}'"

    if h > 23 or m > 59 or (ampm and not 1 <= h <= 12):
        return None, False, f"impossible time '{raw}'"

    if ampm == "am":
        h = 0 if h == 12 else h
    elif ampm == "pm":
        h = 12 if h == 12 else h + 12
    elif 1 <= h <= 7:                            # no AM/PM written
        h += 12
    return h * 60 + m, ampm is not None, None


def fmt(minutes):
    """Minutes -> '10:20 PM' ('+1 day' if after midnight)."""
    if minutes is None:
        return ""
    day, m = divmod(minutes, 1440)
    h, mm = divmod(m, 60)
    s = f"{(h % 12) or 12}:{mm:02d} {'AM' if h < 12 else 'PM'}"
    return s + (" (+1 day)" if day else "")


# ---- Reading the CSV --------------------------------------------------------
def load_rows(path):
    """Read data.csv. Missing columns become ''. A ditto copies the value
    from the row above, like in the register."""
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for line, r in enumerate(csv.DictReader(f), start=2):
            row = {c: (r.get(c) or "").strip() for c in COLUMNS}
            row["line"] = line
            rows.append(row)

    prev = {}
    for row in rows:
        if row["gate"] != prev.get("gate"):
            prev = {}
        for c in ("date", "destination", "purpose", "vehicle", "own_risk",
                  "in_time"):
            if row[c].lower() in DITTO:
                row[c] = prev.get(c, "")
        if row["date"] == "" and not crossed(row):
            row["date"] = prev.get("date", "")
        prev.update({c: row[c] for c in COLUMNS if row[c]})
    return rows


def crossed(row):
    return "entry crossed out" in row["note"].lower()


# ---- The three checks -------------------------------------------------------
def check_row(row, curfew_min):
    """Return one result: status = Late / Not arrived / Returned / -,
    minutes late, and a list of (Suspicious|Incomplete, reason)."""
    problems = []
    out_m, _, out_err = parse_time(row["out_time"])
    in_m, in_ampm, in_err = parse_time(row["in_time"])
    by_m, _, by_err = parse_time(row["return_by"])
    note = row["note"].lower()

    # Incomplete
    if crossed(row):
        problems.append(("Incomplete", "whole entry crossed out"))
    else:
        if row["room"] == "":
            problems.append(("Incomplete", "no room number"))
        if row["out_time"] == "":
            problems.append(("Incomplete", "no out time"))
    for err in (out_err, in_err, by_err):
        if err:
            problems.append(("Incomplete", err))

    # Return time with no AM/PM far "before" out time -> 12 hours later
    if out_m is not None and in_m is not None and not in_ampm \
            and out_m - in_m >= ROLLOVER_GAP_MIN:
        in_m += 720
        problems.append(("Suspicious", f"return '{row['in_time']}' has no "
                         f"AM/PM, taken as {fmt(in_m)} - verify"))

    # Suspicious
    if out_m is not None and in_m is not None and in_m < out_m:
        problems.append(("Suspicious", f"return {row['in_time']} is before "
                         f"out {row['out_time']}"))
    if out_m is not None and by_m is not None and by_m < out_m:
        problems.append(("Suspicious", f"'return by' {row['return_by']} is "
                         f"before out {row['out_time']}"))
    if any(w in note for w in ("overwritten", "unclear", "corrected")):
        problems.append(("Suspicious", "overwritten / unclear in register: "
                         + row["note"]))

    # Late / not arrived
    late = 0
    if crossed(row) or out_m is None:
        status = "-"
    elif in_m is None and not in_err:
        status = "Not arrived"
    elif in_m is not None and in_m > curfew_min:
        status, late = "Late", in_m - curfew_min
    else:
        status = "Returned"

    return {"line": row["line"], "date": row["date"], "gate": row["gate"],
            "student": row["student"], "room": row["room"],
            "destination": row["destination"],
            "out": fmt(out_m) or row["out_time"],
            "back": fmt(in_m) or row["in_time"],
            "status": status, "late_min": late, "problems": problems}


def check_all(rows, curfew=CURFEW):
    curfew_min, _, err = parse_time(curfew)
    if curfew_min is None:
        raise ValueError(f"bad curfew time '{curfew}'")
    results = [check_row(r, curfew_min) for r in rows]

    # Same room + same out time + same return time: did one girl sign for
    # her friend? (the guard's main worry)
    seen = {}
    for r, res in zip(rows, results):
        if r["out_time"] and r["in_time"]:
            key = (r["gate"], r["date"], r["room"], r["out_time"],
                   r["in_time"])
            if key in seen:
                for x in (seen[key], res):
                    x["problems"].append(("Suspicious", "same room and same "
                        "times as another entry - one girl signed for both?"))
            else:
                seen[key] = res
    return results


# ---- The three lists --------------------------------------------------------
def late_list(results):
    return sorted([r for r in results if r["status"] == "Late"],
                  key=lambda r: -r["late_min"])


def not_arrived_list(results):
    return [r for r in results if r["status"] == "Not arrived"]


def problem_list(results):
    return [(r, kind, why) for r in results for kind, why in r["problems"]]


def report_text(results, curfew=CURFEW):
    late, na, probs = late_list(results), not_arrived_list(results), \
        problem_list(results)
    out = [f"GATE REGISTER CHECK - curfew {curfew}",
           f"Late: {len(late)} | Not arrived: {len(na)} | "
           f"Entries to verify: {len({r['line'] for r, _, _ in probs})}", "",
           "1. LATE ARRIVALS"]
    out += [f"   {r['date']:9} {r['gate']:5} room {r['room']:6} back "
            f"{r['back']}  ({r['late_min']} min late)" for r in late] or \
           ["   none"]
    out += ["", "2. NOT YET ARRIVED"]
    out += [f"   {r['date']:9} {r['gate']:5} room {r['room']:6} out "
            f"{r['out']}  to {r['destination']}" for r in na] or ["   none"]
    out += ["", "3. SUSPICIOUS / INCOMPLETE"]
    out += [f"   line {r['line']:3} room {r['room'] or '?':6} [{k}] {why}"
            for r, k, why in probs] or ["   none"]
    return "\n".join(out)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    curfew = sys.argv[2] if len(sys.argv) > 2 else CURFEW
    print(report_text(check_all(load_rows(path), curfew), curfew))
