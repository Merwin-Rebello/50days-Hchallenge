#take input in variable x
class Solution:
    def isPalindrome(self, x: int) -> bool: #function definition 
        if str(x) == str(x)[::-1]:#compare the string already given from back and from index -1 which is the alst variable
            return True
        else:
            return False 