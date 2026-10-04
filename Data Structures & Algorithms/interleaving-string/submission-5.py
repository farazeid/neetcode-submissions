from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        def fn(i1: int, i2: int) -> bool:

            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if i1 == len(s1) and i2 == len(s2):
                cache[(i1, i2)] = True
                return cache[(i1, i2)]
            
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s3[i1+i2] and s2[i2] == s3[i1+i2]:
                x = fn(i1+1, i2) if  i1+1 < len(s1) else False
                y = fn(i1, i2+1) if i2+1 < len(s2) else False
                cache[(i1, i2)] = x or y
                return cache[(i1, i2)]
            
            if i1 < len(s1) and s1[i1] == s3[i1+i2]:
                cache[(i1, i2)] = fn(i1+1, i2) or False
                return cache[(i1, i2)]
            if i2 < len(s2) and s2[i2] == s3[i1+i2]:
                cache[(i1, i2)] = fn(i1, i2+1) or False
                return cache[(i1, i2)]
                
            cache[(i1, i2)] = False
            return cache[(i1, i2)]
        
        cache = {}
        return fn(0, 0)
        