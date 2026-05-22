class Solution:
    # Function to find the indices of 
    # next smaller elements
    def findNSE(self, arr):
        n = len(arr)
        # To store the answer
        ans = [0] * n
        # Stack 
        st = []
        # Start traversing from the back
        for i in range(n - 1, -1, -1):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the smaller element
            while st and arr[st[-1]] >= currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # next greater elements
    def findNGE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Start traversing from the back
        for i in range(n - 1, -1, -1):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the greater element
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # previous smaller or equal elements
    def findPSEE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Traverse on the array
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements are greater than the current element
            while st and arr[st[-1]] > currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # previous greater or equal elements
    def findPGEE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Traverse on the array
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements are smaller than the current element
            while st and arr[st[-1]] < currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the sum of the 
    # minimum value in each subarray
    def sumSubarrayMins(self, arr):
        
        nse = self.findNSE(arr)
        
        psee = self.findPSEE(arr)
        
        # Size of array
        n = len(arr)
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Count of first type of subarrays
            left = i - psee[i]
            
            # Count of second type of subarrays
            right = nse[i] - i
            
            # Count of subarrays where 
            # current element is minimum
            freq = left * right * 1
            
            # Contribution due to current element 
            val = (freq * arr[i] * 1)
            
            # Updating the sum
            total_sum += val
        
        # Return the computed sum
        return total_sum
    
    # Function to find the sum of the 
    # maximum value in each subarray
    def sumSubarrayMaxs(self, arr):
        
        nge = self.findNGE(arr)
        
        pgee = self.findPGEE(arr)
        
        # Size of array
        n = len(arr)
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Count of first type of subarrays
            left = i - pgee[i]
            
            # Count of second type of subarrays
            right = nge[i] - i
            
            # Count of subarrays where 
            # current element is maximum
            freq = left * right * 1
            
            # Contribution due to current element 
            val = (freq * arr[i] * 1)
            
            # Updating the sum
            total_sum += val
        
        # Return the computed sum
        return total_sum
    
    # Function to find the sum of 
    # subarray ranges in each subarray
    def subArrayRanges(self, arr):
        
        # Return the result
        return (self.sumSubarrayMaxs(arr) - 
                self.sumSubarrayMins(arr))

# Main function to test the solution
if __name__ == "__main__":
    arr = [1, 2, 3]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the sum of 
    # subarray ranges in each subarray
    ans = sol.subArrayRanges(arr)
    
    print("The sum of subarray ranges is:", ans)