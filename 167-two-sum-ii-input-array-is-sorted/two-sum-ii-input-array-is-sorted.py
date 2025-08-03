class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_pair = dict()
        result = []
        for idx, num in enumerate(numbers):
            if target - num in sum_pair:
                result = [sum_pair[target-num], idx+1]
            sum_pair[num] = idx+1
        return result