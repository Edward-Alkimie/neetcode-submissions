class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left_pointer = 0
        right_pointer = 0
        length_s = len(s)
        char_set = set()
        max_length = 0 



        while right_pointer < length_s:
            if s[right_pointer] not in char_set:
                char_set.add(s[right_pointer])
                right_pointer += 1
                # current_length += 1
            else:
                while s[right_pointer] in char_set:
                    char_set.remove(s[left_pointer])
                    left_pointer += 1
                char_set.add(s[right_pointer])
                right_pointer += 1
                    # current_length -= 1
            if right_pointer - left_pointer > max_length:
                max_length = right_pointer - left_pointer 
        
        return max_length

