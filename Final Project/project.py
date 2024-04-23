import sys
from datetime import date
from calendar import monthrange

# Create a class for expenses.
class Expense:
    def __init__(self, name, category, amount) -> None:  # This method does not return any value.
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"< Expense: {self.name}, {self.category}, ${self.amount:.2f} >"



def main():
    print("👋 Welcome to Budget Tracker!")
    exp_file_path = "expenses.csv"  # csv file path.
    budget = load_income()  # Load the budget value.
    print(f"💵 Current Income: ${budget:.2f}")

    try:
        while True:
            open_settings = input("Do you want to open the settings menu? [yes/no] --> ").strip().lower()
            if open_settings == "no":
                break
            elif open_settings == "yes":
                option = settings_menu()  # Call settings_menu function to get the user's choice.
                if option == "⚙️ - Set Income":
                    while True:
                        try:
                            new_income = float(input("New income per month: $"))
                            save_income(new_income)  # Call save_income function to save the new income.
                            print(f"💵 New Income Set: ${new_income:.2f}")
                            break
                        except ValueError:  # ValueError handling.
                            print("🔴 Invalid input, please try again.")
                            continue
                elif option == "⚙️ - Add a Category":
                    new_category = input("Enter the name of the new category: ").strip()
                    add_category(new_category)  # Call add_category function to add the new category.
                elif option == "⚙️ - Delete a Category":
                    while True:
                        try:
                            print("Current categories:")
                            for i, category in enumerate(exp_categories):  # Enumerate and print categories.
                                print(f"  {i + 1}) {category}")
                            category_index = int(input(f"Enter the number of the category to delete [1-{len(exp_categories)}]: ")) - 1  # Get the index of the selected category.
                            delete_category(category_index)  # Call delete_category function to remove the selected category.
                            break
                        except ValueError:  # ValueError handling.
                            print("🔴 Invalid input, please choose a valid number.")
                            continue
                        except IndexError:  # IndexError handling.
                            print("🔴 Invalid category number, please try again.")
                            continue
            else:
                print("🔴 Invalid input, please try again.")

        while True:
            expense = get_expense()  # Get user input for expense.
            write_expense(expense, exp_file_path)  # Write their expense to a file.
            summarize_expense(exp_file_path, budget)  # Read the file and summarize expenses.
            while True:
                ask = input("Do you want to enter another expense? [yes/no] --> ").strip().lower()
                if ask == "no":
                    sys.exit("👋 Good bye, see you soon!")
                elif ask == "yes":
                    break
                else:
                    print("🔴 Invalid input, please try again.")

    except EOFError:  # EOFError handling.
        print()
        sys.exit()
    except KeyboardInterrupt:  # KeyboardInterrupt handling.
        print()
        sys.exit()



def settings_menu():
    """ Display settings menu and return the selected option. """
    setting_options = [
        "⚙️ - Set Income",
        "⚙️ - Add a Category",
        "⚙️ - Delete a Category"
    ]
    while True:
        print("Select a setting option:")
        for i, option in enumerate(setting_options):  # Enumerate and print setting options.
            print(f"  {i+1}) {option}")
        try:
            choice = int(input("Enter the option number: ")) - 1  # Get the index of the selected option.
            if 0 <= choice < len(setting_options):
                return setting_options[choice]  # Return the user's choice.
            raise ValueError  # Raise ValueError if the previous conditional is false, to restart the while loop.
        except ValueError:  # ValueError handling.
            print("🔴 Invalid input. Please enter a valid option number.")


def load_income():
    """ Load the income from a file if it exists, otherwise return a default value. """
    try:
        with open("income_settings.txt", "r") as file:  # Open the income_settings file in read mode.
            return float(file.read().strip())  # Read the content, strip whitespace, convert to float, and return the value.
    except (FileNotFoundError, ValueError):  # Catch exceptions if the file is not found or the content is not a valid float.
        return 1500  # Return a default income value of 1500 if there's an error.


def save_income(budget):
    """ Save the income to a file. """
    with open("income_settings.txt", "w") as file:  # Open the income_settings file in writing mode or create the file if it doesn't exist.
        file.write(str(budget))  # Convert the budget value to a string and write it to the file.


def load_categories():
    """ Load categories from a file, or initialize with defaults if the file doesn't exist. """
    try:
        with open("categories.txt", "r") as file:  # Open the categories file in read mode.
            return [line.strip() for line in file if line.strip()]   # Read all non-empty lines, strip whitespace, and return them as a list.
    except FileNotFoundError:  # Catch the exception if the categories file does not exist.
        return [
            "🏠 - Housing", "🚗 - Transportation", "🥪 - Food", "⚒️ - Work",
            "🧾 - Utilities", "👔 - Clothing", "💊 - Healthcare",
            "🎓 - Education", "💰 - Savings", "📽️ - Entertainment"
        ]  # Return a default list of categories if the file doesn't exist.


# Initialize global categories list.
exp_categories = load_categories()


def save_categories():
    """ Save the current categories to a file. """
    with open("categories.txt", "w") as file:  # Open the categories file in writing mode, which will overwrite the existing file.
        for category in exp_categories:
            file.write(category + "\n")  # Write each category to the file, followed by a newline character to separate categories.


def add_category(new_category):
    """ Add a category to the category list if it does not already exist. """
    if new_category not in exp_categories:  # Check if the new_category is not already in the list of categories.
        exp_categories.append(new_category)  # Add the new_category to the exp_categories list.
        save_categories()  # Call save_categories function to update the category list file.
        print(f"✅ Category Added: {new_category}")
    else:
        print("🔴 Category already exists.")


