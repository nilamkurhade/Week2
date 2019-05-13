from DataStructurePrograms.TestFunctional import Test_Stack
from DataStructurePrograms.Test import TestFunctional

t1 = Test_Stack()  # reference of a Test_Stack


class Prime_Anagram_Stack:
    while True:
        try:
            print("enter range of a number to find prime numbers....\n")
            number = int(input())  # taking user inputs
            while number <= 32:  # validating user inputs
                print("enter positive and greater than 32 to check prime anagram...\n ")
                number = int(input())
                break
            prime_list = TestFunctional.prime_number(number)  # prime number() returns the list
            anagram_list = TestFunctional.anagram_prime(prime_list) # anagram_prime returns the list

            for i in anagram_list:
                t1.stack_push(int(i))  # pushing the elements from list to stack
            print()

            print("stack values are as follows: \n")
            t1.stack_dispaly()      # printing stack elements
            print()
            break
        except ValueError:  # handling the exceptions
            print("enter valid input........\n")
            continue
        except RuntimeError:  # handling the exceptions
            print("enter valid input........\n")
            continue
