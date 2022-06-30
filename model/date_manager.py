from view import terminal as view

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30


def convert_to_days(date, mode=1):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    if mode == 1:  # Counting the days of passed years from AD also.
        counted_days = 0
        for i in range(year):
            if leap_year(i):
                counted_days += 366
            else:
                counted_days += 365
        for i in range(month):
            if i + 1 < month:
                counted_days += days_in_month(i + 1, year)
        counted_days += day
        return counted_days
    if mode == 2:  # Counting the days without passed year.
        counted_days_without_year = 0
        for i in range(month):
            if i + 1 < month:
                counted_days_without_year += days_in_month(i + 1, year)
        counted_days_without_year += day
        return counted_days_without_year

def get_valid_date():
     while True:
        date_to_check = view.get_input("\nType the date in YYYY-MM-DD format")
        separator = "-"
        try:
            year_to_check = int(date_to_check[:4])
            month_to_check = int(date_to_check[5:7])
            day_to_check = int(date_to_check[8:10])
            if len(date_to_check) == 10 and date_to_check[4] == separator and date_to_check[7] == separator \
                    and month_to_check > 0 and month_to_check < 13 and \
                    day_to_check <= days_in_month(month_to_check, year_to_check):
                return date_to_check
            else:
                view.print_error_message("\nInvalid date or format.\n")
        except ValueError:
            view.print_error_message("\nInvalid input.\n")