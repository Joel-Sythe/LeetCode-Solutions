1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        ans = nums[:]
4        for num in nums:
5            ans.append(num)
6        return ans