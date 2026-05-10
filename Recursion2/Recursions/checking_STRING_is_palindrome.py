def Palindrome(i,arr):
    n=len(arr)
    if i>=n//2:
        return
    elif arr[i] != arr[n-1]:
        return "not a palindrome"
    else:
        Palindrome(i+1,arr)
    return " is a palindrome"
           
    

string = "MADAM"
print(Palindrome(0,string))