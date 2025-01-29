class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = dict()
        for idx, elem in enumerate(nums):
            if elem != 0:
                self.nums[idx] = elem
    
    def getVector(self):
        return self.nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        vec_nums = vec.getVector()
        for key in vec_nums:
            if key in self.nums:
                result += vec_nums[key] * self.nums[key]
        return result

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)