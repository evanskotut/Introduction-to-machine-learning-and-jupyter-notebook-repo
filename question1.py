# '1). Write a Python program to check whether a string is a palindrome or not using a stack.

class Stack:
    def __init__(self):
        self.items = []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
 
    def is_empty(self):
        return len(self.items) == 0
 
# Function to check palindrome using a stack
def is_palindrome(s):
    stack = Stack()
 
    # Push each character onto the stack
    for char in s:
        stack.push(char)
 
    # Pop characters from the stack and compare with the string
    for char in s:
        if char != stack.pop():
            return False
 
    return True
 
# Example usage
input_string = "Radar"
result = is_palindrome(input_string.lower())  # Convert to lowercase for case-insensitivity
if result:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")