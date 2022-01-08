from typing import Dict
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_nums: int = len(nums)
        curr_major: int = nums[0]
        num_count: Dict[int, int] = defaultdict(int)
        num_count[nums[0]] = 1
        
        for num in nums[1:]:
            num_count[num] += 1
            if num_count[num] > num_count[curr_major]:
                curr_major = num
            if num_count[curr_major] > (len_nums//2):
                return curr_major
        return curr_major