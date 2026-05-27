1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        for index in range(int(len(s)/2)):
7            s[index],s[-(index + 1)] = s[-(index + 1)], s[index]
8
9        