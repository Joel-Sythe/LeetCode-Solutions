1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8
9        characters_s = list()
10        characters_t = list()
11
12        if (len(s) == len(t)):
13            for char in s:
14                characters_s.append(char)
15
16            for char in t:
17                characters_t.append(char)
18
19            for char in characters_s:
20                if char in t:
21                    t = t.replace(char,"", 1)
22                else:
23                    return False
24                
25        else:
26            return False
27        return True
28        