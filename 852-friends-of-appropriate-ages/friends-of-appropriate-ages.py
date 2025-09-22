class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count_ages = sorted(Counter(ages).items()) # (age, count)
        window = requests = left = 0
        for right in range(len(count_ages)):
            # window represents the number of eligible people who can receive requests
            window += count_ages[right][1]

            while left < right and count_ages[left][0] <= count_ages[right][0] * 0.5 + 7:
                window -= count_ages[left][1]
                left += 1
            
            if count_ages[right][0] > 14:
                requests += count_ages[right][1] * (window-1)
        
        return requests
            
        