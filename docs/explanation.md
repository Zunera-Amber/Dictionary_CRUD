# Project Notes: Gradebook (Dictionary CRUD App)

**Track:** Python Foundations — Dictionaries & Functions
**Type:** Mini-project (real-world pattern: CRUD tool)

---

## What This Project Is

A command-line gradebook that stores student names and marks in a dictionary,
with menu-driven options to add, remove, edit, and view records. This is a
**CRUD app** — Create, Read, Update, Delete.

---

## Core Concepts Practiced

### 1. Dictionaries as a mini-database
```python
gradebook = {"Alan": 89, "Sarah": 69, "Kevin": 87, "Jimmy": 68}
```
Keys = student names, values = marks. Dictionaries are the natural structure
for "lookup by name" — much faster and more readable than searching a list.

### 2. Functions wrapping each operation
Each CRUD action got its own function (`add_student`, `remove_student`,
`edit_student`) — keeps the menu loop clean and each piece of logic testable
on its own.

### 3. Accessing/modifying dict values
- Read: `gradebook[name]`
- Write/update: `gradebook[name] = marks`
- Delete: `del gradebook[name]`
- Membership check: `if name in gradebook`

### 4. Input validation, in the right order
Learned to validate the **string** before converting type:
```python
choice = input("Enter Option: ")
if choice.isdecimal():        # check while it's still a string
    choice = int(choice)      # convert only after confirming it's valid
```
`.isdecimal()` is a string method — calling it on an int (after converting
too early) throws an error. Order of operations matters.

### 5. Range validation for data integrity
```python
if marks in range(1, 101):
    gradebook[name] = marks
else:
    print("Marks should be in between 1-100.")
```
Key catch: `range(1, 101)` is needed (not `range(1, 100)`) because `range()`
excludes its stop value — this is a classic off-by-one trap.

---

## Bugs Found & Fixed (in order)

| Bug | Fix |
|---|---|
| `gradebook{name}` — wrong bracket type | `gradebook[name]` |
| `choice.isdecimal` — method not called | `choice.isdecimal()` |
| `choice == 1` compared string to int | Convert `choice` to `int` first |
| Converted to `int` *before* checking `.isdecimal()` | Validate as string first, convert after |
| `marks` stored as string | Wrapped in `int(input(...))` |
| Inconsistent casing (`"sarah"` vs `"Sarah"`) | Standardized capitalization — dict keys are case-sensitive |
| No `else` for out-of-range marks | Added feedback message in both `add_student` and `edit_student` |
