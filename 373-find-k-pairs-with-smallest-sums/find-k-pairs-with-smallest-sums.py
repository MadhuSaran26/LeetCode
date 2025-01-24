class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        result = []
        len_result = 0
        # since both nums1 and nums2 are sorted, sum of the first elements from both will be the smallest
        heap = [(nums1[0]+nums2[0], 0, 0)]
        visited = set()

        while heap:
            _, idx1, idx2 = heappop(heap)
            result.append([nums1[idx1], nums2[idx2]])
            len_result += 1
            if len_result == k:
                return result

            if (idx1, idx2+1) not in visited and idx2+1 < n:
                heappush(heap, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))
            if (idx1+1, idx2) not in visited and idx1+1 < m:
                heappush(heap, (nums1[idx1+1]+nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
            
        return result #when k value is greater than m*n
        

            
