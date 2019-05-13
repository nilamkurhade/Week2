from DataStructurePrograms.TestFunctional import Test_Stack
from DataStructurePrograms.Test import TestFunctional

q1 = Test_Stack()   # reference of a Test_Stack class


class Prime_Anagram_Queue:
    while True:
        try:

            print("enter the number range to check anagram prime...\n ")
            num = int(input())              # taking user input

            while num <= 31: # checking validation
                print("enter the number range greater than 32 to check anagram prime...\n ")
                num = int(input())  # taking user input
                break
            prime_list = TestFunctional.prime_number(num)  # storing result of prime numbers
            anagram_list = TestFunctional.anagram_prime(prime_list)  # storing result of anagram_prime numbers

            print("Pushing elements to the Queue.....\n")
            for i in anagram_list:    # pushing elements of anagram_list into a queue
                q1.en_Queue(i)
            print()
            print("Displaying the Queue elements.....\n ")
            q1.queue_display()      # printing queue elements
            break
        except ValueError:          # exception handling
            print("enter valid input.....\n")
            continue
        except RuntimeError:
            print("oops something went wrong.........\n")
            continue