import json

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def display_expenses(self):
        for expense in self.expenses:
            print(expense)

if __name__ == '__main__':
    tracker = ExpenseTracker()
    tracker.add_expense(50.0, 'Food', 'Lunch at a restaurant')
    tracker.display_expenses()
