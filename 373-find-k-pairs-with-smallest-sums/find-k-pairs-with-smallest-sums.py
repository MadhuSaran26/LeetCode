class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        # since both arrays are sorted, the sum of first elements from these two arrays will be the smallest
        heap = [((nums1[0] + nums2[0]), 0, 0)]
        visited = {(0,0)}
        result, result_len = [], 0
        while heap:
            _, idx1, idx2 = heappop(heap)
            result.append([nums1[idx1], nums2[idx2]])
            result_len += 1
            if result_len == k:
                return result
            
            # next possible smallest elements
            if idx1+1 < m and (idx1+1, idx2) not in visited:
                heappush(heap, ((nums1[idx1+1] + nums2[idx2]), idx1+1, idx2))
                visited.add((idx1+1, idx2))
            if idx2+1 < n and (idx1, idx2+1) not in visited:
                heappush(heap, ((nums1[idx1] + nums2[idx2+1]), idx1, idx2+1))
                visited.add((idx1, idx2+1))
        
        return result # when k > m*n
        