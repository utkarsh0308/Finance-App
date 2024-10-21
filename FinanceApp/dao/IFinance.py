from abc import ABC, abstractmethod

class IFinance(ABC):

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def create_expense(self, expense):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass

    @abstractmethod
    def delete_expense(self, expense_id):
        pass

    @abstractmethod
    def get_all_expenses(self, user_id):
        pass

    @abstractmethod
    def update_expense(self, user_id, expense):
        pass
