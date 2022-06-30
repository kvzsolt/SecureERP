def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print("\n" + title + ":", end="")
    print()
    for i in range(len(list_options)):
        if i + 1 < len(list_options):
            print(f"({i + 1}) {list_options[i + 1]}")
    print(end="")
    print(f"(0) {list_options[0]} \n")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if isinstance(result, (int, float, complex)):
        print("\n{}: {:.2f}".format(label, result))
    elif isinstance(result, (list, tuple)):
        print(f"\n{label}:")
        print(*result, sep="; ")
    elif isinstance(result, dict):
        print(f"\n{label}")
        print('; '.join(['{}: {}'.format(k, v) for k, v in result.items()]))
    else:
        print(f"\n{label}: {result}")

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    start_decor = "/"
    mid_decor = "-"
    end_decor = "\\"
    split_decor = "|"
    len_table = [list(map(lambda x: len(x), element)) for element in table]
    max_len_list = [max(element) for element in list(zip(*len_table))]
    max_print_len = sum(max_len_list) + (3 * len(max_len_list)) + 1  # 2 spaces and 1 split_decor for each element,
                                                                     # and a last split_decor for each line
    print(f"{start_decor}{mid_decor * (max_print_len - 2)}{end_decor}", end="")
    print()
    for i in range(len(table[0])):
        print(f"{split_decor} {table[0][i].center(max_len_list[i])} ", end="")
    print(split_decor)
    print(end="")
    for i in range(len(table)):
        if i + 1 < len(table):
            for j in range(len(table[i])):
                print(f"{split_decor}{(mid_decor * (max_len_list[j] + 2)).center(max_len_list[j] + 2)}", end="")
            print(split_decor)
            for j in range(len(table[i])):
                print(f"{split_decor} {table[i+1][j].center(max_len_list[j])} ", end="")
            print(split_decor)
    print(f"{end_decor}{mid_decor * (max_print_len - 2)}{start_decor}")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f"{label}: ")
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_input_list = []
    for label in labels:
        user_input = input(f"{label}: ")
        user_input_list.append(user_input)
    return user_input_list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
