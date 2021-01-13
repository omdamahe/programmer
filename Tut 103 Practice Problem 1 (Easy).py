'''The task you have to perform is
“Your Age In 2090”.
This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable.
Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
'''


print("Welcome to the age calculator:")
def start():
    Exit = False
    while Exit is not True:
        try:
            currentYear = int(input("Enter Current Year: "))
            year = int(input("Enter age or year of age: "))
            ageCaluclation(currentYear, year)
            Exit = True
        except Exception as e:
            print("Please put numerical value\n"
              "Try Again...")

def hundred_year(year_of_birth):
    hundred = year_of_birth + 100
    return hundred

def yearOfBirth(current_year, year_or_age):
    year_of_birth = current_year - year_or_age
    return year_of_birth

def birthYearInput(current_year, year_or_age):
    print("You Entered year of Birth")
    print(f"You current age is {yearOfBirth(current_year, year_or_age)}")
    hundred = year_or_age + 100
    if hundred < current_year:
        print(f"You already turned 100 on {hundred}")
    elif hundred == current_year:
        print(f"This is your hundredth year {hundred} 👏🎉")
    else:
        print(f"You will turn 100 on year {hundred}")

def ageCaluclation(current_year, year_or_age):
    if current_year < 1900:
        print("Please Enter Current Year Greater than 1900")
        start()
    else:
        if year_or_age >= 0 and year_or_age <= 99:
            hundred = hundred_year(yearOfBirth(current_year, year_or_age))
            print(f"You will turn 100 on year {hundred}")
            year_of_birth = yearOfBirth(current_year, year_or_age)
            year_or_age = year_of_birth
            print(f"You Birth Year is {year_of_birth}")

        elif year_or_age < 1900 and year_or_age >= 100:
            print("You Seem to be oldest person alive")
            year_of_birth = yearOfBirth(current_year, year_or_age)
            year_or_age = year_of_birth
            print(f"You Birth Year is {year_of_birth}")

        elif year_or_age >= 1900 and year_or_age <= current_year:
            birthYearInput(current_year, year_or_age)
            pass
        else:
            print("May be you are not human, seems like you are form another planet")
            exit()
        while True:
            print("Do you want to know your age on particular year\n"
                  "Press Y for Yes and N For No")
            choice = input()

            if choice == "n" or choice == "N":
                print("Thanks for using this program")
                exit()
            elif choice =="y" or choice == "Y":
                Exit = False
                while Exit is not True:
                    try:
                        year = int(input("Enter year you want to know your age on: "))
                        ageOnParticularYear = year - year_or_age
                        print(f"Your age on this year is {ageOnParticularYear}")
                        print("Thanks for using our program")
                        exit()
                    except Exception as e:
                        print("Please Numerical value\n"
                              "Try Again...")
            else:
                print("Wrong Input\n"
                      "Try Again")
                continue
start()

