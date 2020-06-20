import math

# Python program to  
# demonstrate stack implementation 
# using list 
  
from graphics.py import *   
stack = [] 
  
# append() function to push 
# element in the stack

def Stack(s):
    stack.append(s)
    
    
#stack.append('a') 
#stack.append('b') 
#stack.append('c') 
# pop() fucntion to pop 
# element from stack in  
# LIFO order
for i in range(10):
    Stack(i)

print('Initial stack') 
print(stack)

angle=math.radians(30)
print(angle)

#Stack(9)
#Stack(99)
#Stack(999)
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
print(stack) 
  
# uncommenting print(stack.pop())   
# will cause an IndexError  
# as the stack is now empty 
