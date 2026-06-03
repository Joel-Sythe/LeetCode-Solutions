1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3
4        tn = ""
5        sn = ""
6
7        for char in s:
8            if char == '#':
9                sn = sn[:-1]
10            else:
11                sn += char
12
13        for char in t:
14            if char == '#':
15                tn = tn[:-1]
16            else:
17                tn += char
18        
19
20        if sn == tn:
21            return True
22        
23        else:
24            return False
25        