#  Number Guessing Game (Python)

A simple command-line game where the computer picks a secret number between 1 and 100 and the player keeps guessing until they get it right, with "too high" or "too low" hints after each wrong guess.

---

##  Overview

This project practices core Python fundamentals: random number generation, user input, type conversion, `while` loops, and conditional logic.

**How the game works:**

1. The computer picks a random whole number from 1 to 100
2. The player types a guess
3. If the guess is wrong, the game says whether it was too high or too low
4. This repeats until the player guesses the number
5. The game prints "Correct!" and the number of tries

---

---

##  How to Run

Make sure [Python 3](https://www.python.org/downloads/) is installed, then run:

```bash
python guessing_game.py
```

**Example run**

```
42
Write a random number? 50
Too high. Try again
Write a random number? 30
Too low, Try again
Write a random number? 42
Correct!
You got it in 1 tries
```

---

##  Concepts Demonstrated

| Concept | Where it appears |
|---|---|
| **Random numbers** | `random.randint(1, 100)` picks the secret number |
| **User input** | `input()` collects each guess |
| **Type conversion** | `int(...)` turns the typed text into a number |
| **`while` loop** | Repeats until the guess equals the secret number |
| **`if` / `elif`** | Decides between "too high" and "too low" |
| **Counter variable** | `question_count` is meant to track the number of tries |
| **f-strings** | `f"You got it in {question_count} tries"` builds the final message |

