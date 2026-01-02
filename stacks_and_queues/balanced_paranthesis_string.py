

def is_balanced(s):
    n=len(s)
    stack=[]
    Bracket=["(",'{','[']
    for i in range(n):
        if s[i] in Bracket:
            stack.append(s[i])

        
        else:
            if not stack:
                return False
            top=stack.pop()
            
            if s[i] == ')' and top != '(':
                return False
            if s[i] == '}' and top != '{':
                return False
            if s[i] == ']' and top != '[':
                return False
            
    return len(stack)==0

print(is_balanced("(){}[]"))      # True
print(is_balanced("({[]})"))      # True
print(is_balanced("(]"))          # False
print(is_balanced("({)}"))        # False
print(is_balanced("((("))         # False
print(is_balanced(")("))          # False


#Shorter
def Balancing(s):
    open="([{"
    close=")]}"
    stack=[]
    for ch in s:
        if ch in open:
            stack.append(ch)
        else:
            if not stack or open.index(stack.pop()) !=close.index(ch):
                return False
    return not stack

    