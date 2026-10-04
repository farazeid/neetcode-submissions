from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        def fn(i1: int, i2: int) -> bool:

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if i1 == len(s1) and i2 == len(s2):
                return True
            
            state = False
            
            if i1 < len(s1) and s1[i1] == s3[i1+i2]:
                state = fn(i1+1, i2) or state
            if i2 < len(s2) and s2[i2] == s3[i1+i2]:
                state = fn(i1, i2+1) or state
                
            cache[(i1, i2)] = state
            return cache[(i1, i2)]
        
        cache = {}
        return fn(0, 0)
