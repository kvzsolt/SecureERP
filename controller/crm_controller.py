from model.crm import crm
from view import terminal as view

ID = 0
NAME = 1
EMAIL = 2
SUBSCRIBED = 3


def list_customers():
    contents_of_crm = crm.data_manager.read_table_from_file(crm.DATAFILE)
    contents_of_crm.insert(0, crm.HEADERS)
    view.print_table(contents_of_crm)


def add_customer():
    contents_of_crm = crm.data_manager.read_table_from_file(crm.DATAFILE)
    id_for_new_data = crm.util.generate_id()
    new_data = view.get_inputs(crm.HEADERS[1:])
    new_data.insert(0, id_for_new_data)
    contents_of_crm.append(new_data)
    crm.data_manager.write_table_to_file(crm.DATAFILE, contents_of_crm)


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    contents_of_crm = crm.data_manager.read_table_from_file(crm.DATAFILE)
    trans_subscribed_crm = list(zip(*contents_of_crm))
    while True:
        id_to_delete = view.get_input(crm.HEADERS[ID])
        if id_to_delete == "0":
            return
        else:
            try:
                index_to_delete = trans_subscribed_crm[ID].index(id_to_delete)
                break
            except ValueError:
                view.print_error_message("\nInvalid ID.\n")
                continue
    del contents_of_crm[index_to_delete]
    crm.data_manager.write_table_to_file(crm.DATAFILE, contents_of_crm)


def get_subscribed_emails():
    contents_of_crm = crm.data_manager.read_table_from_file(crm.DATAFILE)
    subscribed_crm = filter(lambda x: x[SUBSCRIBED] == "1", contents_of_crm)
    trans_subscribed_crm = list(zip(*subscribed_crm))
    view.print_general_results(trans_subscribed_crm[EMAIL], "Subscribed emails")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
