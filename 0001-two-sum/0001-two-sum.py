class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index1 = 0
        index2 = 0

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                elif num + num2 == target:
                    index1 = i
                    index2 = j
                    break

        return [index2, index1]
