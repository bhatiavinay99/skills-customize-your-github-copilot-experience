# 📘 Assignment: Working with Databases using SQLite & SQLAlchemy

## 🎯 Objective

Learn how to persist data in a relational database by using SQLAlchemy ORM to define a schema, connect to a SQLite database, and perform full CRUD (Create, Read, Update, Delete) operations from Python.

## 📝 Tasks

### 🛠️ Define a Database Schema

#### Description
Set up a SQLAlchemy engine connected to a SQLite database and define a `Student` model with the ORM.

#### Requirements
Completed program should:

- Create a SQLAlchemy engine connected to a file named `school.db`.
- Define a `Student` ORM model (mapped to a `students` table) with the columns: `id` (integer primary key, auto-increment), `name` (string, required), and `grade` (integer, required).
- Call `Base.metadata.create_all()` to create the table in the database.
- Example: running the script should create `school.db` on disk with the `students` table.

### 🛠️ Insert and Query Records

#### Description
Write functions to add new students to the database and retrieve them.

#### Requirements
Completed program should:

- Implement `add_student(name, grade)` that opens a session, creates a `Student` instance, adds it, and commits the transaction.
- Implement `get_all_students()` that returns a list of all `Student` records.
- Implement `get_students_by_grade(grade)` that returns only students with the given grade.
- Example usage:
  ```python
  add_student("Alice", 10)
  add_student("Bob", 11)
  print(get_students_by_grade(10))  # [<Student id=1 name='Alice' grade=10>]
  ```

### 🛠️ Update and Delete Records

#### Description
Write functions to modify and remove existing student records.

#### Requirements
Completed program should:

- Implement `update_student_grade(student_id, new_grade)` that finds the student by `id` and updates their `grade`, then commits.
- Implement `delete_student(student_id)` that finds the student by `id`, deletes the record, and commits.
- Return `True` if the operation succeeded, or `False` if no student with that `id` was found.
- Example usage:
  ```python
  update_student_grade(1, 11)  # True
  delete_student(99)           # False — no such student
  ```
