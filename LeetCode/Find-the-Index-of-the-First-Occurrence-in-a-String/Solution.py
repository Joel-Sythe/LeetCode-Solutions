1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        
4        for index, hay in enumerate(haystack):
5            
6            if hay == needle[0]:
7                if needle in haystack[index: index + len(needle)]:
8                    return index
9        return -1
10
11