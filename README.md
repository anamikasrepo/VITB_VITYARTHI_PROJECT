# 🎓 Student Marks Sorting System


BY-
ANAMIKA SHARMA
REG - 26BAI10872
VITYARTHI PROJECT FOR PYTHON PROGRAMMING 

#About 

A beginner-friendly Python project that creates a marks sheet for **50 students** of a Python class and sorts it in **ascending or descending order of marks**, based on user input.

The output is shown in two panels:

| Panel | What it shows |
|-------|---------------|
| **Panel 1** | Data sheet (Name, Reg. No., Marks, Grade) in **random order** |
| **Panel 2** | The same data sheet **sorted** in the order the user chooses (ascending / descending) |

---

## ✨ Features

- 50 students data
- **Unique registration numbers** from `26BAI10001` to `26BAI11300`
- Marks between **0 and 50**, with grades from **S to F**
- Class topper is fixed: **Anamika Sharma, 26BAI10872, 43/50 (Grade S)**
- Sorting with **Bubble Sort** written using simple loops (no built-in `sort()`)
- Input validation and an option to sort again
- Only Python's standard library (`random`), nothing to install

---

## 📊 Grading Scale (out of 50)

| Marks | Grade |
|-------|-------|
| 43 – 50 | S |
| 38 – 42 | A |
| 33 – 37 | B |
| 28 – 32 | C |
| 23 – 27 | D |
| 20 – 22 | E |
| 0 – 19 | F |

---

## 🐍 Python Concepts Used

Variables & constants · Lists · Dictionaries · `if / elif / else` · `for` and `while` loops · Functions · `random` module · `input()` and `print()` · f-strings

---

## 🚀 How to Run

**Requirements:** Python 3.6 or above

```bash
git clone https://github.com/anamikasrepo/student-data-sorting-system.git
cd student-data-sorting-system
python main.py
```

---

## 🖥️ Sample Output

```
==================================================================
           PANEL 1 - STUDENT DATA SHEET (RANDOM ORDER)
==================================================================
S.No  Name                    Reg. No.      Marks     Grade
------------------------------------------------------------------
1     Riya Rathore            26BAI10203    36/50     B
2     Ananya Mishra           26BAI10892    29/50     C
3     Rahul Verma             26BAI10997    32/50     C
...

Sort marks in (A)scending or (D)escending order? [A/D]: D

==================================================================
            PANEL 2 - MARKS SHEET (DESCENDING ORDER)
==================================================================
S.No  Name                    Reg. No.      Marks     Grade
------------------------------------------------------------------
1     Anamika Sharma          26BAI10872    43/50     S
2     Payal Rathore           26BAI10261    42/50     A
...
```

> Apart from the topper, names, registration numbers and marks are randomly generated on every run.

---

## 🧠 How It Works

1. `generate_students()` creates the fixed topper plus 49 random students (marks up to 42, so Anamika stays first).
2. `get_grade()` converts marks into a grade with an `if / elif` chain.
3. The shuffled list is shown as **Panel 1**.
4. `ask_order()` asks for `A` (ascending) or `D` (descending) until the input is valid.
5. `bubble_sort()` compares neighbouring students and swaps them if needed; the result is shown as **Panel 2**.

---

## 📁 Project Structure

```
student-marks-sorting-system/
├── main.py            # Complete source code
├── Project_Report.docx
└── README.md
```
## 👤 Author

**Anamika Sharma** – Reg. No. 26BAI10872, SCAI, VIT Bhopal University
GitHub: [anamikasrepo](https://github.com/anamikasrepo)
