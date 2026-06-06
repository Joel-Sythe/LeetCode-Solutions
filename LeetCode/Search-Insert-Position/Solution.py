1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        
4        left = 0
5        right = len(nums) - 1
6        
7        while left <= right:
8            
9            mid = (left + right) // 2
10            
11            if nums[mid] == target:
12                return mid
13        
14            if nums[mid] > target:
15                right = mid - 1
16            else:
17                left = mid + 1
18        return left
19            
20            
21            
22                
23        