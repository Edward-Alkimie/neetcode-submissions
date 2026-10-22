class Solution:
    def isPalindrome(self, s: str) -> bool:

        left_index = 0
        right_index = len(s) - 1
        
        while left_index <= right_index:
            
            if not s[left_index].isalnum():
                left_index += 1
                continue 
            
            if not s[right_index].isalnum():
                right_index -= 1
                continue 
            

            left = s[left_index].lower()
            right = s[right_index].lower()

            if left == right:
                right_index -= 1
                left_index +=1
                continue 
            else:
                return False
        return True 
        