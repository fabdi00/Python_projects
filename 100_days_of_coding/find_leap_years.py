100 days of coding: Day 3, find the Leap years

Understanding how leap year is calculated was tricky, but it's finally here using this method:

Criteria for leap year:

Can you evenly divide the year by 4? Yes | yes
Can you evenly divide the year by 100? No | yes
Can you evenly divide the year by 400? No | yes

year = int(input("Which year do you want to check? "))

if year % 4==0 and year % 100==0 and year % 400==0:
print(f"{year} is a Leap Year")
elif year % 4 ==0 and year %100 !=0 and year % 400 !=0:
print(f"{year} is a Leap Year")
else:
print(f"{year} is not a Leap Year")