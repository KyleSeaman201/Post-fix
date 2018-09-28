#Uses the Stack class to evaluate a postfix expression.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__
                          

class Stack:
    def __init__(self):
        self.top = None

    def push(self,item):
        new_node= Node(item)
        new_node.next=self.top
        self.top= new_node
     
    def pop(self):
        temp= self.top.value
        self.top= self.top.next
        return temp

def postfix(expression):
    stack=Stack()
    expression= expression.split()
    for i in expression:
        if i.isdigit():
            stack.push(i)
        else:
            temp1= float(stack.pop())
            temp2= float(stack.pop())
            if i=='+':
                stack.push(temp2 + temp1)
            if i=='-':
                stack.push(temp2 - temp1)
            if i=='/':
                stack.push(temp2 / temp1)
            if i=='*':
                stack.push(temp2 * temp1)
            if i=='^':
                stack.push(temp2 ** temp1)


    return stack.pop()

#test cases
'''
print(postfix("4 7 6 * + 10 -"))
print(postfix("2 4 ^ 3 + 2 5 / -"))
print(postfix("16 42 3 - - 7 + 5 *"))
print(postfix("10 5 / 2 +"))