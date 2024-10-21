from entity.user import User
from entity.expense import Expense
from dao.financeImpl import FinanceImpl
from exception.userNotFoundException import UserNotFoundException
from exception.expenseNotFoundException import ExpenseNotFoundException

def main_menu():
    # Create an instance of FinanceImpl
    finance_impl = FinanceImpl()

    while True:
        print("1. Add User\n2. Add Expense\n3. Delete User\n4. Delete Expense\n5. Update Expense\n6. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            user_id = input("Enter user_id: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user = User(user_id=user_id, username=username, password=password, email=email)
            
            # Call the method on the instance of FinanceImpl
            success = finance_impl.create_user(user)
            
            if success:
                print("User created successfully.")
            else:
                print("Failed to create user.")

        elif choice == 2:
            expense_id = input("Enter expense_id: ")
            user_id = input("Enter user_id: ")
            amount = float(input("Enter amount: "))
            category_id = input("Enter category_id: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            expense = Expense(expense_id=expense_id, user_id=user_id, amount=amount, category_id=category_id, date=date, description=description)

            success = finance_impl.create_expense(expense)

            if success:
                print("Expense added successfully.")
            else:
                print("Failed to add expense.")

        elif choice == 3:
            user_id = input("Enter user ID to delete: ")
            try:
                finance_impl.delete_user(user_id)
                print("User deleted successfully.")
            except UserNotFoundException as e:
                print(e)

        elif choice == 4:
            expense_id = input("Enter expense ID to delete: ")
            try:
                finance_impl.delete_expense(expense_id)
                print("Expense deleted successfully.")
            except ExpenseNotFoundException as e:
                print(e)

        elif choice == 5:
            expense_id = input("Enter expense ID to update: ")
            user_id = input("Enter user ID: ")
            amount = float(input("Enter new amount: "))
            category_id = input("Enter new category ID: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            description = input("Enter new description: ")
            expense = Expense(expense_id=expense_id, user_id=user_id, amount=amount, category_id=category_id, date=date, description=description)

            success = finance_impl.update_expense(user_id, expense)
            if success:
                print("Expense updated successfully.")
            else:
                print("Failed to update expense.")

        elif choice == 6:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
