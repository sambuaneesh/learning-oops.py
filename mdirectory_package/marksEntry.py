from __future__ import annotations
from prettytable import PrettyTable


class MarksEntry:
    def __init__(
        self,
        first_name,
        last_name,
        roll_number,
        course_name,
        semester,
        exam_type,
        total_marks,
        scored_marks,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number
        self.course_name = course_name
        self.semester = semester
        self.exam_type = exam_type
        self.total_marks = total_marks
        self.scored_marks = scored_marks

    def update_entry(self, attribute, value):
        # print all attributes
        if hasattr(self, attribute):
            setattr(self, attribute, value)
            return value
        else:
            return None

    def is_same(self, entry: MarksEntry) -> bool:
        return (
            self.first_name == entry.first_name
            and self.last_name == entry.last_name
            and self.roll_number == entry.roll_number
            and self.course_name == entry.course_name
            and self.semester == entry.semester
            and self.exam_type == entry.exam_type
        )

    def __str__(self):
        entry = PrettyTable()
        entry.field_names = [
            "First Name",
            "Last Name",
            "Roll Number",
            "Course Name",
            "Semester",
            "Exam Type",
            "Total Marks",
            "Scored Marks",
        ]
        entry.add_row(
            [
                self.first_name,
                self.last_name,
                self.roll_number,
                self.course_name,
                self.semester,
                self.exam_type,
                self.total_marks,
                self.scored_marks,
            ]
        )
        return str(entry)
