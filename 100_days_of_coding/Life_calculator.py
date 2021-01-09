100 days of coding: Day2 challenge #2

calculate life in weeks, months and days:

age = input("What is your current age?")

years = 90 - int(age)
days = years * 365
months = years * 12
weeks = years * 52

print(f"You have {months} months, {weeks} weeks, and {days} days left" )