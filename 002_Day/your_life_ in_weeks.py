# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Example Input
# 56

# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

left_months = (90 - int(age)) * 12
left_weeks = (90 - int(age)) * 52
left_days = (90 - int(age)) * 365
print(f'You have {left_days}, {left_weeks} weeks, and {left_months} left.')






