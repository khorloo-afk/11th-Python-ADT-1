# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
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
    global TopOfStack
    if IsEmpty():
        return "-1"
        
def IsEmpty():
    return TopOfStack < 0
    item = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return item

# Exercise 4
def Peek():
    if TopOfStack < 0:
        return "-1"
    return stack[TopOfStack]


def Size():
    if TopOfStack < 0:
        return 0
    return TopOfStack + 1


# Exercise 5
def ReverseWord(Word):
    stack = []
    TopOfStack = -1
    for letter in Word:
        stack.append(letter)
        TopOfStack += 1
    reversed_word = ""
    
    while TopOfStack >= 0:
        letter = stack.pop()
        reversed_word += letter
        TopOfStack -= 1
    return reversed_word

