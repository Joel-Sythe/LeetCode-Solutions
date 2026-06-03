1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3
4        stack = []
5
6        for c in s:
7
8            if stack and stack[-1] == c:
9                stack.pop()
10
11            else:
12                stack.append(c)
13
14        return ''.join(stack)
15
16
17        