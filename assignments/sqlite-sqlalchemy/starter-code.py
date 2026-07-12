from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

# Task 1 — Database setup
# Create an engine connected to 'school.db'
engine = None  # Replace with create_engine(...)


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    # Define columns: id (primary key), name (String), grade (Integer)
    pass


# Create all tables
# Base.metadata.create_all(engine)


# Task 2 — Insert and query
def add_student(name: str, grade: int):
    # Open a session, create a Student, add and commit
    pass


def get_all_students():
    # Return a list of all Student records
    pass


def get_students_by_grade(grade: int):
    # Return students filtered by grade
    pass


# Task 3 — Update and delete
def update_student_grade(student_id: int, new_grade: int) -> bool:
    # Find student by id, update grade, commit; return True on success, False if not found
    pass


def delete_student(student_id: int) -> bool:
    # Find student by id, delete, commit; return True on success, False if not found
    pass
