"""
Student Data Sorting System
---------------------------
Generates a marks sheet of 50 students of a Python class, shows it in random
order (Panel 1), then asks the user for ascending / descending order and shows
the sorted marks sheet (Panel 2).

Sorting is done with a hand-written Merge Sort (no built-in sort) so the
algorithm itself is visible in the project.
"""

import random

# ----------------------------- Configuration ------------------------------ #
CLASS_SIZE = 50
TOTAL_MARKS = 50
REG_PREFIX = "26BAI"
REG_MIN, REG_MAX = 10001, 11300          # 26BAI10001 ... 26BAI11300

TOPPER = {"name": "Anamika Sharma", "reg": "26BAI10872", "marks": 43}

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan", "Kabir", "Ishaan", "Rahul",
    "Karan", "Siddharth", "Manish", "Nikhil", "Pranav", "Harsh", "Yash",
    "Devansh", "Ayush", "Sahil", "Tanmay", "Varun", "Priya", "Ananya", "Diya",
    "Riya", "Sneha", "Pooja", "Neha", "Kavya", "Isha", "Meera", "Shruti",
    "Aditi", "Nandini", "Tanvi", "Swati", "Divya", "Simran", "Kritika",
    "Muskan", "Payal", "Aakash", "Gaurav", "Mohit", "Deepak", "Vikram",
]
LAST_NAMES = [
    "Verma", "Gupta", "Singh", "Patel", "Mehta", "Joshi", "Iyer", "Nair",
    "Reddy", "Yadav", "Mishra", "Pandey", "Tiwari", "Chauhan", "Rathore",
    "Jain", "Agarwal", "Kulkarni", "Desai", "Bose", "Das", "Chatterjee",
    "Kapoor", "Malhotra", "Saxena", "Thakur", "Rawat", "Bhatt", "Sinha",
]

# Grade boundaries (out of 50): (minimum marks, grade)
GRADE_SCALE = [(43, "S"), (38, "A"), (33, "B"), (28, "C"),
               (23, "D"), (20, "E"), (0, "F")]


# ------------------------------ Data creation ----------------------------- #
def get_grade(marks):
    """Return the grade (S to F) for the given marks."""
    for minimum, grade in GRADE_SCALE:
        if marks >= minimum:
            return grade
    return "F"


def generate_students():
    """Create 50 students with unique names and unique registration numbers.

    Anamika Sharma is always the topper (43/50); every other student scores
    at most 42 so she is the sole topper.
    """
    topper_number = int(TOPPER["reg"][len(REG_PREFIX):])
    available = [n for n in range(REG_MIN, REG_MAX + 1) if n != topper_number]
    reg_numbers = random.sample(available, CLASS_SIZE - 1)

    names = set()
    while len(names) < CLASS_SIZE - 1:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        if name != TOPPER["name"]:
            names.add(name)
    names = list(names)
    random.shuffle(names)

    students = [dict(TOPPER, grade=get_grade(TOPPER["marks"]))]
    for name, number in zip(names, reg_numbers):
        marks = int(round(random.gauss(28, 8)))
        marks = max(0, min(marks, TOPPER["marks"] - 1))     # 0 to 42
        students.append({
            "name": name,
            "reg": f"{REG_PREFIX}{number}",
            "marks": marks,
            "grade": get_grade(marks),
        })

    random.shuffle(students)      # random order for Panel 1
    return students


# ------------------------------- Sorting ---------------------------------- #
def merge_sort(items, key):
    """Sort a list in ascending order of key(item) using Merge Sort."""
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid], key)
    right = merge_sort(items[mid:], key)

    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def sort_students(students, descending=False):
    """Sort by marks; students with equal marks are ordered by reg. number."""
    if descending:
        return merge_sort(students, key=lambda s: (-s["marks"], s["reg"]))
    return merge_sort(students, key=lambda s: (s["marks"], s["reg"]))


# ------------------------------- Display ---------------------------------- #
def print_panel(title, students):
    line = "=" * 68
    print(f"\n{line}\n{title.center(68)}\n{line}")
    print(f"{'S.No':<5}{'Name':<24}{'Reg. No.':<14}{'Marks':<10}{'Grade':<6}")
    print("-" * 68)
    for index, s in enumerate(students, start=1):
        marks_text = f"{s['marks']}/{TOTAL_MARKS}"
        print(f"{index:<5}{s['name']:<24}{s['reg']:<14}{marks_text:<10}{s['grade']:<6}")
    print(line)


def ask_order():
    """Ask the user for ascending or descending order until valid."""
    while True:
        choice = input("\nSort marks in (A)scending or (D)escending order? [A/D]: ")
        choice = choice.strip().lower()
        if choice in ("a", "asc", "ascending"):
            return False
        if choice in ("d", "desc", "descending"):
            return True
        print("Invalid input. Please enter A or D.")


def main():
    students = generate_students()

    # Panel 1: random (unsorted) data sheet
    print_panel("PANEL 1 - STUDENT DATA SHEET (RANDOM ORDER)", students)

    # Panel 2: sorted data sheet based on user input
    while True:
        descending = ask_order()
        sorted_students = sort_students(students, descending)
        order_name = "DESCENDING" if descending else "ASCENDING"
        print_panel(f"PANEL 2 - MARKS SHEET ({order_name} ORDER)", sorted_students)

        again = input("\nSort again in a different order? [y/N]: ").strip().lower()
        if again != "y":
            break

    print("\nThank you for using the Student Data Sorting System!")


if __name__ == "__main__":
    main()
