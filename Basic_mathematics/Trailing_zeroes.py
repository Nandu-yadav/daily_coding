'''
1. Naive Approach
A simple method is to first calculate the factorial of n, then count trailing 0s in the result (We can count trailing 0s by repeatedly dividing the factorial by 10 till the remainder is not 0).

2. EFFICIENT: 
Following is the summarized formula for counting trailing 0s:
Trailing 0s in n! = Count of 5s in prime factors of 
n! = floor(n/5) + floor(n/25) + floor(n/125) + ....
'''

n=int(input())
result=0
i=int(5)
while i<=n:
    result += n//i
    i=i*5
print(result)