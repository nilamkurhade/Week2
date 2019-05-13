


"""======Utility data structure solving using stack and queue======"""

from DataStructurePrograms.TNode import TNode


class Test_Stack:
    head = None
    size = 0
    top = -1

    def __init__(self):
        """
        Constructor of this class
        """
        self.top = None
        self.size = 0
        self.head = None
        self.front = None
        self.rear = None
        pass

    """=====stack functions==========="""

    def stack_push(self, data):  # instance method accepts data as input
        node = TNode(data)  # assigning Node(data) into the node
        self.size += 1  # increment size by 1
        if self.top is None:  # where stack is empty add data to the first node itself
            self.top = node
        else:  # adding data to the stack
            node.next = self.top  # else store data into a next node
            self.top = node
        print(node.data, end=" ")  # printing the node data

    def stack_pop(self):  # instance method accepts none
        if self.top is None:  # if top is None,stack is empty
            print("stack is empty...")
        # while self.top is not None:
        temp = self.top  # using temp traverse to next node
        self.top = self.top.next  # traverse from head to next node
        self.size -= 1  # decrement size by 1
        # print(temp.data, end=" ")
        return temp.data  # return temp.data

    def stack_dispaly(self):  # instance method accepts none
        my_list = []
        temp = self.top  # temp pointing to the first node
        while temp is not None:  # loop up to temp is None
            # print("reverse order...\n")
            print(temp.data, "=>", end=" ")  # printing temp data
            my_list.append(temp.data)  # append temp.data into a my_list
            temp = temp.next  # traverse to next node
        return my_list  # return my_list

    def stack_getSize(self):  # instance method accepts none
        return self.size  # return size

    """========================queue functions==============="""

    def en_Queue(self, data):  # instance method accepts data as input
        node = TNode(data)  # assigning Node(data) into the node
        if self.rear is None:  # if rear is none
            self.front = node  # assign node to front,rear
            self.rear = node
        else:
            self.rear.next = node  # traverse to rear.next
            self.rear = self.rear.next  # assign rear = rear.next
        self.size = self.size + 1  # increment size by 1
        print(node.data, end="=>")  # printing node.data

    def de_queue(self):  # instance method accepts none

        if self.front is not None:  # check condition front is not none
            temp = self.front  # temp holds the data of a front
            self.front = self.front.next  # jumps to next node
            # print(temp.data)
            return temp.data  # returns the data
        else:
            if self.rear is not None:  # else rear is not none
                self.rear = None  # assign rear to none
                print("queue is empty...\n")

    def queue_display(self):  # instance method accepts none
        temp = self.front
        while temp is not None:  # traverse up to queue is None
            print(temp.data, end="=>")  # printing the data
            temp = temp.next  # traverse up to last node

    """========================Double-Ended Queue functions==============="""

    def add_front(self, data):
        node = TNode(data)
        if self.front is None and self.rear is None:
            self.front = node
        else:
            node.next = self.front
            self.front = node
        print(node.data, end="=>")

    def add_rear(self, data):
        node = TNode(data)
        if self.front is None and self.rear is None:
            self.rear = node
        else:
            node.next = self.rear
            self.rear = node
        print(node.data, end="=>")

    def remove_front(self):
        if self.front.next is None:
            temp = self.front
            self.front = None
            return temp.data
        temp = self.front
        self.front = self.front.next
        # print(temp.data, end="=>")
        return temp.data

    def remove_rear(self):
        traverse = self.front
        if self.rear == self.front:   # single element in a queue
            self.rear = None
            self.front = None
            print(traverse.data, end="=>")
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next

        rear_value = self.rear
        self.rear = traverse
        traverse.next = None
        # print(traverse.data, end="=>")
        return traverse.data

    def de_size(self):
        size = 1
        traverse = self.front
        if self.front is None:
            return 0
        while traverse.next is not None:
            traverse = traverse.next
            size += 1
        # print(size)
        return size

    def de_is_Empty(self):
        if self.front is None:
            return True
        else:
            return False


t = Test_Stack()

