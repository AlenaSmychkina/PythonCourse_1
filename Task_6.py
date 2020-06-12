
day = 1
start = int(input("Enter how many km you ran on the 1st day: "))
plan = int(input("Enter how many km you are planning to run: "))
progress = start
while progress < plan:
    day += 1
    progress *= 1.1
print(f"You need {day} day(s) to reach your plan")

