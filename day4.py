import random as rm

random_integer = rm.randint(1,5)
print(random_integer)

random_floating_num = rm.uniform(1,5)
print(random_floating_num)

heads_or_tails = rm.randint(0,1)

if heads_or_tails == 0:
    print("Tails")
else:
    print("Head")

names = input("Enter Names:")
names_list = names.split(",")
the_person_to_pay = names_list[rm.randint(0,len(names_list))]
print(the_person_to_pay)

names = input("Enter Names: ")
names_list = names.split(",")
person_who_will_pay = rm.choice(names_list)
print(person_who_will_pay)

row1 = ['0','0','0']
row2 = ['0','0','0']
row3 = ['0','0','0']

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Enter number:")

vertical = int(position[0])
horizontal = int(position[1])

map[vertical-1][horizontal-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

user_choice = input ("Enter 0 for rock , 1 for scissors or 2 for paper\n")

if int(user_choice) == 0:
    print("Rock\n")
if int(user_choice) == 1:
    print("Scissors\n")
if int(user_choice) == 2:
    print("Paper\n")

ran_choice = rm.randint(0,2)

if ran_choice == 0:
    print("Rock")
if ran_choice == 1:
    print("Scissors")
if ran_choice == 2:
    print("Paper")

if ran_choice == int(user_choice):
    print("Its a Draw!")
if ran_choice == 0 and int(user_choice) == 1:
    print("You lost!")
if ran_choice == 1 and int(user_choice) == 0:
    print("You won")
