# Gradebook CLI — Dictionary CRUD App

A simple command-line gradebook built in Python to practice dictionaries, functions, and input validation. Manages student names and marks with a menu-driven interface.

## Features

- **Add** a new student with a validated mark (1–100)
- **Remove** a student record
- **Edit** an existing student's mark (with the same 1–100 validation)
- **View all** students and their marks
- Input validation at every step — no crashes on bad input, clear feedback on invalid choices

## How It Works

Student records are stored in a dictionary (`name: marks`), giving fast lookup and update by key. Each operation (add/remove/edit) is wrapped in its own function, keeping the main menu loop clean and each piece of logic easy to test and reuse.

```python
gradebook = {"Alan": 89, "Sarah": 69, "Kevin": 87, "Jimmy": 68}
```

## Usage

```bash
python gradebook.py
```

You'll see a menu:

```
1. Add Student
2. Remove Student Data
3. Edit Student Data
4. View All Student Data
5. Exit
```

Enter the number for the action you want, then follow the prompts.

## Example

```
Enter Option: 1
Enter student name: Zunera
Enter marks: 95
```

## Validation Rules

- Menu choice must be a digit (checked with `.isdecimal()` before conversion to `int`)
- Marks must fall between 1 and 100 inclusive — anything outside that range is rejected with a message
- Adding a student that already exists, or editing/removing one that doesn't, is handled gracefully rather than crashing

## Concepts Practiced

- Dictionaries as a key-value data store
- Functions for separating concerns (single-responsibility per operation)
- String vs. numeric type handling (`isdecimal()`, `int()`)
- Defensive programming — validating input before trusting it
- CRUD pattern (Create, Read, Update, Delete) — the same pattern used in databases and, later, SQL

## Why This Project

This is part of my Python → Data Science learning path. The CRUD pattern here is a direct stepping stone toward working with Pandas DataFrames and, eventually, SQL — both of which involve the same create/read/update/delete operations on structured data.

## Possible Next Steps

- Add `try/except` for non-integer marks input
- Persist data to a CSV or JSON file instead of resetting on exit
- Add a search/sort feature (e.g. view students sorted by marks)

---
*Part of my Python Foundations → Data Science learning journey.*
