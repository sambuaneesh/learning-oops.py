from prettytable import PrettyTable
from mdirectory_package.marksEntry import MarksEntry
from mdirectory_package.marksDirectory import MarksDirectory
from common.clear import clear
from mdirectory_package.print_menu import print_menu
from mdirectory_package.functions import get_attribute


def main():
    marks_directory = MarksDirectory()
    while True:
        print_menu(0)
        option = input("Enter an option: ")
        clear()

        ok = print_menu(option)
        if not ok:
            continue

        if option == "0":
            clear()
            break
        elif option == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            roll_number = input("Enter Roll Number: ")
            course_name = input("Enter Course Name: ")
            semester = input("Enter Semester: ")
            exam_type = input("Enter Exam Type: ")
            total_marks = input("Enter Total Marks: ")
            scored_marks = input("Enter Scored Marks: ")
            new_entry = MarksEntry(
                first_name,
                last_name,
                roll_number,
                course_name,
                semester,
                exam_type,
                total_marks,
                scored_marks,
            )
            ok = marks_directory.add_entry(new_entry)
            if ok:
                input("\nEntry Added!\nPress Enter to continue...")
            else:
                input("\nEntry already exists!\nPress Enter to continue...")
        elif option == "2":
            menu_table = PrettyTable()
            menu_table.field_names = ["Option", "Description"]
            menu_table.add_row(["1", "Load Entries from CSV File"])
            menu_table.add_row(["2", "Save Entries to CSV File"])
            print(menu_table)
            csv_option = input("Enter an option: ")
            if csv_option == "1":
                file_name = input(
                    "Enter the path of the CSV file to load entries from: "
                )
                ok = marks_directory.load_from_csv(file_name)
                if not ok:
                    print("File not found!")
            elif csv_option == "2":
                try:
                    file_name = input(
                        "Enter the path of the CSV file to save entries to: "
                    )
                    ok = marks_directory.save_to_csv(file_name)
                    if not ok:
                        print("File not found!")
                except:
                    print("Something is Wrong!")
        elif option == "3":
            directory_table = PrettyTable()
            directory_table.field_names = [
                "First Name",
                "Last Name",
                "Roll Number",
                "Course Name",
                "Semester",
                "Exam Type",
                "Total Marks",
                "Scored Marks",
            ]
            for entry in marks_directory.entries:
                directory_table.add_row(
                    [
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
            print(directory_table)
            input("Press Enter to continue...")
        elif option == "4":
            input_attribute = get_attribute()
            input_value = input("Enter Value: ")
            removed_entry = marks_directory.remove_entry(input_attribute, input_value)
            if removed_entry:
                print("Removed Entry Successfully!")
                input("\nPress Enter to continue...")
            else:
                input("Entry not found!\nPress Enter to continue...")
        elif option == "5":
            attribute = get_attribute()
            old_value = input("Enter Old Value: ")
            ok = marks_directory.update_entry(attribute, old_value)
            if ok:
                input("Entry Updated!\nPress Enter to continue...")
            else:
                input("Entry not found!\nPress Enter to continue...")
        elif option == "6":
            attribute = get_attribute()
            value = input("Enter Value: ")
            found_entries = marks_directory.search_entry(attribute, value)
            if found_entries:
                print(found_entries)
            else:
                print("Entry not found!")
            input("\nPress Enter to continue...")
        else:
            input("Press Enter to continue...")
        clear()


if __name__ == "__main__":
    main()
