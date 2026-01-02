#Stack implementation

class ArrayStack:
    def __init__(self,n=1000):
        self.stack=[None]*n
        self.capacity=n
        self.top=-1
    def push(self,x):
        if self.push==self.capacity-1:
            raise OverflowError("stack overflow")
        self.top+=1
        self.stack[self.top]=x
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        val=self.stack[self.top]
        self.top-=1
        return val
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]
    def is_empty(self):
        return self.top==-1
    