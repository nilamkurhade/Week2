from DataStructurePrograms.TestFunctional import Test_Stack
from DataStructurePrograms.Test import TestFunctional

s1 = Test_Stack()  # reference of Test_Stack class
s2 = Test_Stack()  # reference of Test_Stack class


class Calender_Stack:
    while True:
        try:

            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # days of a month
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar",
                      "November", "December"]                          # month names
            weeks = ["Sun",  "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]  # weeks names

            print("enter month number...\n")
            month = int(input())
            while month < 1 or month > 12:
                print("enter valid month number...\n")
                month = int(input())
                break                                       # taking input from a user

            print("enter year number...\n")
            year = int(input())
            while month < 1 or month > 12:
                print("enter valid year number...\n")
                year = int(input())
                break                                       # taking input from a user

            if month == 2 and TestFunctional.leapyear(year):  # checking for a leap year
                days[month-1] = 29                            # yes , printing 29 days for month
            val = days[month - 1]                             # store it in a variable
            day = TestFunctional.day_of_week(1, month, year)  # to get day of particular date
            print("\n")
            weeks.reverse()  # used for a stack

            for i in range(len(weeks)):  # accepts days of a weeks
                s1.stack_push(weeks[i])  # push into the stack
            print()
            for i in range(val, 0, -1):  # days of a week in reversed order
                s2.stack_push(i)         # pushed into a stack

            print()
            print("      ", months[month - 1], " - ", year)      # printing month and year

            for i in range(1, 8):                                    # to print the days of a weeks range(1 to 8)
                print(s1.stack_pop(), end=" ")                       # pop the element from a stack
            print()

            for i in range(day * 4):                       # for spaces between a dates
                print(end=" ")                             # end with spaces
            for i in range(1, val + 1):                    # range(1,date+1)
                if i <= 5:                                 # printing the single digit dates
                    print("", s2.stack_pop(), " ", end="")
                if 5 < i < 10:                             # printing range above 5 and below 10
                    print("", s2.stack_pop(), " ", end="")
                if i > 9:                                  # printing double digits
                    print("", s2.stack_pop(), "", end="")

                if (i + day) % 7 == 0:                     # after 7 column print in next line
                    print()
            break
        except ValueError:                                # handling the exceptions
            print("enter valid input.....\n")
            continue
        except RuntimeError:
            print("oops something went wrong...\n")
            continue