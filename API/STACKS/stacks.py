#creating a stack
def create_stack():
    stack=[]
    return stack

#creating an empty stack
def create_empty(stack):
    return len(stack)    

#adding an item toa stack
def push(stack,item):    
    stack.append(item)
    print("pushed item: "+ item)

#Removing an element
def pop(stack):
    if (create_empty(stack)):
        return "stack is empty"
    return stack.pop()        


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))