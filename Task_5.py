income = int(input("Enter your month income in $: "))
expenses = int(input("Enter your month expenses in $: "))
if income < 0:
    expenses -= income
    income = 0
if expenses < 0:
    income -= expenses
    expenses = 0

profit = income - expenses
if profit > 0:
    print(f"Well done! You earned {profit} $")
    efficiency = profit / income * 100
    print(f"The month efficiency is {efficiency} %")
    headcount = int(input("How many people did work in this month? "))
    perEmployee = profit / headcount
    print(f"Every employee earned {perEmployee} $ in this month.")
else:
    print(f"You lost in this month {-profit} $")
