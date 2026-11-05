# Library Workshop Proposal: AI Basics for Adult Patrons (Revised)

> **Notice**: This document is a planning proposal only and **not a confirmed booking**. Room availability has not been verified; librarian review and formal booking confirmation are required.

---

## 1. Overview
- **Topic**: AI basics for adult library patrons
- **Audience**: 35 adult library patrons
- **Duration**: 60 minutes
- **Booking Status**: All rooms are hypothetical candidates. Availability has NOT been checked; librarian approval and a real booking are required.

---

## 2. Planning Constraints & Requirements
- **Expected Attendance**: 35 patrons (updated from 20)
- **Approved Budget Cap**: $100.00 (updated from $80.00)
- **Projector Required**: Yes
- **Step-Free Access Required**: Yes
- **Refreshments**: None / Removed per request ($0.00)

---

## 3. Selected Facility
- **Selected Room**: Community Hall
- **Capacity**: 40 (accommodates 35 attendees; Reading Room capacity of 24 is no longer sufficient)
- **Projector**: Yes (available)
- **Step-Free Access**: Yes (compliant)
- **Room Fee**: $30.00

---

## 4. Itemized Budget
| Item | Unit Cost | Quantity | Subtotal |
| :--- | :--- | :--- | :--- |
| **Room Rental Fee** (Community Hall) | Flat rate | 1 session | $30.00 |
| **Participant Materials** | $2.00 / person | 35 attendees | $70.00 |
| **Refreshments** | $0.00 (removed) | 0 | $0.00 |
| **Total Estimated Cost** | | | **$100.00** |
| **Approved Budget** | | | **$100.00** |
| **Surplus / Variance** | | | **$0.00** (exact match to budget cap) |

---

## 5. 60-Minute Workshop Agenda
| Time | Duration | Activity | Description |
| :--- | :--- | :--- | :--- |
| **00:00 – 00:10** | 10 min | **Welcome & Foundations** | Welcome the 35 attendees, distribute handout packets, review session goals, and introduce foundational concepts of artificial intelligence. |
| **00:10 – 00:25** | 15 min | **Everyday AI & Generative Tools** | Presentation using Community Hall projector illustrating everyday AI utilities (search engines, translation, writing assistants) and core prompting methods. |
| **00:25 – 00:45** | 20 min | **Interactive Demonstration & Group Practice** | Large-group guided prompting demonstrations with live examples, encouraging patrons to follow along on personal devices or guided worksheets. |
| **00:45 – 00:55** | 10 min | **Critical Evaluation, Privacy & Ethics** | Discussion on spotting misinformation and hallucinations, preserving privacy, and evaluating generative content responsibly. |
| **00:55 – 01:00** | 5 min | **Q&A, Evaluation & Next Steps** | Group Q&A, session feedback collection, and sharing library digital resources for ongoing self-paced learning. |

---

## 6. Accessibility Notes
- **Physical Access**: Community Hall provides full step-free access for attendees and presenter.
- **Audiovisual Setup**: Wall-mounted projector and screen provide clear viewing for an audience of 35.
- **Printed Materials**: Handouts will be printed in high-contrast, large-print format for ease of reading.

---

## 7. Data Sources & Verification
- `data/request.json`: Baseline workshop parameters.
- `data/rooms.csv`: Room capacity, audiovisual capabilities, accessibility status, and facility fees.
- `data/policy.json`: Fee structures, optional refreshment terms, and proposal status requirements.
- **Verification Tool**: Evaluated via deterministic constraint checker (`python3 check_plan.py --attendees 35 --budget 100`), confirming Community Hall without refreshments as the sole feasible option with 0 constraint violations.
