# Hostel-gate-return-monitoring-system

A small tool for the night guard at the girls' hostel gates, IIIT Allahabad (Jhalwa campus).
It reads the hostel in/out register (copied into `data.csv`) and shows, in one place:

1. **Late arrivals**: who came back after the curfew, and how many minutes late
2. **Not yet arrived**: who went out and has no arrival time written
3. **Entries to verify**: suspicious or incomplete entries

**Place:** Gate 4 (where I first saw the problem) and the Girls' Hostel 3 (GH3) entrance
**Person:** Manisha Kesarwani, security guard, night shift (5 PM to 5 AM)
**Date of fieldwork:** 21 November 2026
**By:** Esha Panwar

## The problem

Students fill a paper register when they go out and come back. At night the
guard has to read the whole register "again and again" to find who is late,
who is not back, and which entries are fake or wrong (a friend signing,
a missing return time, writing that can't be read). Details are in
[research.md](research.md) and [fieldwork.md](fieldwork.md).

## How to run

Needs Python 3.9+.

```
pip install -r requirements.txt
streamlit run app.py
```

The dashboard opens in the browser. In the sidebar you can change the
**curfew time**, filter by **gate** and **date**, or upload another register CSV.
The **Download report for warden** button saves a text summary.

Without the dashboard (terminal only):

```
python logic.py data.csv          # curfew 10 PM
python logic.py data.csv 20:00    # any other curfew
```

Settings at the top of `logic.py`:

| Setting | Default | Meaning |
|---|---|---|
| `CURFEW` | `"22:00"` | curfew time |
| `ROLLOVER_GAP_MIN` | `180` | a return time with no AM/PM that is this many minutes "before" the out time is taken as 12 hours later (after midnight) |

## Files

| File | What it is |
|---|---|
| `data.csv` | 67 register entries I collected (34 from Gate 4, 17 Nov 2026; 33 from the GH3 Civil Lines register, 27-29 Aug 2026). Students are codes (S01...), no names, roll numbers or phone numbers. |
| `logic.py` | time parsing and the three checks |
| `app.py` | Streamlit dashboard |
| `research.md`, `fieldwork.md` | research and fieldwork notes |
| `reflection.md` | my reflection |

## Real output

`python logic.py data.csv` on my real data (only some entries shown here;
the complete output is shown in the screen recording):

```
GATE REGISTER CHECK - curfew 22:00
Late: 9 | Not arrived: 12 | Entries to verify: 24

1. LATE ARRIVALS
   29/8/26   GH3   room 807    back 12:16 AM (+1 day)  (136 min late)
   29/8/26   GH3   room 549    back 10:30 PM  (30 min late)
   28/8/26   GH3   room 529    back 10:20 PM  (20 min late)
   ...
   28/8/26   GH3   room 804    back 10:10 PM  (10 min late)

2. NOT YET ARRIVED
   27/08/26  GH3   room 807    out 5:34 PM  to Civil Lines
   28/8/26   GH3   room 704    out 5:10 PM  to Jhalwa
   28/8/26   GH3   room 611    out 5:45 PM  to Civil Lines
   ...

3. SUSPICIOUS / INCOMPLETE
   line  15 room 108-B  [Suspicious] same room and same times as another entry - one girl signed for both?
   line  24 room 640    [Suspicious] return 3:15 is before out 3:45
   line  28 room 108-B  [Suspicious] return 3:06 is before out 3:09
   line  40 room 624    [Incomplete] no out time
   line  41 room 702    [Incomplete] whole entry crossed out
   line  59 room 501    [Suspicious] 'return by' 2:00 PM is before out 2:30 PM
   line  68 room 807    [Suspicious] return '12:16' has no AM/PM, taken as 12:16 AM (+1 day) - verify
   ...
```

In the dashboard, late arrivals more than 10 minutes late are shown in red.

With a curfew of 8 PM (`python logic.py data.csv 20:00`) the late count goes from 9 to 17.

### Bad rows

I fed it a file with broken rows (`25:99`, `abc`, no room, no out time). It does
not crash; it lists them under "Suspicious / incomplete":

```
3. SUSPICIOUS / INCOMPLETE
   line   2 room 612    [Incomplete] impossible time '25:99'
   line   2 room 612    [Incomplete] unreadable time 'abc'
   line   3 room ?      [Incomplete] no room number
   line   4 room 613    [Incomplete] no out time
```

## How it reads times

The register is handwritten, so times look like `12:21`, `1:07 pm`, `10.00 pm`,
`900 PM`, `10 pm`. Each one is turned into minutes after midnight.

- If AM/PM is written, it is used.
- If not: hours 1-7 are taken as PM, 8-11 as AM, 12 as noon.
- If a return time has no AM/PM and is 3+ hours "before" the out time, it is
  taken as 12 hours later (out 5:20 PM, back `12:16` -> 12:16 AM next day) and
  flagged "verify".
- A ditto mark copies the value from the row above, like in the register.

## What it gets wrong

- **It cannot see girls who never signed.** Manisha ji told me many girls
  in a rush don't sign at all. They are not in the register, so they are not
  in this tool. This is the biggest gap.
- **AM/PM is guessed.** A girl who wrote `8:00` meaning 8 PM is read as 8 AM.
  The 3-hour midnight rule is also a guess; `12:16` could really be noon.
- **"Not yet arrived" may just mean she forgot to write the time.** The tool
  cannot tell a missing girl from a missing entry. The guard still has to check.
- **"One girl signed for both?" is often wrong.** Two friends from the same
  room going out together will have the same times. It only means "look again".
- **Overwritten / unclear flags come from my notes in `data.csv`**, not from
  the tool reading handwriting. Someone has to type the register first.
- **Typing the register is extra work for the guard.** Manisha ji's register
  is on paper; this tool only helps if someone copies it into the CSV (or the
  register moves to a sheet). I have not solved that.
- **Old data.** The late entries are from August (Civil Lines register at GH3).
  I could not collect fresh entries after 10 PM because of my own hostel timing,
  and Gate 4 did not share its late-entry pages.
- **Gate 4 page is daytime only** (12:21 PM to 4:10 PM), so at a 10 PM curfew it shows no late
  arrivals from Gate 4.
- **My transcription can be wrong.** The photos are dark and the handwriting
  is messy. Uncertain values are marked in the `note` column.

## Privacy

The real register has names, roll numbers and phone numbers. None of that is in
this repo. Each student is a code; only room numbers are kept. The guard did
not allow photos of herself, so there are none.
