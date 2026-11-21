# AI chat summary – Claude

**Tool:** Claude (claude.ai, mobile app and desktop)
**Date:** 21 November 2026, about 11:26 AM to 11:00 PM IST
**Note:** This is a summary of the chat, written by Claude at my request.
It is not the full word-for-word transcript.

## Link to the full chat

Full chat: [Claude conversation](https://claude.ai/share/0735cb2e-9045-4eb6-94f4-9e753bd26ad7)

---

## 1. Understanding the assignment (11:26 AM)
- I uploaded the assignment and asked what they want.
- Claude explained the 4 steps, the rules, the git rules, and pointed out that
  the scoring notes were left in the file (fieldwork below 10 = reject, red flags,
  call questions).

## 2. Choosing the problem (11:28 AM)
- I said my idea: the guard at the Gate 4 girls' hostel keeps a paper register
  and after 10 PM has to find by hand who is late, who has not returned, and
  fake entries.
- Claude said it fits the right size and warned about privacy: use room numbers
  or codes, never names or phone numbers, and ask the warden first.

## 3. Research (11:40 AM – 12:04 PM)
- I asked for sources. Claude searched and found:
  - IRE Journals paper on a fingerprint outpass system with late-entry alerts
  - Hostel attendance study report on manual IN-OUT registers
  - QR gate-pass apps (SpaceBasic, AMD GatePass)
  - News articles on women's hostel curfews
- I wrote research.md myself and uploaded it. Claude reviewed it: rename the
  file to research.md, fill the person placeholder, fix the date and "Gate -04",
  fix bullet formatting, and replace "manual register" as an existing solution.

## 4. Fieldwork (7:12 PM – 8:50 PM)
- I sent photos of the Gate 4 register (17 Nov). Claude warned not to upload
  them unblurred (names, roll numbers, phone numbers) and pointed out messy
  entries: return before out (108-B), overwritten times, unclear handwriting,
  no AM/PM, ditto marks, two guards signing.
- Claude said the page was daytime only, so it did not show the 10 PM problem.
  Suggested going back in the evening.
- I could not stay out till 10 PM (my own hostel timing). Staff did not allow
  photos of the guard or the conversation. Claude suggested writing notes with
  timestamps instead and writing the refusal honestly in fieldwork.md.
- I went back, talked to the guard (Manisha Kesarwani, night shift 5 PM–5 AM)
  and took photos at the GH3 entrance, plus the Civil Lines register at GH3.
- I sent my notes. Claude drafted fieldwork.md from my notes. I asked for
  changes: GH3 entrance instead of Gate 4 for the photos and conversation, add
  that the guard did not allow her photo, add the limits (no fresh late entries
  from Gate 4, my curfew, late entries taken from GH3 Civil Lines register).

## 5. data.csv (9:10 PM – 9:20 PM)
- I asked Claude to convert the register photos into CSV, leaving blanks
  where no time is written and keeping AM/PM only where written.
- Claude typed 34 rows from Gate 4 (17 Nov) and 33 rows from the GH3 Civil
  Lines register (27–29 Aug). Students replaced with codes (S01...), no names
  or phone numbers. Uncertain values marked in the note column.
- Claude first said the Civil Lines photo was too dark to read reliably and
  did not want to guess; after I asked again it rotated and enhanced the photo
  and transcribed it, marking unclear values. I need to check rows against
  the photos.
- I asked if AI transcription is allowed. Claude said yes, since the data is
  real and collected by me, as long as I check it and mention it.

## 6. Building the tool (9:24 PM – 10:15 PM)
- I described what I wanted: logic.py and a Streamlit app.py.
- Claude wrote both and tested them on data.csv and on bad rows
  (25:99, abc, missing room, missing out time).
- I asked to simplify to only 3 things: late arrivals, not yet arrived,
  suspicious/incomplete entries. Claude rewrote both files.
- I asked how time parsing works and how suspicious entries are found;
  Claude explained (AM/PM guessing, 3-hour midnight rule, ditto handling,
  5 suspicious rules).
- I asked to change colours: red text only if more than 10 minutes late.

## 7. README and reflection (9:40 PM – 10:26 PM)
- Claude wrote README.md (how to run, real output, what it gets wrong).
  I changed the heading to my repo name, removed the screen recording section,
  and asked to show only some output entries.
- I asked what to include in reflection.md. Claude gave guiding questions
  and an empty format. **I wrote reflection.md myself without AI.**

## 8. Demo video (10:26 PM – 10:46 PM)
- Claude explained how to record and what to show. I recorded the screen.
- My video was 142 MB, so Claude compressed it to about 4 MB for GitHub.

---

## What AI did / what I did

| Part | Me | AI (Claude) |
|---|---|---|
| Choosing the problem | ✓ | feedback |
| research.md | wrote it | found sources, reviewed |
| Going to the gates, talking to the guard, photos | ✓ | – |
| fieldwork.md | my notes and facts | drafted from my notes, edited on my request |
| data.csv | collected the register photos, checked rows | typed rows from photos |
| logic.py, app.py | decided what the tool should do | wrote the code |
| README.md | edits | drafted |
| reflection.md | wrote it myself | only gave the format |
| Demo video | recorded it | compressed it |
