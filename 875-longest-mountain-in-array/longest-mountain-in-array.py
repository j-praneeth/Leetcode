class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        max_length = 0
        
        for i in range(1, n - 1):  # The peak can't be at the first or last position
            if arr[i - 1] < arr[i] > arr[i + 1]:  # We found a peak
                left = i - 1
                right = i + 1
                
                # Expand to the left while the values are strictly increasing
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                    
                # Expand to the right while the values are strictly decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                    
                # The length of the mountain is the difference between right and left indices + 1
                max_length = max(max_length, right - left + 1)
        
        return max_length
        
        