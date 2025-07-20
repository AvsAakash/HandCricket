# 🏏 Hand Cricket Game through console
---

##  **Features**

- Toss system using Odd or Even logic
- Turn-based gameplay: choose to Bat or Bowl
- Computer opponent with random moves
- Scoring system with run tracking and win/loss logic
- Option to play multiple games in a single session
- Input validation for a smooth user experience

---

## **Technologies Used**

- **Python 3**
- Python Standard Library:
  - `random` for opponent move generation
  - `input()` for player interaction

---

## Gameplay Overview 

1. Toss
   - Player chooses "Odd" or "Even"
   - Both player and computer select a number
   - Sum determines toss winner
   - Toss winner selects to Bat or Bowl

2. Batting/Bowling 
   - Each turn, both player and computer select a run (1–6)
   - If both select the same number, the batsman is OUT
   - Otherwise, runs are added to the batsman's total

3. Second Innings
   - Roles reverse
   - The second player tries to beat the opponent's score

4. Result
   - Game declares the winner and gives an option to restart or stop

---

##  How to Run

Make sure Python 3 is installed on your system.

```bash
python Hand_Cricket.py
