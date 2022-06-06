import random

names_string = input("Give me everybody's anme, seperated by a comma. ")

names = names_string.split(", ")

num_items = len(names)

# The following code will select a random person to pay the bill.

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
names[random_choice] 

# The code below will do the above work with much less code. dont for get to comment the above code to try the code below

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today.")