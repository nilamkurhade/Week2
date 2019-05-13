
"""=============== Utility DataStructure========"""
from DataStructurePrograms.Test import TestFunctional
from DataStructurePrograms.Node import Node


class Test_LinkedList:
    def __init__(self, head=None):     # constructor which accepts self,head parameter
        self.head = head               # self.head = head
        self.size = 0                  # size = 0 initially

    def addNode(self, data):            # instance method accepts data
        newNode = Node(data, self.head)  # adding data into the list
        self.head = newNode              # node added to the list
        self.size += 1                   # increment size by 1
        return True                      # return true after adding

    def getSize(self):                    # instance method accepts none
        return self.size                 # returns size of a linked list

    def PrintNode(self):           # instance method accepts none
        my_list = []               # initializing list
        curr = self.head           # assign head to curr
        while curr:
            print(curr.data, end=" => ")  # printing the data of LL
            my_list.append(curr.data)     # appending to the list
            curr = curr.nextNode          # traversing to next node of LL
        return my_list                # returns the list

    def findNodes(self, values):   # instance method accepts none
        curr = self.head            # assign head to curr
        result = None              # assign result to None
        while curr:
            if curr.data == values:   # checking node data with given values..
                result = True          # is true means break
                break
            else:
                result = False            # else,visit rest of a node
            curr = curr.getNextNode()
        if result:
            print("Element Found :", values)  # printing  element found or not
            return True
        else:
            print("Element Not Found:")
        return False

    def removeNode(self, values):   # instance method accepts none
        prev = None
        curr = self.head
        if curr.data == values:        # checking node data with given values..
            self.head = curr.nextNode  # data find in head only assign node.next
            curr.nextNode = self.head
            self.size -= 1             # decrement size by 1
            return True                # element removed means returns true
        else:
            while curr:
                if curr.data == values:    # if element not found in head,traverse upto end of node
                    prev.nextNode = curr.nextNode  # current reference is giving to the previous
                    curr.nextNode = None       # removing the current node
                    return True          # values is get means
                    break                  # break
                else:
                    prev = curr           # traverse up to end of the Linked list
                    curr = curr.nextNode
            self.size -= 1          # deleting node by decrement size by 1
        return False                # element not found return false

    def isEmpty(self):              # instance method accepts none
        if self.size == 0:          # size of linked == 0 ,then linked list is empty
            print("the list is empty,use add method to add element \n")
        else:                       # else prints not empty
            print("the list is not empty \n")

    def index(self, values):             # instance method accepts none,prints given values position
        curr = self.head
        res = True
        pos = 0
        for i in range(self.size):
            if curr.getData() == values:
                print("==========")
                pos = i
                res = True
                break
            else:
                res = False
            curr = curr.getNextNode()
        if res:
            print("given values:", values, ",found at position:", pos)
        else:
            print("values not found,give proper values \n")

    def insertAtPos(self, new_data, pos):  # instance method accepts data , pos as input
        temp = self.head
        prev = None
        new_Node = Node(new_data)
        if pos == 0:                       # given position == 0 means data adds at a first node only
            return Node(new_data, self.head)
        if pos > self.size:                # if pos is greater than size means out os range u can append at end
            print("out of range,please wait for append function to write...\n")
        if pos > 0 or pos < self.size:  # pos > 0 and < size
            for i in range(0, self.size):
                if i == pos:              # add at given position
                    self.size += 1        # and increment size by 1
                    new_Node.nextNode = temp
                    prev.nextNode = new_Node
                    break
                else:
                    prev = temp
                    temp = temp.nextNode

    """=============== Utility DataStructure For Ordered List========"""

    def add(self, values):                 # instance method accepts input values
        current = self.head
        previous = None
        while current is not None:
            if current.data > values:       # if values is greater than current data break
                break
            previous = current
            current = current.nextNode
        temp = Node(values)
        if previous is None:
            temp.nextNode = self.head
            self.head = temp
        else:
            temp.nextNode = current
            previous.nextNode = temp
        self.size = self.size + 1          # increment size by 1

    def getSize(self):                     # instance method accepts none
        return self.size                   # return size of a list

    def PrintNodeOrdered(self):            # instance method accepts none
        curr = self.head
        while curr:
            print(curr.data, end=" => ")   # prints the list data
            curr = curr.getNextNode()

    def searchNode(self, values):          # instance method accepts input as values
        current = self.head
        result = True
        while current is not None:
            if current.data == values:     # checks for given values is present in a list or not
                result = True
                break
            if current.data > values:
                result = False
            current = current.nextNode       # checks for first node ,else traverse up to last node of a list
        if result:
            print("Element Found: ", values)
            return True                      # element found means return True
        else:
            print("Element Not Found:", values)
        return False                         # not found returns false

    """=====stack implementation using array for balanced parentheses======="""

    st_list = []                        # initialize list
    capacity = -1                       # initialize capacity to -1
    top = -1                            # initialize top  to -1

    def push(self, val):                # instance method for push elements into stack accepts data as input
        if self.top == self.capacity:   # if stack top pointing to -1
            self.top += 1               # add element to the stack,increment top by 1
            self.st_list.append(val)    # add element to the stack
            self.capacity += 1          # increment stack capacity by 1
        return self.st_list             # return list

    def pop(self):                      # instance method for pop stack element
        if self.top != -1:              # if top not points to -1,means elements in stack
            self.top -= 1               # decrement top by 1
            self.capacity -= 1          # and capacity by 1
            for i in self.st_list:      # take elements from a list
                if i == '(' or i == '{' or i == '[':  # check if it contains (,{,[ characters
                    self.st_list.remove(i)            # remove that characters from list
                    break                             # break
        return self.st_list                           # return the list

    def st_size(self):                  # instance method for print size of an stack
        # print("size of an stack is :", self.capacity)  # printing
        x = self.capacity
        return x

    def st_isEmpty(self):               # instance method to check stack empty or not
        if self.capacity == 0:          # if capacity is == 0 stack empty,otherwise not empty
            print("stack is empty \n")
        else:
            print("stack is not empty \n")

    def peek(self):                      # instance method prints recently accepted element in a stack
        # print("peek element in a stack is :", self.st_list[len(self.st_list) - 1])
        x = self.st_list[len(self.st_list) - 1]
        return x

    """======queue implementation using array for banking process===="""
    front = 0                         # initialize variable to 0
    rear = 0                          # initialize variable to 0
    size = 0                          # initialize variable to 0
    my_list1 = []                     # initialize list

    def queue_push(self, amount):      # instance method which accepts data int as inputs
        if self.rear == self.front:    # rear and front are equal means stack is empty
            self.rear += 1             # increment by 1
            self.size += 1             # increment by 1
        self.my_list1.append(amount)   # appending data into a list
        for i in self.my_list1:        # accessing elements from aa list
            print(i, end=" => ")       # printing the data
        return self.my_list1           # returning the list

    def queue_pop(self):               # instance method which accepts none
        if self.size != 0:             # elements are in queue
            self.rear -= 1             # decrement by 1
            self.size -= 1             # decrement by 1
        for i in range(len(self.my_list1)):  # accessing element from a list
            self.my_list1.remove(self.my_list1[i])  # removes element from a list
            break
        for i in self.my_list1:
            print(i, end=" => ")
        print()
        return self.my_list1

    """======displaying calender taking input month and the year===="""

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of days
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobar",
             "November", "December"]                     # list of month names

    def displayCalOfMonth(self, month, year):            # instance method which accepts month and years as input
        if month == 2 and TestFunctional.leapyear(year):  # checking for leap year
            self.days[month - 1] = 29                     # if yes,assign 29 days for a month
        day = TestFunctional.day_of_week(1, month, year)  # to get day of particular date
        print(day)
        print("        ", self.month[month - 1], "   ", year)
        print("Sun Mon Tue Wed Thu Fri Sat")
        val = self.days[month - 1]                         # to check how many days are for particular month
        for i in range(day * 4):                      # for particular month how many dates are come for particular day
            print(end=" ")                                 # end with spaces
        for i in range(1, val + 1):
            if i <= 5:                                     # printing 5 or less than 5
                print("", i, " ", end="")
            if 5 < i < 10:                                 # printing greater than 5 and less than 10
                print("", i, " ", end="")
            if i > 9:                                     # printing double digits numbers
                print("", i, "", end="")

            if (i + day) % 7 == 0:                         # after 7 column print in next line
                print()

    """======displaying prime numbers using 2D Array=========="""

    def prime_2d_array(self):
        number = 500
        prime_list = TestFunctional.prime_number1(number)
        row = 10
        column = 25
        limit = 100                 # giving limits to print as per question mentioned
        # creating Two-Dimensional Array....
        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0
        for i in range(row):
            for j in range(column):
                if k < len(prime_list):
                    if prime_list[k] <= limit:
                        two_d_array[i][j] = prime_list[k]       # adding the element to the 2D array
                        k += 1
            limit += 100                            # increment limit by 100 for each iteration

        for i in range(row):
            for j in range(column):
                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")      # printing 2D Array for Prime Number
            print()

    """ ====================displaying which are not prime anagram========= """

    def anagram_prime_2D_array(self):  # instance method accepts none
        num = 300
        prime_list = TestFunctional.prime_number(num)
        anagram_list = TestFunctional.anagram_prime(prime_list)
        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]  # creating
        k = 0
        index = 0
        for i in prime_list:
            if anagram_list.__contains__(i) is not True:
                not_anagram.append(i)

        for i in range(row):
            for j in range(column):
                if k < len(anagram_list):
                    two_d_array[i][j] = anagram_list[k]    # adding anagram values into the array
                    k += 1
                if k >= len(anagram_list) and index < len(not_anagram):
                    two_d_array[i][j] = not_anagram[index]  # adding not anagram into the array
                    k += 1
                    index += 1

        for i in range(row):                            # displaying prime and not prime anagram
            for j in range(column):
                if two_d_array[i][j] != 0:              # checks conditions of array not equals to 0
                    print(two_d_array[i][j], end=" ")  # printing both prime and not prime anagrams
            print()

    """============================= Binary_Search_Tree================="""

    @staticmethod
    def binary_search_tree(number):  # static method accepts int as inputs
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i           # fact * i
        return fact                  # return factorials

    """===========================balanced parentheses==============="""

    def balanced_parentheses1(self, string):
        """
        This method is used to check whether expression is balanced or not.
        :param string: this is the expression which will be given by user
        :return: nothing
        """

        for i in string:

            if i == '(' or i == '[' or i == '{':
                t.push(i)                   # adding element into stack

            if ((t.peek() == '(' and i == ')') or (t.peek() == '[' and i == ']') or
                    (t.peek() == '{' and i == '}')) and t.st_size() > 0:
                t.pop()
                continue

        if t.st_size() == 0:
            print("Balanced Parenthesis ")  # after push and pop operation if stack size
        else:                               # is zero then balanced otherwise unbalanced
            print("not Balanced parentheses ")


t = Test_LinkedList()  # reference of a Test_linkedList class
