class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_seen = {}
        list_index_output = []

        for index, num in enumerate(nums):
            target_diff = target - num
            
            if target_diff in dict_seen:
                print(dict_seen)
                list_index_output.append(dict_seen[target_diff])
                print(list_index_output)
                list_index_output.append(index)
                return list_index_output
            else:
                dict_seen[num] = index
        
