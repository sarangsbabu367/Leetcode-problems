class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]