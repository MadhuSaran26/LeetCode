class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        p_len = 10 # pattern length
        if len(s) < 10:
            return []
        p = 10**9+7 # large prime modulus
        b = 4 # base - 4 characters in DNA sequence
        b_multiplier = pow(b, p_len - 1, p) # Precompute base multiplier for removing old character
        hash_dict = defaultdict(int)
        char2int = {'A':0, 'C':1, 'G':2, 'T':3} # character mapping for hashing
        p_hash = 0
        #s = list(s)
        result = set()
        # calculating hash
        for idx in range(p_len):
            p_hash = (p_hash * b + char2int[s[idx]]) % p
        
        hash_dict[p_hash] += 1
        
        for idx in range(1, len(s)-p_len+1):
            old, new = s[idx-1], s[idx+p_len-1]
            # Update the rolling hash
            # removing old character's contribution
            p_hash = (p_hash - char2int[old] * b_multiplier) % p
            # adding new character's contribution
            p_hash = (p_hash * b + char2int[new]) % p
            hash_dict[p_hash] += 1
            if p_hash not in result and hash_dict[p_hash] > 1:
                result.add(s[idx:idx+p_len])
        
        return list(result)



            
        