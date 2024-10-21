from dao.IFinance import IFinance
from entity.user import User
from entity.expense import Expense
from util.DbConnUtil import DbConnUtil
import pyodbc

class FinanceImpl(IFinance):
    def __init__(self):
        self.connection = DbConnUtil.getConnection()

    def create_user(self, user):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Users (user_id, username, password, email) VALUES (?, ?, ?, ?)", 
                           (user.user_id, user.username, user.password, user.email))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating user: {e}")
            return False

    def create_expense(self, expense):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Expenses (expense_id, user_id, amount, category_id, date, description) VALUES (?, ?, ?, ?, ?, ?)",
                           (expense.expense_id, expense.user_id, expense.amount, expense.category_id, expense.date, expense.description))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating expense: {e}")
            return False

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
            if cursor.rowcount == 0:
                print(f"User with ID {user_id} not found.")
                return False
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting user: {e}")
            return False

    def delete_expense(self, expense_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM Expenses WHERE expense_id = ?", (expense_id,))
            if cursor.rowcount == 0:
                print(f"Expense with ID {expense_id} not found.")
                return False
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting expense: {e}")
            return False

    def get_all_expenses(self, user_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM Expenses WHERE user_id = ?", (user_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching expenses for user ID {user_id}: {e}")
            return []

    def update_expense(self, user_id, expense):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                UPDATE Expenses 
                SET amount = ?, category_id = ?, date = ?, description = ?
                WHERE expense_id = ? AND user_id = ?
            """, (expense.amount, expense.category_id, expense.date, expense.description, expense.expense_id, user_id))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating expense: {e}")
            return False





