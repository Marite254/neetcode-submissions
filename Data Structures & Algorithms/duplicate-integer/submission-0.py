class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for elem in nums:
            if elem in count:
                return True
            count.add(elem)
        return False