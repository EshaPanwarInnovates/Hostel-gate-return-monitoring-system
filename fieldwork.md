# Fieldwork – Gate 4 and GH3 Gate, Girls' Hostels, IIIT Allahabad (Jhalwa)

**Date:** 21 November 2026
**Visits:** around 7: PM (first visit) and 8:00–8:30PM (second visit)
**Where I stood:**at 6:30pm i went to gate-4 and also at the entrance of the Girls' Hostel 3 (GH3) entrance, near the guard's desk

## Why two gates

I first saw the problem at Gate 4. Gate 4 does not allow photos of the
late-entry register, so I collected the evening data and talked to the guard
at the Girls' Hostel 3 (GH3) entrance, which uses the same register system.

- **Gate 4:** where I first noticed the problem; I got the 17 Nov register
  entries here
- **Girls' Hostel 3 (GH3) entrance:** conversation with the guard, Civil Lines register (late
  entries), both photos from 8:05–8:06 PM

## Photos

- `gh3_entrance.jpg` – Girls' Hostel 3 entrance, taken 21 Nov 2026, 8:06 PM
  (file name 20261121_200607). The person inside is scribbled out on purpose.
- `register_blurred.jpg` – taken 21 Nov 2026, 8:05 PM (file name 20261121_200550).
  Names, roll numbers, phone numbers and signatures are blurred.

The guard did not allow me to take her photo, or photos of the conversation
or of people at the gate. I respected that. That is why there is no photo of
the guard, and why the person in the gate photo is scribbled out. Instead, I
wrote the conversation in my phone notes (screenshot: `notes_conversation.jpg`,
8:29 PM).

## Conversation

**Name:** Manisha Kesarwani
**Role:** Security guard at the Girls' Hostel 3 (GH3) entrance, night shift (5 PM to 5 AM)

**3 things she said:**
1. The student fills the register herself: date, name, roll number, phone
   number, room number, where she is going, purpose, vehicle, "own risk",
   out time and sign, then arrival time and sign. **The student writes the
   time, not the guard.**
2. To find who is late or not back, they have to check the whole register
   again and again.
3. The main problem is fraud entries: a friend signing for someone, a missing
   return time, or writing that can't be read.

**What surprised me:**
She told me that when girls are in a rush, many of them don't sign at all
and just go. I had assumed the register was complete and only needed
checking. If a girl never signs, she is not in the register, so no tool that
reads the register can know she is out.

**What this changed in my plan:**
- The tool cannot trust the times fully, because students write them
  themselves. So it should flag odd times (in before out, overwritten,
  unreadable) instead of only calculating who is late.
- The tool can only check what is written. Girls who never signed are
  outside its reach. I will say this clearly in the README.

## Data collection (data.csv)

There is more than one register at the gate: the one with the 17 Nov page,
and a separate Civil Lines register for trips into the city. So the guard
has to check more than one book at night.

| Source | Rows | How I collected it |
| --- | --- | --- |
| Gate 4 register page, 17 Nov 2026 (daytime) | __ | Photographed the register at Gate 4, then typed each row by hand |
| Girls' Hostel 3 (GH3) entrance, Civil Lines register, 27–29 Aug 2026 (trips into the city, evening, has late returns) | __ | Photographed on 21 Nov at 8:05 PM, then typed each row by hand |

**Privacy:** I did not copy names, roll numbers or phone numbers. Each student
is a code (S01, S02...) and I kept the room number. The real register stays
with the guard.

**Things I noticed in the raw data:**
- An "in" time earlier than the "out" time (room 108-B, 17 Nov: out 3:09, in 3:06)
- Times crossed out and rewritten (1:27 changed to 2:00)
- Unclear handwriting (1:20 or 7:20?)
- Most times have no AM/PM
- Ditto marks (") instead of writing the place again
- Incomplete dates ("1/26")
- Two different guards signing on the same day (shift change)
- Evening pages have arrivals after 10 PM (10:10, 10:18, 10:20, 10:30) and one at 12:16
- Some rows have no arrival time

**Limits:**
- At Gate 4 they did not give me fresh late entries, so the Gate 4 data
  (17 Nov) has daytime entries only.
- I cannot go out after 10 PM because of my own hostel timing, so I could
  not collect late entries myself at the time of the curfew check. My own
  observation stops around 8 PM and thats why i collected entries from
   gh-3 gate ther is also the same problem.
- I noticed the same problem at the Girls' Hostel 3 entrance, so I collected
  the late entries there, from the Civil Lines register (27–29 Aug 2026).
  These are older entries, not from tonight.

