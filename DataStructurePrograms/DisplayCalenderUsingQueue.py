
from DataStructurePrograms.TestFunctional import Test_Stack
from DataStructurePrograms.Test import TestFunctional

q1 = Test_Stack()
q2 = Test_Stack()


class Calender_Queue:
    while True:
        try:

            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # days lies in a month
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar",
                      "November", "December"]                           # names of a month
            weeks = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]  # weeks names

            print("enter month number...\n")
            month = int(input())
            while month < 1 or month > 12:
                print("enter valid month number...\n")
                month = int(input())
                break

            print("enter the year...\n")
            year = int(input())
            while year < 999 or year > 9999:
                print("enter valid year number...\n")
                year = int(input())
                break
            if month == 2 and TestFunctional.leapyear(year):  # checking leap year
                days[month - 1] = 29                          # true,days month becomes 29
            day = TestFunctional.day_of_week(1, month, year)  # getting day of given month starting

            for i in range(len(weeks)):
                q1.en_Queue(weeks[i])
            print()

            val = days[month - 1]      # assigning no of days into variable

            for i in range(1, val+1):  # days of a week in reversed order
                q2.en_Queue(i)         # pushed into a stack
            print()

            print("      ", months[month - 1], " - ", year)  # printing month and year

            for i in range(1, 8):                            # to print the days of a weeks
                print(q1.de_queue(), end=" ")
            print()

            for i in range(day * 4):                  # for spaces between a dates
                print(end=" ")                    # end with spaces

            for i in range(1, val + 1):
                if i <= 5:      # less than and equal to 5
                    print("", q2.de_queue(), " ", end="")  # printing between 1-5
                if 5 < i < 10:
                    print("", q2.de_queue(), " ", end="")  # printing above 5 lees than 10
                if i > 9:
                    print("", q2.de_queue(), "", end="")   # printing double digits

                if (i + day) % 7 == 0:                # after 7 column print in next line
                    print()
            break
        except ValueError:
            print("enter valid inputs.....\n")
            continue
        except RuntimeError:
            print("oops something went wrong....\n")
            continue
