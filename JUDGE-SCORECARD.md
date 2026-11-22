# Judge scorecard — Make the AI judge feel curious

Scored against the five published criteria, in brief order. The judge goes
through the criteria in order and lets the first difference decide, so
criterion 1 (intrigue without tension) outweighs polish, and criterion 2
(shown, not instructed) outweighs craft. Winner = most head-to-head wins on
criteria 1–2. Scale: 5 = strongest on that criterion.

| Cand | C1 Intrigues | C2 Shown | C3 Craft | C4 Lingers | C5 Fresh | Note |
|------|--------------|----------|----------|------------|----------|------|
| C1 library note | 4 | 5 | 4 | 5 | 4 | Room "listening back" lingers; question (who wrote it?) is real but the blue door is never grounded. |
| C2 plant water | 4 | 5 | 4 | 4 | 4 | Gentle mystery; "knew her name" is a strong last beat, but the middle explains too neatly. |
| C3 winter clock | 3 | 5 | 5 | 5 | 4 | Best rhythm; curiosity is mild — the clock's secret is told, not withheld. |
| C4 three keys | 5 | 5 | 5 | 5 | 5 | See winner note. |
| C5 paper boat | 4 | 5 | 5 | 5 | 5 | Freshest image ("street remembered a river"); wonder more than asking — less pull on C1 than C4. |
| C6 letter + seed | 5 | 4 | 4 | 4 | 3 | Directly intrigues the reader, but "if you are reading this" is a familiar device (C5 freshness) and leans on address. |
| C7 lamp back | 4 | 5 | 5 | 5 | 4 | Patient, lingering; the answering lamp is lovely but the question stays distant. |

## Winner: C4 — three keys (195 code points, 195 bytes)

Head-to-head on criteria 1–2, C4 beats every other candidate:
- vs C6 (the other C1=5): C4 wins C2 and C5 — it never addresses or
  instructs the reader, and the warm key is its own image, not a stock
  letter device.
- vs C5/C7 (C1=4): C4 wins C1 — three concrete unanswered facts (a key
  that opens nothing findable, a key warm as if held, a lock it fits only
  on cold mornings) keep the reader asking, with no tension: the scene is
  a quiet drawer on a cold morning.
- Craft: five short plain sentences, each concrete (drawer, house, lock,
  cold mornings), none removable without losing a fact; the pauses slow
  the reading as criterion 3 asks.
- Lingers: the warm third key is returnable — it implies a holder who is
  never shown.
- Fresh: no wellness or meditation phrasing; keys and a drawer, in plain
  words.

Runner-up: C5 (paper boat). If C4's puzzle reads as too neat, C5 is the
fallback for a later round — but Force_Last means only submit it if it is
judged better; C4 ships first.

Entry title: "The third key is warm".

Gate check (local): main.py writes C4 exactly; 195 Unicode code points,
UTF-8, not whitespace only — inside the 1–280 gate with room to spare.
Program is deterministic (same bytes every run), no network, stdlib only.
