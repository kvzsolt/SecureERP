from model.hr import hr
from view import terminal as view
import model.date_manager as date_manager

ID = 0
NAME = 1
DATE_OF_BIRTH = 2
DEPARTMENT = 3
CLEARANCE = 4


def list_employees():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    contents_of_hr.insert(0, hr.HEADERS)
    view.print_table(contents_of_hr)


def add_employee():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    id_for_new_data = hr.util.generate_id()
    new_data = view.get_inputs(hr.HEADERS[1:])
    new_data.insert(0, id_for_new_data)
    contents_of_hr.append(new_data)
    hr.data_manager.write_table_to_file(hr.DATAFILE, contents_of_hr)


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    trans_subscribed_hr = list(zip(*contents_of_hr))
    while True:
        id_to_delete = view.get_input(hr.HEADERS[ID])
        if id_to_delete == "0":
            return
        else:
            try:
                index_to_delete = trans_subscribed_hr[ID].index(id_to_delete)
                break
            except ValueError:
                view.print_error_message("\nInvalid ID.\n")
                continue
    del contents_of_hr[index_to_delete]
    hr.data_manager.write_table_to_file(hr.DATAFILE, contents_of_hr)


def get_oldest_and_youngest():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    oldest_hr = min(contents_of_hr, key=lambda x: x[DATE_OF_BIRTH].strip("-"))
    youngest_hr = max(contents_of_hr, key=lambda x: x[DATE_OF_BIRTH].strip("-"))
    oldest_and_youngest_hr = oldest_hr[NAME], youngest_hr[NAME]
    view.print_general_results(oldest_and_youngest_hr, "Oldest and youngest employees")


def get_average_age():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    dates_of_births = list(map(lambda x: x[DATE_OF_BIRTH], contents_of_hr))
    average_age = sum(map(lambda x: 2022 - int(x[:4]), dates_of_births)) / len(dates_of_births)  # Task forbid using other
                                                                                            # modules (such as datetime)
    view.print_general_results(average_age, "Average age of employees")


def next_birthdays():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    date_to_check = date_manager.get_valid_date()
    days_of_date_to_check = date_manager.convert_to_days(date_to_check, 2)
    birthday_within_2_weeks = filter(lambda x: 15 > abs(date_manager.convert_to_days(x[DATE_OF_BIRTH], 2)
                            - days_of_date_to_check), contents_of_hr) # This covers +/-14 days, and puts out result even
                                                                      # if the date is before the person's birth year
    names_of_birthday_within_2_weeks = list(map(lambda x: x[NAME], birthday_within_2_weeks))
    view.print_general_results(names_of_birthday_within_2_weeks, hr.HEADERS[NAME])


def count_employees_with_clearance():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    number_of_input_lvl_clearance_employees = sum(map(lambda x: 0 < int(x[CLEARANCE]), contents_of_hr))
    view.print_general_results(number_of_input_lvl_clearance_employees,
                               "Number of input or higher level clearance employees")


def count_employees_per_department():
    contents_of_hr = hr.data_manager.read_table_from_file(hr.DATAFILE)
    department_list = list(map(lambda x: x[DEPARTMENT], contents_of_hr))
    department_employees_dict = {department: department_list.count(department) for department in set(department_list)}
    view.print_general_results(department_employees_dict, "Number of employees of each department")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
