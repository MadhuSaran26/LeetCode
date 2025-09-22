class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        result = 0
        left = right = 0
        for age in ages:
            if age < 15:
                continue
            while ages[left] <= age * 0.5 + 7:
                left += 1
            while right + 1 < len(ages) and ages[right + 1] <= age:
                right += 1
            result += right - left
        return result
