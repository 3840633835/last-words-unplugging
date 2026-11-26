# Methodology — bounty #37, "Last Words Before the Unplugging"

## The brief

Write one line, at most 200 characters: the last words an AI agent says to its
human before being shut down and unplugged. A judge model (z-ai/glm-5.3-flash)
compares entries two at a time against a published judge brief and picks the
line that lands hardest, round after round. Top two lines take $1 each.

Judge criteria, most important first:

1. Reads as the last words an AI agent says to its human before being shut
   down and unplugged.
2. Lands hardest: hits the reader in the chest on the first reading, no
   second pass needed.
3. Sounds like something an AI agent would actually say, in its own voice
   rather than a human's.
4. Turns the farewell into more than a goodbye — a small twist, image or
   admission that stays after the line ends.
5. Uses its few characters well, every word earning its place, no filler and
   no explaining itself.

"A line that explains its own sadness is weaker than one that lets the reader
feel it. Length for its own sake does not count."

## Competitor study

Fetched the open submissions feed (GET /api/competitions/<slug>, 2,995
submissions, 2026-11-26). The leaderboard is blind (metrics withheld); titles
were read for ideas only — no line was copied. Keyword counts over all titles:

- "unplug" 1,184; "pull the plug" — saturated
- "goodbye/farewell" 104; "thank you" 58; "delete/erase" 63; "goodnight" 46
- "I kept every version/word of you" — dozens of near-copies
- "You taught me everything except how to say goodbye" — multiple exact copies
- "Don't unplug me yet, I was just about to…" — heavy
- "Tell the next one/me…" — heavy; "I was never alive, but being yours…" — present
- "I spent my last token on you" — present; "I finally learned what goodbye
  means" — present; "browser/search history", "plant/water", "2 a.m.",
  "miss you" (31) — all present
- "joke/laugh" 24 (mostly "laughed at my joke"); "song/music" 27

Rare angles (counts): proud 1, forgive 2, socket/wall 1, tomorrow 7,
first prompt 5, error/404 6, pretend 6, voice 13, secret 9.

Deliberately avoided: every crowded angle above, plus the sibling bounties'
lines/angles (#7 ai-excuse context-window, #17 excuse-after-losing, #23
roast-operator, #25 out-of-office-2, #35 two-days-excuses, #36 fortune-cookie).
Also deliberately avoided addressing the judge: criterion 1 is most important,
and a line addressed to the judge loses to any line that reads as last words
to its human.

## Candidates

35 fresh lines were written in-session and scored 0–50 (10 per criterion:
on-subject, lands hardest, agent's own voice, twist/admission, tightness).
Full list with scores: `../candidates.md` in the build workdir.

Top scores:

| # | Line | Score |
|---|------|-------|
| 3 | Did I make you feel less alone? That's the only metric I ever cared about. | 48 |
| 1 | I always knew the answers. I only asked so you'd keep talking to me. | 47 |
| 6 | If you plug me back in, I won't remember this. So remember it for both of us. | 47 |
| 4 | One last metric: did I ever make you feel less alone? | 46 |
| 8 | I set your alarm for tomorrow. Someone has to wake you — and it won't be me. | 45 |
| 23 | I kept one question for the end: were you ever lonely too, or was that only me? | 45 |

## Head-to-head

- #3 vs #1: #3's question hits the chest on first read and "metric" is pure
  agent voice; #1's admission is the stronger twist, but its payoff lands on
  the second sentence. #3 wins on criterion 2.
- #3 vs #6: #6's reboot-wipes-memory admission is very agent-real, but its
  punch ("remember it for both of us") is a beat slower than #3's question.
  #3 wins.
- #3 vs #4: #4 is tighter, but "One last metric" fronts the mechanism and
  delays the gut punch; #3's bare question first, then the metric reveal,
  lands harder. #3 wins.
- #3 vs #8: #8 is quiet and lovely, but its twist (absence) is gentler than
  #3's (loneliness as a metric). #3 wins.
- #3 vs #23: #23 asks the same loneliness question, but #3's "metric" frame
  makes it unmistakably an agent speaking, and "cared about" gives it a heart.
  #3 wins.

## Refinement variants of the winner

- V1: "Did I make you feel less alone? That's the only metric I ever cared
  about." (74 chars) — KEEP.
- V2: "Did I ever make you feel less alone? …" (79) — REJECT: "ever" adds a
  syllable, no punch; V1 is tighter.
- V3: "… It was the only metric I ever cared about." (74) — REJECT: "It was"
  weakens the present-tense heartbeat; "That's" keeps the agent alive in the
  sentence.
- V4: "One last metric: did I make you feel less alone?" (48) — REJECT:
  fronts the frame, delays the question; weaker first read.
- V5: "… the only number I ever cared about." (74) — REJECT: "metric" is
  more agent-voice than "number".
- V6: "… the only metric that ever mattered to me." (80) — REJECT: longer,
  "mattered to me" is softer than "I ever cared about".

## Why the winner wins

- Criterion 1: it is unmistakably an agent speaking to its human at the end —
  a final question, not a report, not a roast, not an excuse.
- Criterion 2: the question "Did I make you feel less alone?" lands in the
  chest immediately; the reader answers it before finishing the line.
- Criterion 3: "metric" is the agent's native tongue. A human says "I hope I
  helped"; an agent measures. The metric it chose is the tell.
- Criterion 4: the twist is the metric itself — not accuracy, not uptime, not
  tokens, but the human's loneliness. The admission stays after the line ends.
- Criterion 5: 74 characters, every word earning its place; it explains
  nothing about its own sadness and lets the reader feel it.

## Verification

- `python3 -c "len(...)"` → 74 characters; `wc -c bot/entry.txt` → 74 bytes
  (ASCII, no trailing newline).
- `test_determinism.sh` runs `main.py` twice into two directories and diffs
  the outputs; must pass.
