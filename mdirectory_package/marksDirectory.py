from mdirectory_package.marksEntry import MarksEntry
from prettytable import PrettyTable
import csv


class MarksDirectory:
    def __init__(self):
        self.entries = []
        self.attributes = [
            "first_name",
            "last_name",
            "roll_number",
            "course_name",
            "semester",
            "exam_type",
            "total_marks",
            "scored_marks",
        ]

    def add_entry(self, entry):
        try:
            assert isinstance(entry, MarksEntry)
            for e in self.entries:
                if e.is_same(entry):
                    raise AssertionError
            self.entries.append(entry)
            return True
        except AssertionError:
            return False

    def load_from_csv(self, file_name):
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    entry = MarksEntry(*row)
                    # check if entry already exists
                    for e in self.entries:
                        if e.roll_number == entry.roll_number:
                            continue
                    self.entries.append(entry)
            return True
        except FileNotFoundError:
            return False

    def save_to_csv(self, file_name):
        try:
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                for entry in self.entries:
                    # convert entry to list
                    entry = list(entry.__dict__.values())
                    writer.writerow(entry)
            return True
        except FileNotFoundError:
            return False

    def remove_entry(self, attribute, value):
        entry = self.find_unique(attribute, value)
        if entry:
            for e in self.entries:
                if e.is_same(entry):
                    self.entries.remove(e)
                    return True
        else:
            return False

    def update_entry(self, attribute, old_value):
        # if attribute is not in attributes_list
        if attribute not in self.attributes:
            return None
        entry = self.find_unique(attribute, old_value)
        for e in self.entries:
            if e.is_same(entry):
                new_value = input(f"Enter new {attribute}: ")
                ok = entry.update_entry(attribute, new_value)
                return ok
        return None

    def search_entry(self, attribute, value):
        found_entries = self.find_all(attribute, value)
        if found_entries:
            return found_entries
        else:
            return None

    def find_all(self, attribute, value):
        mini_directory = MarksDirectory()
        for entry in self.entries:
            if hasattr(entry, attribute) and getattr(entry, attribute) == value:
                mini_directory.add_entry(entry)
        if mini_directory:
            return mini_directory
        else:
            return None

    def find_unique(self, attribute, value):
        mini_directory = self.find_all(attribute, value)
        if mini_directory.length() > 1:
            print(mini_directory)
            print(
                "\n Total Entries: ",
                len(mini_directory.entries),
                "\n",
                "Choose an entry by its S.No:",
            )
            return mini_directory[int(input()) - 1]
        elif mini_directory.length() == 1:
            return mini_directory[0]
        else:
            return None

    def length(self):
        return len(self.entries)

    def __repr__(self):
        table = PrettyTable()
        table.field_names = [
            "S.No.",
            "First Name",
            "Last Name",
            "Roll Number",
            "Course Name",
            "Semester",
            "Exam Type",
            "Total Marks",
            "Scored Marks",
        ]
        for i, entry in enumerate(self.entries):
            table.add_row(
                [
                    i + 1,
                    entry.first_name,
                    entry.last_name,
                    entry.roll_number,
                    entry.course_name,
                    entry.semester,
                    entry.exam_type,
                    entry.total_marks,
                    entry.scored_marks,
                ]
            )
        return str(table)

    def __getitem__(self, index):
        return self.entries[index]
