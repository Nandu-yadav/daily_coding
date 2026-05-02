

def precedence(op):
    if op=='+' or op =='-':
        return 1
    if op =='*' or op =='/':
        return 2
    if op =='^':
        return 3
    return 0

#INFIX TO PREFIX

def infix_to_prefix(exp):
    # reverse expression
    exp=exp[::-1]

    # SWAP Brackets
    exp=list(exp)
    for ch in exp:
        if ch=='(':
            ch =')'
        elif ch==')':
            ch ='('

    exp = ''.join(exp)
    
    stack=[]
    postfix=[]
    #step 3 : Infix to postfix
    for ch in exp:
        if ch.isalnum():
            postfix.append(ch)
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()
        else:    #operator
            while stack and precedence(ch) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(ch)
    #step 4 : pop remaining operators
    while stack:
            postfix.append(stack.pop())
    # 5. reverse postfix --> prefix
    postfix.reverse()
    return  ''.join(postfix)

print(infix_to_prefix("A*(B+C)"))


#infix to postfix


def infix_to_postfix(exp):
    stack=[]
    postfix=[]

    for ch in exp:
        if ch.isalnum():  # alphabet or number
            postfix.append(ch)
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1] !="(":
                postfix,append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(ch) <=precedence(stack[-1]):
                postfix.append(ch)
    while stack:
        postfix.append(stacl.pop())
    return ''.join(postfix)
    

