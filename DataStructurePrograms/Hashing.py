class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


def put(self, key, data):
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
    else:
        if self.slots[hashvalue] == key:
            self.data[hashvalue] = data  #replace
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != None and \
                self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

    if self.slots[nextslot] == None:
        self.slots[nextslot]=key
        self.data[nextslot]=data
    else:
        self.data[nextslot] = data  #replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size


def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and  \
        not found and not stop:
        if self.slots[position] == key:
            found = True
            data = self.data[position]
        else:
            position=self.rehash(position,len(self.slots))
        if position == startslot:
            stop = True
    return data


def __getitem__(self,key):
    return self.get(key)


def __setitem__(self, key, data):
    self.put(key, data)


hash_obj = HashTable()


def main():
    hash_obj.slots = [10, 50, 20, 30, 40, 70, 90, 60, 80, 100]
    hash_obj.data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    print(hash_obj)
    hash_obj[10] = "a"
    hash_obj.put(hash_obj.slots, hash_obj.data)
    print(hash_obj)
    print(hash_obj[20])


if __name__ == "__main__":
    hash_obj = HashTable()
