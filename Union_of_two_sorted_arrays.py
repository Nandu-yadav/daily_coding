nums1=[1,2,3,4,5,6]
nums2=[4,5,6,7,8,9,10]



#OPTIMAL
"""Core Idea (Two Pointers)

Since both arrays are sorted, maintain two indices i and j.

Move through both arrays simultaneously.

At each step, pick the smaller element and add to result only if not already added.

Skip duplicates in both arrays.

This leverages the sorted property → O(n + m) time."""
def union_optimal(arr1,arr2):
    i=0
    j=0
    union=[]
    m=len(arr1)
    n=len(arr2)
    while i < m and j < n:
        if arr1[i]<arr2[j]:
            if not union or union[-1] !=arr1[i]:
                union.append(arr1[i])
                i+=1
            
        elif arr2[j]<arr1[i]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    #remaining elements
    while i < m:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Add remaining arr2 elements
    while j < n:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

print(union_optimal(nums1,nums2))

#brute

'''
Idea

Combine all elements of both arrays into a new list.

Then remove duplicates by checking each element’s presence.

Do not use two-pointer optimization — treat it as if arrays were unsorted'''
def Union_brute(arr1,arr2):
    list=arr1+arr2
    print(list)
    result=[]
    for val in list:
        if val not in result :
            result.append(val)
    
    result.sort()
    return result

#Brute using set!!!
'''Idea

Insert every element from both arrays into a set.

Since a set automatically removes duplicates, the union is obtained.

Convert back to a sorted list if needed.

This is still considered brute because it doesn't use the sorted property of arrays and uses an external data structure.
'''
def union_set(arr1,arr2):
    s=set()
    for val in arr1:
        st.add(val)
    for val in arr2:
        st.add(y)

    result=sorted(list(s))
    return result


