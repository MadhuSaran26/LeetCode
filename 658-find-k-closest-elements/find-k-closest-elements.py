class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        # Need to find the starting point of the window where the elements are the closest to x
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # if the starting point of the window is father away than the point outside the window, move left
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]

        
        