# ******************************************************************#
#  Purpose: 2.Implementing Ordered Linked List
#  *
#  *  @author  KIRAN KUMAR S
#  *  @version 3.7
#  *  @since   12-01-2019
#
# */

import re

from DataStructurePrograms.util import Test_LinkedList

l1 = Test_LinkedList()


class LinkedList_Ordered:
    try:
        new_file = open("Numbers.txt", "r+")  # reading from a file with extension .txt
        number = new_file.read()              # reading file content
        value = number.split()                # split by space

        new_file.close()                       # closing a file
        my_list = []
        results = False
        for i in value:
            my_list.append(int(i))             # append value taken from file into a list

        for i in my_list:
            l1.add(int(i))                     # list to node of linked list

        print("size of an Ordered list as follows:", l1.getSize())  # linked list size

        print("elements of ordered list are as follows: \n")
        l1.PrintNode()
        print()

        print("enter elements to search ...\n")
        word = int(input())
        res = l1.searchNode(word)          # searching a  word in a list
        print("searching element success:", res)
        if res is True:

            results = l1.removeNode(word)                      # if found remove that word
            print(word, ",removing element success or not :", results)  # printing removing element

        else:
            l1.add(word)                  # if word not found , add that element to list
            print()
            print(word, ", Its Added To Linked List \n")

        print()
        print("updating  a list..\n")

        num1 = l1.PrintNode()             # print modified list
        print()
        print(num1)

        new_file = open("Numbers.txt", "r+")
        new_file.truncate(0)                  # truncate the file
        new_file.close()

        new_file = open("Numbers.txt", "r+")
        #print(my_list.append(num1))

        for num2 in num1:                  # print the list contents
            num3 = str(num2) + " "           # with white spaces
            new_file.write(num3)             # rewrite to a file
        new_file.close()                      # close the file

        l1.PrintNode()
        my_list.clear()

    except RuntimeError:
        print("=======oops something went wrong.....====\n")
