def isValid(s):
    #Our stack is an array data type that we will treat as a stack
    stack = []
    #Dictionary to detect closing brackets
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        #If closing bracket found
        if char in mapping:
            #If stack is not empty, remove last element
            top_element = stack.pop() if stack else '#' #dummy symbol
            #Check if closing bracket matches with most recent opening bracket.
            if mapping[char] != top_element:
                return False
        #If opening bracket, throw it on the stack.
        else:
            stack.append(char)
    #If stack is empty, then the scenario is valid.
    return not stack #Return False if stuff left in stack
                     #Retrun True if stack is empty.

s = "()"
print(isValid(s))
s = "()[]{}"
print(isValid(s))
s = "(]"
print(isValid(s))
s = "([)]"
print(isValid(s))
s = "{[]}"
print(isValid(s))