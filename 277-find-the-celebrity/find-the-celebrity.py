# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        @lru_cache(None)
        def cacheKnows(a, b):
            return knows(a, b)
        
        def isCelebrity(candidate):
            for idx in range(n):
                if idx != candidate:
                    if cacheKnows(candidate, idx) or not cacheKnows(idx, candidate):
                        return False
            return True
        
        possible_candidate = 0
        for idx in range(n):
            if cacheKnows(possible_candidate, idx):
                possible_candidate = idx
        
        return possible_candidate if isCelebrity(possible_candidate) else -1
        