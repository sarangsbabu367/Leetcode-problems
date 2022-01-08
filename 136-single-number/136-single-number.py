from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_set = defaultdict(set)
        for num in nums:
            if num in count_set[1]:
                count_set[2].add(num)
            else:
                count_set[1].add(num)
        return list(count_set[1] - count_set[2])[0]