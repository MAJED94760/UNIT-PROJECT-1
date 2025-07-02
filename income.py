class IncomeManager:
    def __init__(self):
        self.income = 0
        self.allocation = {'Needs': 0, 'Wants': 0, 'Savings/Debt': 0}

    def set_income(self, amount):
        self.income = amount
        self.allocation['Needs'] = amount * 0.5
        self.allocation['Wants'] = amount * 0.3
        self.allocation['Savings/Debt'] = amount * 0.2

    def show_allocation(self):
        print("\n💰 Income Allocation:")
        for key, value in self.allocation.items():
            print(f"{key}: {value:.2f} SAR")
