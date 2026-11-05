# Librarian Agent Demo — Antigravity (Two-Round Version)

## Goal
Demonstrate an AI agent reading fictional library planning data, running a Python constraint checker, saving a proposal, and updating it after a librarian changes the requirements. No infeasible/conflict scene. Proposed rooms are NOT booked.

## Setup (0:00–0:55)
1. Unzip this project and open the `librarian-agent-demo` folder in Google Antigravity using File > Open Folder.
2. Show `AGENTS.md`, `data/request.json`, and `data/rooms.csv` in the Explorer.
3. Open Agent Chat (on Mac, try Cmd+L; use the Agent button if your version differs). Use local workspace access and review command approvals.
4. Open Terminal > New Terminal and run `python3 --version`. Optionally run `python3 check_plan.py` to test the checker before recording.

## Round 1 — Initial planning (0:55–1:55)
Paste into the built-in Antigravity Agent Chat:

```text
Read AGENTS.md and act as my Library Workshop Planner.
Plan a 60-minute AI basics workshop for 20 adult library patrons with an $80 budget.
Read the project data, run check_plan.py, and select a feasible room.
Include refreshments if they fit the budget.
Save a detailed proposal to output/event_plan.md, including an itemized budget and a 60-minute agenda.
Explain your tool actions briefly. Label the plan as a proposal, not a confirmed booking.
```

Expected result: Reading Room, 20 attendees, $0 room + $40 materials + $20 refreshments = $60 within $80. Open `output/event_plan.md` to show the result.

## Round 2 — Direct revision (1:55–2:45)
In the SAME chat, paste:

```text
Let's revise the workshop plan.
We now expect 35 attendees, and the approved budget is $100.
Remove refreshments, but keep the 60-minute duration, projector requirement, and step-free access.
Run check_plan.py again with the updated inputs.
Select a suitable room and update output/event_plan.md with the new budget and agenda.
Do not claim the room is booked.
```

Expected tool call:

```bash
python3 check_plan.py --attendees 35 --budget 100
```

Expected result: Community Hall, 35 attendees, $30 room + $70 materials + $0 refreshments = $100.

## Review and close (2:45–3:30)
Open `output/event_plan.md` again and compare attendees (20 → 35), budget ($80 → $100), room (Reading Room → Community Hall), refreshments ($20 → $0), and cost ($60 → $100). Conclude: the agent works with files, checks constraints with a tool, and revises the proposal; a librarian must still review and book the room.

## CapCut subtitles
Import `Librarian_Agent_Antigravity_CapCut_EN.srt` into CapCut's captions/subtitle import feature. Timing assumes a 3:30 edited video, not real-time execution. Adjust caption timestamps after editing the recording. Subtitle language: English.

All project data are fictional. Python checker is not the AI; the built-in Antigravity agent controls the workflow.
