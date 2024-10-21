import unittest
from unittest.mock import patch, MagicMock
from dao.financeImpl import FinanceImpl
from entity.user import User
from entity.expense import Expense

class TestFinanceImpl(unittest.TestCase):

    @patch('dao.financeimpl.DbConnUtil.getConnection')
    def setUp(self, mock_get_connection):
        # Mock the database connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor
        mock_get_connection.return_value = self.mock_connection
        
        # Initialize the FinanceImpl with the mocked connection
        self.finance_impl = FinanceImpl()

    def test_create_user_success(self):
        # Arrange
        user = User(user_id=1, username="test_user", password="password123", email="test@example.com")
        self.mock_cursor.execute.return_value = None  # No exception thrown
        self.mock_cursor.rowcount = 1
        
        # Act
        result = self.finance_impl.create_user(user)

        # Assert
        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Users (user_id, username, password, email) VALUES (?, ?, ?, ?)",
            (user.user_id, user.username, user.password, user.email)
        )
        self.assertTrue(result)

    def test_create_expense_success(self):
        # Arrange
        expense = Expense(expense_id=1, user_id=1, amount=100.50, category_id=1, date="2024-10-21", description="Lunch")
        self.mock_cursor.execute.return_value = None  # No exception thrown
        self.mock_cursor.rowcount = 1
        
        # Act
        result = self.finance_impl.create_expense(expense)

        # Assert
        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Expenses (expense_id, user_id, amount, category_id, date, description) VALUES (?, ?, ?, ?, ?, ?)",
            (expense.expense_id, expense.user_id, expense.amount, expense.category_id, expense.date, expense.description)
        )
        self.assertTrue(result)

    def test_get_all_expenses_success(self):
        # Arrange
        user_id = 1
        mock_expenses = [(1, 1, 100.50, 1, "2024-10-21", "Lunch")]
        self.mock_cursor.fetchall.return_value = mock_expenses
        
        # Act
        result = self.finance_impl.get_all_expenses(user_id)

        # Assert
        self.mock_cursor.execute.assert_called_once_with("SELECT * FROM Expenses WHERE user_id = ?", (user_id,))
        self.assertEqual(result, mock_expenses)

    def test_create_user_exception(self):
        # Arrange
        user = User(user_id=1, username="test_user", password="password123", email="test@example.com")
        self.mock_cursor.execute.side_effect = Exception("Database error")
        
        # Act
        result = self.finance_impl.create_user(user)

        # Assert
        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO Users (user_id, username, password, email) VALUES (?, ?, ?, ?)",
            (user.user_id, user.username, user.password, user.email)
        )
        self.assertFalse(result)

    def test_delete_user_not_found(self):
        # Arrange
        user_id = 1
        self.mock_cursor.rowcount = 0
        
        # Act
        result = self.finance_impl.delete_user(user_id)

        # Assert
        self.mock_cursor.execute.assert_called_once_with("DELETE FROM Users WHERE user_id = ?", (user_id,))
        self.assertFalse(result)

    def test_update_expense_exception(self):
        # Arrange
        expense = Expense(expense_id=1, user_id=1, amount=150.75, category_id=2, date="2024-10-22", description="Dinner")
        self.mock_cursor.execute.side_effect = Exception("Update failed")

        # Act
        result = self.finance_impl.update_expense(expense.user_id, expense)

        # Assert
        self.mock_cursor.execute.assert_called_once_with(
            """
            UPDATE Expenses 
            SET amount = ?, category_id = ?, date = ?, description = ?
            WHERE expense_id = ? AND user_id = ?
            """, (expense.amount, expense.category_id, expense.date, expense.description, expense.expense_id, expense.user_id)
        )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
