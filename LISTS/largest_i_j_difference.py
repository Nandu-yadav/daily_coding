#Given an array arr of positive integers. You have to return the maximum of j - i such that arr[i] < arr[j] and i < j.
'''Examples:
Input: arr[] = [1, 10]
Output: 1
Explanation: arr[0] < arr[1] so (j-i) is 1-0 = 1.
Input: arr[] = [5, 4, 3]
Output: 0
Explanation: There is no pair that satisfies the given condition.
Input: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6
Explanation: In the given array arr[1] < arr[7] satisfying the required condition(arr[i] < arr[j]) thus giving the maximum difference of j - i which is 6(7-1). '''

