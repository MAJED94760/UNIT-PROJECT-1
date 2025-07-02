class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def set_expense(self, category, amount):
        expense = Expense(category, amount)
        self.expenses.append(expense)
        print(f"✅ {amount} SAR added to {category}")

    def list_expenses(self):
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        print("\n📄 Expenses Summary:")
        for exp in self.expenses:
            print(f"{exp.category}: {exp.amount:.2f} SAR")
