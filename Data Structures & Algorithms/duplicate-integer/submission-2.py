class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = set()
        for num in nums:
            if num in newlist:
                return True
            else:
                newlist.add(num)
        return False 

        