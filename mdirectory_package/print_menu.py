from prettytable import PrettyTable


def print_menu(option):
    try:
        option = int(option)
    except ValueError:
        print("Invalid option!")
        return False
    menu_table = PrettyTable()
    if option == 0:
        menu_table.field_names = ["Option", "Description"]
        menu_table.add_row(["1", "Add New Entry"])
        menu_table.add_row(["2", "CSV File"])
        menu_table.add_row(["3", "Display Marks Directory"])
        menu_table.add_row(["4", "Remove Entry"])
        menu_table.add_row(["5", "Update Entry"])
        menu_table.add_row(["6", "Search Entries"])
        menu_table.add_row(["0", "Exit"])
        print(menu_table)
    elif option == 1:
        print("***** Add New Entry Menu *****")
        print("Enter details for the new entry:")
        # Provide prompts for entering details (e.g., first name, last name, roll number, etc.)
    elif option == 2:
        print("***** Load Entries from CSV File Menu *****")
        print("Enter the path of the CSV file to load entries from:")
    elif option == 3:
        print("***** Display Marks Directory *****")
        # Display directory using PrettyTable
    elif option == 4:
        print("***** Remove Entry Menu *****")
        print("Enter attribute and value to remove the entry:")
    elif option == 5:
        print("***** Update Entry Menu *****")
        print("Enter attribute, value, and new value to update the entry:")
    elif option == 6:
        print("***** Search Entries Menu *****")
        print("Enter attribute and value to search the entries:")
    else:
        print("Invalid option!")
        return False
    return True
