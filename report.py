import matplotlib.pyplot as plt


class Report:
    def __init__(self, income_manager, expense_manager):
        self.income = income_manager
        self.expenses = expense_manager

    def show_summary(self):
        totals = {'Needs': 0, 'Wants': 0, 'Savings/Debt': 0}
        for exp in self.expenses.expenses:
            if exp.category in totals:
                totals[exp.category] += exp.amount

        print("\n📊 Financial Report:")
        print("Category       | Budget  | Spent  | Difference")
        print("------------------------------------------------")
        for cat, budget in self.income.allocation.items():
            spent = totals.get(cat, 0)
            diff = budget - spent
            print(f"{cat:<14} | {budget:<7.2f} | {spent:<7.2f} | {diff:.2f}")


def show_dashboard(income_manager, expense_manager, investment_amount, years=25, debt_amount=0):
    labels = ['Needs', 'Wants', 'Savings/Debt']
    income_values = [
        income_manager.allocation['Needs'],
        income_manager.allocation['Wants'],
        income_manager.allocation['Savings/Debt']
    ]

    expense_totals = {'Needs': 0, 'Wants': 0, 'Savings/Debt': 0}
    for exp in expense_manager.expenses:
        if exp.category in expense_totals:
            expense_totals[exp.category] += exp.amount

    expense_values = [
        expense_totals['Needs'],
        expense_totals['Wants'],
        expense_totals['Savings/Debt']
    ]

    plt.figure(figsize=(18, 6))

    # 🔵 1. Pie chart for Income vs Expenses Distribution
    plt.subplot(1, 3, 1)
    sizes = [sum(income_values), sum(expense_values)]
    labels_pie = ['Income Budget', 'Total Expenses']
    colors = ['#66b3ff', '#ff9999']
    plt.pie(sizes, labels=labels_pie, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Income vs Expenses Distribution')

    # 🟢 2. Investment Growth Chart
    plt.subplot(1, 3, 2)
    years_range = list(range(1, years + 1))
    values = []
    value = 0
    rate = 0.09
    for year in years_range:
        for _ in range(12):
            value = value * (1 + rate / 12) + investment_amount
        values.append(value)

    plt.plot(years_range, values, marker='o', color='green')
    plt.title(f'Investment Growth Over {years} Years')
    plt.xlabel('Year')
    plt.ylabel('SAR')
    plt.grid(True)

    # 🔴 3. Debt Repayment Chart
    plt.subplot(1, 3, 3)
    monthly_payment = income_manager.allocation['Savings/Debt']
    if monthly_payment > 0 and debt_amount > 0:
        months = int(debt_amount / monthly_payment) + 1
        x_months = list(range(1, months + 1))
        debt_remaining = [max(debt_amount - monthly_payment * i, 0) for i in range(months)]
        plt.bar(x_months, debt_remaining, color='red')
        plt.title(f'Debt Repayment Plan ({months} months)')
        plt.xlabel('Month')
        plt.ylabel('Remaining Debt (SAR)')
    else:
        plt.text(0.5, 0.5, 'No Debt', fontsize=14, ha='center')
        plt.axis('off')

    plt.tight_layout()
    plt.show()
