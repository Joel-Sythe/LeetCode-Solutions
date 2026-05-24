1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        characters = [x.lower() for x in s if x.isalnum()]
4        
5        length = len(characters)
6        valid = True
7
8        
9
10        if (length % 2 == 0): #even length of characters
11            for char in range(int((length/2))):
12                left = characters[char]
13                right = characters[-(char + 1)]
14
15                
16                if (left != right):
17                    valid = False
18                    break
19        
20        else: #odd length of characters 
21            for char in range(int((length + 1)/2)):
22                left = characters[char]
23                right = characters[-(char + 1)]
24
25
26                if left != right:
27                    valid = False
28                    break
29        return valid
30
31
32
33        