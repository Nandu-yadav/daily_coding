

def read(n, book, target):
    left, right = 0, n - 1
    book.sort()

    while left < right:
        s = book[left] + book[right]

        if s == target:
            return "YES"
        elif s < target:
            left += 1
        else:
            right -= 1
    return "NO"

#time : O(n)= N + NlogN
    