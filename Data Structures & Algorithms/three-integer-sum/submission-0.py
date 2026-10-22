class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets_list = []
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index -1]:
                continue 

            left = index + 1
            right = len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    triplets_list.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return triplets_list 




-2,-1, 0, 1, 1, 2,3  


        