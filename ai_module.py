class SimpleAI:
    def __init__(self, income_manager, expense_manager):
        self.income = income_manager
        self.expenses = expense_manager

    def analyze(self):
        totals = {'Needs': 0, 'Wants': 0, 'Savings/Debt': 0}
        for exp in self.expenses.expenses:
            if exp.category in totals:
                totals[exp.category] += exp.amount

        total_spent = sum(totals.values())
        total_budget = sum(self.income.allocation.values())

        print("\n🤖 Financial Analysis:")

        if total_spent > total_budget:
            print(f"⚠️ You are overspending by {total_spent - total_budget:.2f} SAR.")
        elif total_spent < total_budget:
            print(f"✅ You are saving {total_budget - total_spent:.2f} SAR. Good job!")
        else:
            print("✔️ Your spending matches your budget exactly.")

    def suggest_plan(self):
        savings_for_investment = self.income.allocation['Savings/Debt']

        if savings_for_investment <= 0:
            print("\n❌ You have no available savings for investment.")
            return 0, 0, 0

        print("\n💡 Suggestions:")
        print("- ✅ You can start an investment or debt repayment plan.")

        # ✅ Investment calculation
        years = 25
        rate = 0.09
        investment = 0
        for _ in range(years * 12):
            investment = investment * (1 + rate / 12) + savings_for_investment

        print(f"- 📈 If you invest {savings_for_investment} SAR monthly, it can grow to {investment:.2f} SAR in {years} years (9% annual return).")

        # ✅ Debt calculation
        try:
            debt_amount = float(input("\n💳 Do you have any debt? Enter total amount (SAR) or 0 if none: "))
            if debt_amount > 0:
                months = int(debt_amount / savings_for_investment)
                print(f"- 💸 You can finish paying {debt_amount} SAR debt in approximately {months} months.")
            else:
                print("- 🎉 You are debt free!")
        except ValueError:
            debt_amount = 0
            print("❌ Invalid input for debt. Assuming no debt.")

        return savings_for_investment, years, debt_amount
