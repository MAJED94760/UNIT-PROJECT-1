from income import IncomeManager
from expenses import ExpenseManager
from ai_module import SimpleAI
from report import Report, show_dashboard


def main():
    print("\n🔷 Welcome to Smart Financial Analyzer 🔷")

    income_manager = IncomeManager()
    expense_manager = ExpenseManager()

    try:
        income_amount = float(input("\n💰 Enter your monthly income (SAR): "))
        income_manager.set_income(income_amount)

        print("\nEnter your monthly expenses:")
        needs = float(input("   → Needs (Rent, Bills, Essentials): "))
        wants = float(input("   → Wants (Entertainment, Shopping): "))
        savings = float(input("   → Savings/Debt payments: "))

        expense_manager.set_expense('Needs', needs)
        expense_manager.set_expense('Wants', wants)
        expense_manager.set_expense('Savings/Debt', savings)

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    income_manager.show_allocation()
    expense_manager.list_expenses()

    ai = SimpleAI(income_manager, expense_manager)
    ai.analyze()
    investment_amount, years, debt_amount = ai.suggest_plan()

    report = Report(income_manager, expense_manager)
    report.show_summary()

    show_dashboard(income_manager, expense_manager, investment_amount, years, debt_amount)

    choice = input("\n🔄 Do you want to analyze again? (y/n): ")
    if choice.lower() == 'y':
        main()
    else:
        print("👋 Thank you for using Smart Financial Analyzer.")


if __name__ == '__main__':
    main()
