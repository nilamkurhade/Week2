from DataStructurePrograms.stack import Stack


class BalancedParantheses:
    s = Stack()        # Object of the class
    exp = input('Please enter the expression: ')

    for c in exp:
        if c == '(':    # if we receive the opening parantheses we push into stack
            s.push(1)
        elif c == ')':
            if s.isEmpty():
                is_balanced = False
                break
            s.pop()     # once we receive the closing parantheses we pop from stack
    else:
        if s.isEmpty():
            is_balanced = True
        else:
            is_balanced = False

    if is_balanced:
        print('Expression is correctly parenthesized.')
    else:
        print('Expression is not correctly parenthesized.')


if __name__ == "__main__":
    obj = BalancedParantheses()
