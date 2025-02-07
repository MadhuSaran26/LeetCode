class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # dp to hold the longest subsequence length until i
        sub = [nums[0]]

        for idx in range(1,n):
            num = nums[idx]
            # if curr index value is greater than the largest element in subsequence, then extend it
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                # finding the first element that is larger than or equal to num to replace it with num
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

        