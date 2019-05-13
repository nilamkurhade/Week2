from DataStructurePrograms.util import Test_LinkedList

l1 = Test_LinkedList()  # reference of a Test_linkedList class


class Binary_Search_Tree:
    while True:
        try:
            print("enter a number to implement binary search tree....\n")
            num = int(input())
            while num < 1:                         # validation checking
                print("enter a valid  number to implement binary search tree....\n")
                num = int(input())
                break
            var1 = l1.binary_search_tree(num)       # n! factorial
            var2 = l1.binary_search_tree(num * 2)   # (num * 2)!
            var3 = l1.binary_search_tree(num+1)     # (num+1)!
            result = var3 * var1                    # (num+1)! * (n)!
            divisor = var2 // result
            print(divisor)
            break
        except ValueError:
            print("please give valid inputs.....\n")
            continue
        except RuntimeError:
            print("oops something went wrong.....\n")
            continue
