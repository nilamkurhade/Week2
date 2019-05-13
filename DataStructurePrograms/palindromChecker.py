from DataStructurePrograms.dequeue import Deque


dq = Deque()
text = input('Please enter the string: ')

for character in text:
    dq.addRear(character)

reversed_text = ''
while not dq.isEmpty():
    reversed_text = reversed_text + dq.removeRear()

if text == reversed_text:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
