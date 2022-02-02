print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12 o 15? "))
spl_peop = int(input("How many people to split the bill? "))

total_amount = total_bill * (percent/100 + 1)
spl_amount = total_amount / spl_peop

print(f"Each person should pay: ${round(spl_amount,2)}")
