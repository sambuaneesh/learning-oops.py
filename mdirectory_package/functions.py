from prettytable import PrettyTable
from common.fuzzy_search import fuzzy_search

fields = [
    "first_name",
    "last_name",
    "roll_number",
    "course_name",
    "semester",
    "exam_type",
    "total_marks",
    "scored_marks",
]


def get_attribute():
    attributes_table = PrettyTable()
    attributes_table.field_names = ["Attribute"]
    for field in fields:
        attributes_table.add_row([field])
    print(attributes_table)
    return fuzzy_search(input("Enter Attribute: "), fields)
