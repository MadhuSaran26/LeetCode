class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        alen, blen = len(nums1), len(nums2)
        nlen = alen + blen

        def binary_search(k, astart, aend, bstart, bend):

            if astart > aend:
                return nums2[k-astart]
            if bstart > bend:
                return nums1[k-bstart]

            amid, bmid = (astart + aend)//2, (bstart + bend)//2
            avalue, bvalue = nums1[amid], nums2[bmid]

            if amid + bmid < k:
                if avalue > bvalue:
                    return binary_search(k, astart, aend, bmid+1, bend)
                else:
                    return binary_search(k, amid+1, aend, bstart, bend)
            else:
                if avalue > bvalue:
                    return binary_search(k, astart, amid-1, bstart, bend)
                else:
                    return binary_search(k, astart, aend, bstart, bmid-1)
        
        if nlen%2:
            return binary_search((nlen//2), 0, alen-1, 0, blen-1)
        else:
            return (binary_search((nlen//2 - 1), 0, alen-1, 0, blen-1) + 
            binary_search((nlen//2), 0, alen-1, 0, blen-1))/2
        