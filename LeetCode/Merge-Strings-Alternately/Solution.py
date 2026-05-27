1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        
4        iterations = int(len(word1) + len(word2))
5        result = ""
6
7        for i in range(iterations):
8            try:
9                result += word1[i] + word2[i]
10
11            except(IndexError):
12                if len(word1) > len(word2):
13                    result += word1[i:]
14
15                else:
16                    result += word2[i:]
17
18                break
19        return result
20
21
22        