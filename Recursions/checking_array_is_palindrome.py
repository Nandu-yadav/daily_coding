


#one pointer method
def Palindrome(i,arr):
    n=len(arr)
    if i>=n//2:
        return
    elif arr[i] != arr[n-1]:
        return "not a palindrome"
    else:
        Palindrome(i+1,arr)
    return "array is palindrome"
           
    

nums=[2,4,7,9,7,4,2,3]
print(Palindrome(0,nums))


#here i am applying function to the array the printing
# As the mistake i was doing earlier was that i was just printing the function so it just returned none
#that ws wrong , we actually need that array