1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8
9
10        if (len(s) == len(t)):
11            for char in s:
12                if char in t:
13                    t = t.replace(char,"", 1)
14                else:
15                    return False
16                
17        else:
18            return False
19        return True
20        