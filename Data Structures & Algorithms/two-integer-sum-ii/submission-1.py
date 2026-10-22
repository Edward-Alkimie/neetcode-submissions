class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        listPastNum = {}

        for index, num in enumerate(numbers):
            target_difference = target - num
            if target_difference in listPastNum:
                return [ listPastNum[target_difference], index + 1]
            listPastNum[num] = index + 1
        
            


        