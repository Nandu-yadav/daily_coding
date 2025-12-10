#Divide and conqer algorith
#it works on the fact that all the elements before pivot are smaller and all the elments after are greater than pivot
#

def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]         # pivot variable
        i = low - 1               # index of smaller element

        for j in range(low, high):
            if arr[j] < pivot:    # compare with pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # swap

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1              # pivot final position

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)     # left side
            sort(pi + 1, high)    # right side

    sort(0, len(arr) - 1)
    return arr

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))



    