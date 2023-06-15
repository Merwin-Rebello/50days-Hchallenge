#power of four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n+1):
            if 4**i == n:
                return True
            if 4**i>n:
                return False    
        return False 

#power of three
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n+1):
            if 3**i == n:
                return True
            if 3**i>n:
                return False    
        return False 