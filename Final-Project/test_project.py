from unittest.mock import mock_open, patch
from project import Expense, get_expense, write_expense, summarize_expense

# Test get_expense.
def test_get_expense(monkeypatch):
    inputs = iter(["Coffee", "2.50", "3"])  # Prepare a list of inputs that simulate the user entering "Coffee", "2.50", and "3" sequentially.
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))  # Use monkeypatch to replace the input function with one that returns the next value in our inputs.
    expense = get_expense()  # Call get_expense, which should now use our mocked inputs.
    assert expense.name == "Coffee"  # Verify that the expense object returned has the correct name.
    assert expense.amount == 2.50  # Verify that the expense object returned has the correct amount.
    assert expense.category == "🥪 - Food"  # Verify that the expense object returned has the correct category.

# Test write_expense.
def test_write_expense():
    expense = Expense("Coffee", "🥪 - Food", 2.50)  # Create an Expense object to be written to file.
    m = mock_open()  # Create a mock open function that simulates file operations.
    with patch("builtins.open", m, create=True):  # Patch the built-in open function so no actual file operations are performed.
        write_expense(expense, "fake_path.csv")  # Call the function that should write to a file.
    m.assert_called_once_with("fake_path.csv", "a")  # Assert that open was called correctly, expecting it to open the file in append mode.
    handle = m()
    handle.write.assert_called_once_with("Coffee,🥪 - Food,2.5\n")  # Assert that the correct data was written to the file handle.

# Test summarize_expense.
def test_summarize_expense(tmp_path):
    d = tmp_path / "sub"  # Setup a temporary directory and file to simulate reading from a file.
    d.mkdir()
    p = d / "expenses.csv"
    p.write_text("Coffee,🥪 - Food,2.5\nTea,🥪 - Food,3.0\n")  # Write mock data to the temporary file.
    budget = 10.0  # Set a mock budget.
    with patch("builtins.print") as mock_print:  # Patch the print function to capture its outputs for assertion.
        summarize_expense(str(p), budget)  # Call the function that reads the file and summarizes expenses.
    mock_print.assert_any_call("💸 Total Spent: $5.50")  # Check that the print function was called with the correct output for total spent.
    mock_print.assert_any_call("🪙  Budget Remaining $4.50")  # Check that the print function was called with the correct output for remaining budget.

