100 days of coding: Day3 Challenge 2

Love calculator

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

love = "love"
true = "true"

t = combined_names.count(true[0])
r = combined_names.count(true[1])
u = combined_names.count(true[2])
e = combined_names.count(true[3])
l = combined_names.count(love[0])
o = combined_names.count(love[1])
v = combined_names.count(love[2])
e = combined_names.count(love[3])

total_love = l + o + v + e
total_true = t + r + u + e

add = str(total_true) + str(total_love)
add = int(add)

if add < 10 or add > 90:
print(f"Your score is {add}, you go together like coke and mentos.")
elif add >=40 and add <=50:
print(f"Your score is {add}, you are alright together.")
else:
print(f"Your score is {add}.")