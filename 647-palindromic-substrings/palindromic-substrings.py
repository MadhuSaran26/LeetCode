class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "#" + "#".join(s) + "#" # convert s of odd length (2n + 1)
        radii = [0] * len(s)
        C = R = 0 # variables to track the longest palindrome center and the boundary so far
        result = 0
        for center in range(len(s)):
            # if center is within the boundary of the longest palindrome so far
            # the initial palidrome length around this center can be found using the mirror radius
            # since the palindrome around mirror can extend beyond the left boundary, minimum is considered
            if center < R:
                mirror = 2*C - center
                radii[center] = min(R-center, radii[mirror])
            
            # expand further to check whether palindrome length can be extended around center
            while center + radii[center] + 1 < len(s) and center - radii[center] - 1 >= 0 and s[center + radii[center] + 1] == s[center - radii[center] - 1]:
                radii[center] += 1
            
            # if the current palindrome extends beyond the previous longest palindrome's boundary
            # then update the longest palindrome's C and R values
            if center + radii[center] > R:
                R = center + radii[center]
                C = center
            
            # Every expansion results in palindromic substrings
            result += (radii[center] + 1) // 2
            
        return result
