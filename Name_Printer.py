# File Name: Name_Printer
# Author Name: Aneesh Vasudevan
# Email Address: Aneesh1Vasu@gmail.com
#Enivironment: Python 3
# Log of Change: Version 3

username = input("Enter your name: ")

print(f"Your name is {username}")

print("---------------------------------------------------------------")

flip_name = username[::-1]

print("This is your name flipped: ", flip_name)

print("---------------------------------------------------------------")

fav_num = input("What is your favourite number: ")

print("Counting up to your favourite number squared can be given as follows: ")

for i in range(0,int(fav_num)+1):
    print(i**2)


print("---------------------------------------------------------------")

engineer1_name = input("What is Engineer 1's name: ")
engineer1_type = input("What type of engineer is Engineer 1: ")
engineer1_XP = input("What is Engineer 1's years of experience: ")

print("---------------------------------------------------------------")

engineer2_name = input("What is Engineer 2's name: ")
engineer2_type = input("What type of engineer is Engineer 2: ")
engineer2_XP = input("What is Engineer 2's years of experience: ")



class Engineers:

    skill = "problem solver"

    def __init__(self, engineer_name, engineer_type, years_of_experience):
        self.engineer_name = engineer_name
        self.engineer_type = engineer_type
        self.years_of_experience = years_of_experience

engineer1 = Engineers(engineer1_name, engineer1_type, engineer1_XP )
engineer2 = Engineers(engineer2_name, engineer2_type, engineer2_XP )


print(f"Engineer 1 is called {engineer1.engineer_name}, and is a {engineer1.engineer_type} engineer with {engineer1.years_of_experience} years experience")
print(f"Engineer 2 is called {engineer2.engineer_name}, and is a {engineer2.engineer_type} engineer with {engineer2.years_of_experience} years experience")




