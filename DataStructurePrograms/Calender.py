# First import the calendar module

#import calendar

# ask of month and year
#yy = int(input("Enter year: "))
#mm = int(input("Enter month: "))
# display the calendar
#print(calendar.month(yy, mm))

from DataStructurePrograms.util import Test_LinkedList


l1 = Test_LinkedList()


class Display_Calender:
    while True:
        try:
            print("enter month....")
            month = int(input())     # taking month as input
            while month <= 0 or month > 12:  # validating
                print("invalid entry....\n")
                month = int(input())  # taking month as input
                break
            print("enter year....\n")
            year = int(input())       # taking years as user input
            while year <= 999 or year > 9999:  # validating
                print("invalid entry....\n")
                month = int(input())   # taking years as user input
                break
            l1.displayCalOfMonth(month, year)  # calling method
            break
        except ValueError:  # handling exceptions
            print("==oops something went wrong,please give valid inputs...\n")
            continue
        except RuntimeError:
            print("oops something went wrong....\n")
            continue
