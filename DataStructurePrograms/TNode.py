class TNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNext(self):
        return self.next

    def setNext(self, val):
        self.next = val