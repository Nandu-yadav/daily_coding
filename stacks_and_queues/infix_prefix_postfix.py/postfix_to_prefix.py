

def postfix_to_prefix(exp):
    stack=[]

    for ch in exp:

        if ch.isalnum():
            stack.append(ch)
        
        else:
            op2=stack.pop()
            op1=stack.pop()
            new_expr=ch+op1+op2
            stack.append(new_expr)
    return stack[-1]

#prefix to postfix

def prefix_to_postfix(exp):
    stack=[]
    for ch in reversed(exp):
        #oprand
        if ch.isalnum():
            stack.append(ch)

        else:
            op1=stack.pop()
            op2=stack.pop()
            new_expr=op1+op2+ch
            stack.append(new_expr)
    return stack[-1]
print(prefix_to_postfix("+A*BC"))
