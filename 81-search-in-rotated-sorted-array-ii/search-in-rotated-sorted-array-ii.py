class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ## Intuition
        # Rotated sorted array split into F (first) and S (second)
        # Array Start always greater than or equal to elements from S
        # nums[mid] == Array Start -> linear search
        # target == nums[mid] -> target found
        # nums[mid] and target both in the same half, regular binary search
        # nums[mid] in F (target in S) -> start = mid + 1 (move to towards target)
        # nums[mid] in S (target in F) -> end = mid - 1 (move to towards target)

        def existInFirst(start, element):
            return nums[start] <= element
        
        def canBinarySearch(start, element):
            return nums[start] != element
        
        if not nums:
            return False
        
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return True

            # nums[mid] == Array Start -> no binary search -> linear search
            if not canBinarySearch(start, nums[mid]):
                start += 1
                continue
            
            # check whether nums[mid] and target belong to F
            pivot_array = existInFirst(start, nums[mid])
            target_array = existInFirst(start, target)

            # Both in same array -> XOR will be False
            if pivot_array ^ target_array:
                # Both not in same array
                # pivot_array == True -> Target in S -> move start
                # pivot_array == False -> Target in F -> move end
                if pivot_array:
                    start = mid + 1 
                else:
                    end = mid - 1
            else:
                # Both in same sub-array -> regular binary search
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
      
        return False

    
