# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
TopOfStack = -1

def IsEmpty():
    return TopOfStack == -1

def IsFull():
  return TopOfStack == 9

# Exercise 2
def Push(Item):
    if IsFull():
        return False

    global TopOfStack
    TopOfStack += 1

    Stack[TopOfStack] = Item
    return True
# Exercise 3
def Pop():
    # Write your code here
    pass


# Exercise 4
def Peek():
    # Write your code here
    pass


def Size():
    # Write your code here
    pass


# Exercise 5
def ReverseWord(Word):
    stack = []
    TopOfStack = -1
    for char in Word:
        stack.append(char)
        TopOfStack += 1
    new_string = ""
    while TopOfStack != -1:
        new_string += stack.pop()
        TopOfStack -= 1
    return new_string

