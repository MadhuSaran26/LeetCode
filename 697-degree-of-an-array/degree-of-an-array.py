class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(lambda: [0, float('inf'), float('-inf')])
        max_freq = 0
        seq_length = float('inf')

        for idx, elem in enumerate(nums):
            if elem in count:
                count[elem][2] = idx
            else:
                count[elem][1] = count[elem][2] = idx
            count[elem][0] += 1
            
            max_freq = max(max_freq, count[elem][0])
        
        for unique_elem in count:
            if count[unique_elem][0] == max_freq:
                seq_length = min(seq_length, count[unique_elem][2] - count[unique_elem][1] + 1)
        
        return seq_length


        