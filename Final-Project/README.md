# Budget Tracker

#### Video Demo: https://youtu.be/GWEbIUT17Ns
#### Description:

**Budget Tracker** is a Python-based financial management tool developed as my final project for the CS50P course by HarvardX. This application is designed to assist individuals in managing their monthly budget by tracking income and expenses effectively. It offers an intuitive interface for users to add, categorize, and review their financial data, making personal finance more accessible and understandable.

### Purpose

The goal of the Budget Tracker is to simplify personal finance management. In today's fast-paced world, keeping track of daily expenditures can be challenging. This tool allows users to see exactly where their money goes each month, helping them make informed decisions to optimize their financial habits. By providing insights into spending patterns and budget adherence, Budget Tracker empowers users to achieve their financial goals, whether saving for a future event, managing debt, or simply maintaining a healthier financial lifestyle.

### How It Works

Budget Tracker operates through a command-line interface, guiding users through various functionalities with clear prompts and feedback. Here’s a breakdown of the core functionalities:

- **Income Management:** Users can define and update their monthly income, which the system remembers across sessions thanks to persistent storage.
- **Expense Tracking:** Users input details about each expenditure, including the category. This data is stored in a structured format in a CSV file, allowing for easy manipulation and review.
- **Financial Summary:** The application provides a detailed summary of expenses by category and an overall view of financial health relative to the user’s set budget.

### Detailed Functionalities

- **Settings Menu:** Upon startup, users can choose to enter the settings menu to adjust their monthly income or modify expense categories. This flexibility allows the Budget Tracker to adapt to changing financial situations or preferences.
- **Dynamic Category Management:** Users can add new expense categories or delete existing ones as needed. This dynamic aspect ensures the tool remains relevant and customized to individual user needs.
- **Interactive Expense Input:** Users are prompted to enter expenses, which the system records and categorizes. Each entry is confirmed for correctness, and users can continuously add expenses or conclude the session.

### Exception Handling

Robust exception handling ensures the application operates smoothly and remains user-friendly:

- **Input Validation:** All user inputs for monetary values are validated for correct data type. If a non-numeric value is entered, the system catches a `ValueError`, alerts the user, and requests a valid input.
- **Category Management:** During the addition or deletion of categories, the system ensures valid selections through range checks. If a user attempts to delete a non-existent category, an `IndexError` is caught, and an appropriate message is displayed.
- **Data Integrity:** To prevent data corruption, all file operations are enclosed in try-except blocks. Errors like `FileNotFoundError` and `IOError` are handled to maintain system stability and ensure user data is not lost.

### Design Choices

Several key design choices were made during the development of Budget Tracker:

- **Use of CSV Files:** The choice to use CSV files for storing income and expenses stems from their simplicity and compatibility with various systems and software. This format also facilitates easy data manipulation outside the application.
- **Modular Function Design:** Functions are designed to perform specific tasks (like managing categories or handling expenses) and are encapsulated to enhance maintainability and scalability.
- **Persistent Settings:** Settings such as income and categories are saved immediately upon modification, ensuring that all changes are preserved across sessions without additional user intervention.

### Future Enhancements

Looking ahead, potential enhancements could include graphical representations of expenses, integration with banking APIs for automatic transaction imports, and multi-currency support for users dealing with international expenses.

### Conclusion

Budget Tracker is more than just a financial tool; it is a step towards financial literacy and empowerment. By demystifying personal budgeting and providing a clear, actionable view of financial data, it helps users control their economic destiny.

Thank you for considering Budget Tracker for your financial management needs. Please refer to the video demonstration linked above for a detailed walkthrough of the application's capabilities and usage.



