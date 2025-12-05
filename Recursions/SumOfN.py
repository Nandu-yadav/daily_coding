def SumOfN(n):
    if n==0:
        return 0
    return n + SumOfN(n-1)
  
print(SumOfN(10))