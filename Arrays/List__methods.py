
a=[0,1,2,3,4,5,6]
b=[4,5,6,7,8,9]

#slicing or accessing
print(a[1:])
print(a[1:4])
print(a[:-1])


a.append(2)
a.extend(b)
a.extend(i,5)

#removing
a.remove(x)
a.pop()
a.pop(i)
del a[i]
del a[i:j]
a.clear()

#SEARCHING/checking
x in a
a.index(x)
a.count(x)

a.sort()
a.sort(reverse=True)
sorted(a)

#Reversing
a.reversed()
a.[::-1]

#COPYING
b=a.copy()
b=a[:]

#COMBINING
c=a+b
c=a*3

n=len(a)
m=min(a)
o=max(a)
p=sum(a)

