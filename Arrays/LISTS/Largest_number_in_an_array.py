arr=[3,5,7,2,5,3,1,6,4,9,8]

largest=arr[1]
Slar=arr[1]
for val in arr:
 if val>largest:
  largest=val
print(largest)

for val in arr:
 if val>Slar and val!=largest:
  Slar=val
print(Slar)
 




