# One line solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(list(set(nums))) == len(nums) else True


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set() 
        for n in nums:
            if n not in d:
                d.add(n)
            else:
                return True
        return False
