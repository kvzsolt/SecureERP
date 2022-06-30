from model.sales import sales
from view import terminal as view
import model.date_manager as date_manager

ID = 0
CUSTOMER = 1
PRODUCT = 2
PRICE = 3
DATE = 4


def list_transactions():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    contents_of_sales.insert(0, sales.HEADERS)
    view.print_table(contents_of_sales)


def add_transaction():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    id_for_new_data = sales.util.generate_id()
    new_data = view.get_inputs(sales.HEADERS[1:])
    new_data.insert(0, id_for_new_data)
    contents_of_sales.append(new_data)
    sales.data_manager.write_table_to_file(sales.DATAFILE, contents_of_sales)


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    trans_subscribed_sales = list(zip(*contents_of_sales))
    while True:
        id_to_delete = view.get_input(sales.HEADERS[ID])
        if id_to_delete == "0":
            return
        else:
            try:
                index_to_delete = trans_subscribed_sales[ID].index(id_to_delete)
                break
            except ValueError:
                view.print_error_message("\nInvalid ID.\n")
                continue
    del contents_of_sales[index_to_delete]
    sales.data_manager.write_table_to_file(sales.DATAFILE, contents_of_sales)


def get_biggest_revenue_transaction():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    highest_price = max(map(lambda x: float(x[PRICE]), contents_of_sales))
    highest_price_transactions = list(filter(lambda x: float(x[PRICE]) == highest_price, contents_of_sales))
    highest_price_transactions.insert(0, sales.HEADERS)
    view.print_message("\nBiggest revenue transaction(s):")
    view.print_table(highest_price_transactions)


def get_biggest_revenue_product():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    products_and_prices_list = list(map(lambda x: [x[PRODUCT], x[PRICE]], contents_of_sales))
    products_and_revenue_dict = {}
    for element in products_and_prices_list:
        if products_and_revenue_dict.get(element[0]) is None:
            products_and_revenue_dict[element[0]] = float(element[1])
        else:
            products_and_revenue_dict[element[0]] += float(element[1])
    revenue_list = list(products_and_revenue_dict.values())
    index_of_max_revenue = revenue_list.index(max(revenue_list))
    product_list = list(products_and_revenue_dict.keys())
    bigges_revenue_product = product_list[index_of_max_revenue]
    view.print_general_results(bigges_revenue_product, "Highest selling product")


def count_transactions_between():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    start_date = date_manager.get_valid_date()
    end_date = date_manager.get_valid_date()
    clean_start_date = start_date.strip("-")
    clean_end_date = end_date.strip("-")
    number_of_transaction = sum(map(lambda x: clean_start_date <= x[DATE].strip("-")
                            and clean_end_date > x[DATE].strip("-"), contents_of_sales))
    print(number_of_transaction)
    view.print_general_results(number_of_transaction, "Number of transactions between given dates")


def sum_transactions_between():
    contents_of_sales = sales.data_manager.read_table_from_file(sales.DATAFILE)
    start_date = date_manager.get_valid_date()
    end_date = date_manager.get_valid_date()
    clean_start_date = start_date.strip("-")
    clean_end_date = end_date.strip("-")
    list_of_transactions_between_dates = list(filter(lambda x: clean_start_date <= x[DATE].strip("-")
                            and clean_end_date > x[DATE].strip("-"), contents_of_sales))
    amount_of_income = sum(list(map(lambda x: float(x[PRICE]), list_of_transactions_between_dates)))
    view.print_general_results(amount_of_income, "Amount of income between given dates")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
