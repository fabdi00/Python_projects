100 days of coding: Day 2, Challenge #3

Final bill per person calculator

bill = input("welcome to the tip calculator\nwhat was the total bill? £")

tip = input("what percentage tip would you like to give? 10, 12, or 15? ")

number_of_people = input("how many people will split the bill?")

calculate_tip = float(bill) * (int(tip) / 100)
bill_pp = (float(bill) + calculate_tip) / int(number_of_people)
final_bill = (round(bill_pp, 2))

print(f"pay £{final_bill} per person")