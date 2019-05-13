import re
from DataStructurePrograms.util import Test_LinkedList

l1 = Test_LinkedList()


class LinkedList_Unordered:
    try:
        newfile = open("readfile.txt", "r+") # open the file to perform linked list operations
        readfile = newfile.read() # reading file content
        regex = re.sub('[^A-Za-z0-9]+', ' ', readfile)  # accepting alpha-numeric characters(words)
        my_list = []
        my_list = regex.lower().split() # converting to lowercase and split by space store into the list
        newfile.close() # closing the file

        results = True # initializing result variable
        for i in my_list: # iterate element and storing into a singly linked list Node
            l1.addNode(i) # adding the words into a list
        print("total size of an linked list are:", l1.getSize()) # size of a list
        print("***********************************************")
        print("linked list elements are as follows:\n")
        l1.PrintNode() # printing the node values
        print()
        print("***********************************************")
        print("enter elements to search ...\n")
        word = str(input())
        res = l1.findNodes(word) # searching a word in a list
        if res is True:  # if it return true word found ,else not found
            results = l1.removeNode(word)  # if found remove that word
            if results is True:  # checking successfully removed or not
                newfile = open("readfile.txt", "r+")  # open file
                newfile.truncate(0)  # truncating a file to overwrite modified values
                newfile.close()  # closing a file
                newfile = open("readfile.txt", "r+")  # open file to write
                my_list.remove(word)  # remove from list
                for word in my_list:  # traversing list
                    word2 = word + " "  # concating word white spaces
                    newfile.write(word2)  # then writing into  file
                newfile.close()  # after writing close the file
                l1.PrintNode()  # print the list after modified
        else:
            l1.addNode(word)  # if word not found , add that element to list
            print("adding into a list..\n")
            newfile = open("readfile.txt", "r+")
            my_list.append(word)  # appending word into a file
            for word in my_list:  # print the list contents
                word2 = word + " "  # with white spaces
                newfile.write(word2)  # rewrite to a file
            newfile.close()  # close the file
        l1.PrintNode()
        my_list.clear()

    except RuntimeError:  # exception handling
        print("oops something went wrong,please give valid inputs....\n")
