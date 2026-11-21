# Research: Improving Hostel Gate Return Monitoring at Gate 4

**By:** Esha Panwar, M.Tech, IIIT Allahabad\
**Date:** 21 November 2026\
**Place:** Gate 4, IIIT Allahabad (Jhalwa campus)

## The Problem

At Hostel Gate 4, the security guard maintains student movement records in a physical register. At the end of the day, the guard has to manually check the register to identify girls who have not returned yet, students who arrived after the 10 PM curfew, and entries that may be incorrect or fake and therefore need verification. This manual checking takes time, even though the guard needs to quickly identify these cases and inform the warden—particularly when a girl has not arrived or has returned late, which is important for student safety. I want to build a simple tool that organizes the movement records and quickly highlights students who are still out, late arrivals after 10 PM, and suspicious or incomplete entries for the guard to verify and report to the warden.

## Person I Am Helping

**Person:** \[Name or anonymous identifier, with permission\]\
**Role:** Security guard at Hostel Gate 4\
**Location:** IIIT Allahabad, Jhalwa campus

The intended user is the security guard responsible for maintaining and
checking student movement records at Gate 4. Through an initial
conversation, I learned that they currently need to manually identify
entries in the register. The proposed tool aims to make this process
easier by providing an organized view of the records and highlighting
entries that may need attention.

## Existing Solutions and Why They May Not Fit

### 1. Manual Register

The existing method is a physical register used to record student
movement.

**Observed limitations:** - The guard has to manually check the register
to identify late entries, which takes time. - The guard also has to
manually check who has not returned yet. - This information needs to be
identified quickly so the guard can inform the warden early.

### 2. Spreadsheets (Microsoft Excel / Google Sheets)

Spreadsheets can be used to store student movement records digitally and
support sorting, filtering, and calculations.

**Why they may not fit this specific problem:** - Entries would still
need to be manually transferred from the register into a spreadsheet. -
The guards working at Jhalwa are not necessarily technical users; during
my initial interaction, I understood that they may not be comfortable
writing, maintaining, or managing Excel spreadsheets. - A spreadsheet
may require familiarity with filters or formulas to identify students
who have not returned or entries requiring attention. - A simple,
focused tool could be easier to use for this particular workflow without
requiring the guard to manage spreadsheet operations.

## Sources I Actually Read

### Source 1: Fingerprint-Based Hostel Outpass Management System with Automated Late-Entry Alert

**Authors:** Savita S. Kulekumatagi, D. Chaithanya Shree, Karthika,
Nidhi, Shaikh Tanzeen Hana\
**Publication:** Iconic Research and Engineering Journals, Vol. 10,
Issue 5, November 2026\
**Link:** https://doi.org/10.64388/ire1724494

**Notes:** - The paper describes a hostel outpass system using a
Raspberry Pi, fingerprint sensor, database, and warden dashboard to
record student exits and returns. - It compares expected return time
with actual return time and automatically flags late returns, reducing
the need for manual checking. - It provides an example of a more
hardware-intensive automated solution; my proposed prototype will focus
on organizing existing records and identifying entries requiring
attention, based on the guard's confirmed workflow.

### Source 2: SpaceBasic Hostel Outpass System

**Link:**\
https://www.spacebasic.com/hostel-management-system/hostel-outpass-system

**Notes:** - SpaceBasic describes a digital outpass workflow in which students request passes and wardens approve or reject them. - The system includes QR-code verification at the hostel gate, parent/guardian notifications (where configured), and real-time movement logs. - It is a broad platform; my project will investigate a smaller, focused tool for the manual register-checking problem observed at Gate 4, rather than assume the hostel needs or uses a full hostel-management platform.