def delete_category(category_index):
    """ Delete a category from the category list. """
    removed_category = exp_categories.pop(category_index)  # Remove the category at the specified index from the list and store the removed category.
    save_categories()  # Call save_categories function to update the category list file.
    print(f"✅ Category Deleted: {removed_category}")


def get_expense():
    """
    Creates and returns an expense object from the Expense class by gathering input parameters from the user.

    The function prompts the user to input three main attributes of an expense:
    - Name of the expense (str)
    - Amount of the expense (float)
    - Category of the expense (selected from a predefined list)

    Returns:
        Expense: An instance of the Expense class initialized with the name, category, and amount.

    Usage:
        The function is designed to interactively collect user inputs via the console. It is used when there is a need
        to create a new expense record and ensure that all entries are validated and correctly categorized.
    """
    exp_name = input("Enter expense name: ")  # Get the expense name.
    while True:
        try:
            exp_amount = float(input("Enter expense amount: $"))  # Get the expense amount in $.
            if type(exp_amount) == float:
                break
        except ValueError:  # ValueError handling.
            print("🔴 Invalid input, please enter a valid number.")
            continue

    while True:
        print("Select a category")
        for i, cat_name in enumerate(exp_categories):  # Enumerate and print categories.
            print(f"  {i+1}) {cat_name}")

        try:
            cat_index = int(input(f"Enter a category number [1 - {len(exp_categories)}]: ")) - 1  # Get the index of the selected category.
        except ValueError:  # ValueError handling.
            print("🔴 Invalid input, please enter a valid number.")
            continue

        try:
            return Expense(exp_name, exp_categories[cat_index], exp_amount)  # Return the expense object from the Expense class.
        except IndexError:  # IndexError handling.
            print("🔴 Invalid category number, please try again.")
            continue


def write_expense(expense, exp_file_path):
    """
    Writes an expense record to a specified file in CSV format ("expenses.csv").

    This function takes an expense object and a file path, appending the expense data to the file. The data is formatted
    as a CSV line with the expense's name, category, and amount. The file will be opened in append mode, which allows
    for adding new expense records without overwriting existing data.

    Parameters:
        expense (Expense): The expense object containing the expense details.
        exp_file_path (str): The file path where the expense record will be saved.

    Returns:
        None

    Side effects:
        - Opens a file and writes a line to it. If the file does not exist, it will be created.
        - If the file or directory is inaccessible, an IOError could be raised.
    """
    with open(exp_file_path, "a") as file:  # Open the expense file in append mode.
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")  # Write a line in the expense csv file.
    print(f"💾 Saving User Expense: {expense} to {exp_file_path}")


def summarize_expense(exp_file_path, budget):
    """
    Summarizes expenses from a given CSV file and compares the total against a specified budget.

    This function reads an expense CSV file ("expenses.csv"), where each line contains details about an individual expense in the format
    "name,category,amount". It constructs expense objects from these lines, aggregates the expenses by category, and
    calculates the total spent. Additionally, it provides a comparison against a provided budget, showing the remaining
    budget, or amount by which the budget was exceeded, and calculates an estimated daily budget for the rest of the month.

    Parameters:
        exp_file_path (str): The file path of the expense CSV file to read.
        budget (float): The total budget available for the period considered.

    Side effects:
        - Prints the summary of expenses by category.
        - Prints the total expenses, budget remaining or exceeded, and daily budget for the remaining days of the month.
    """
    print("📊 Summarizing User Expense")
    expenses: list[Expense] = []  # Create an empty list (expenses) of objects (Expense).
    with open(exp_file_path, "r") as file:  # Open the expense file in read mode.
        lines = file.readlines()  # Get the csv lines.
        for line in lines:
            strip_line = line.strip()  # Strip the line.
            exp_name, exp_category, exp_amount = strip_line.split(",")  # Split the line by ",".
            line_expense = Expense(exp_name, exp_category, float(exp_amount))  # Create the expense object.
            expenses.append(line_expense)  # Add the object to the list.

    amount_by_category = {}  # Create an empty dict.
    for expense in expenses:
        key = expense.category  # Set the key for the dict, where key=category and value=total-expense-of-that-caregory.
        if key in amount_by_category:  # Check if the key already exists.
            amount_by_category[key] += expense.amount  # Add to the existing amount for this category.
        else:
            amount_by_category[key] = expense.amount  # Set the initial amount for this new category.

    print("📜 Expenses By Category:")
    for index in amount_by_category:
        print(f"  {index} ---> ${amount_by_category[index]:.2f}")  # Print total expense for each category.

    total_spent = sum([exp.amount for exp in expenses])  # Get the addition of a list of amounts for each expense (exp) from the object list (expenses).
    print(f"💸 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent  # Calculate the remaining budget.
    if remaining_budget > 0:
        print(f"🪙  Budget Remaining ${remaining_budget:.2f}")

        today = date.today()  # Get the current date.
        days_in_month = monthrange(today.year, today.month)[1]  # Get the number of days in the current month.
        remaining_days = days_in_month - today.day  # Calculate the remaining number of days in the current month.
        daily_budget = remaining_budget / remaining_days  # Get the daily budget for the current month.
        print(f"🗓️  Budget Per Day: ${daily_budget:.2f}")
    else:
        print(f"⚠️  You have gone over budget by ${abs(remaining_budget):.2f}")


if __name__ == "__main__":
    main()
