class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = []
        
        nums.sort()
        for pos, num in enumerate(nums):
            # Skipping the same starting number.
            if pos > 0 and nums[pos - 1] == num:
                continue
            
            left, right = pos + 1, len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skipping already found left & right pairs.
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
        return triplets