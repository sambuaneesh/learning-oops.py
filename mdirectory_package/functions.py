from prettytable import PrettyTable
import difflib

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


def fuzzy_search(query, choices, cutoff=0.6):
    matches = difflib.get_close_matches(query, choices, n=1, cutoff=cutoff)
    if matches:
        return matches[0]
    else:
        return None


def get_attribute():
    attributes_table = PrettyTable()
    attributes_table.field_names = ["Attribute"]
    for field in fields:
        attributes_table.add_row([field])
    print(attributes_table)
    return fuzzy_search(input("Enter Attribute: "), fields)
