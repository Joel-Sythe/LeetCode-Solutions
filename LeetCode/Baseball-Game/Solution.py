1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        
4        result = []
5
6        for act in operations:
7            try:
8                act = int(act)
9                result.append(act)
10
11            except ValueError:
12
13                if act =="C":
14                    result.pop()
15                elif act == "+":
16                    result.append(result[-1] + result[-2])
17                elif act =="D":
18                    result.append(result[-1] * 2)
19
20        return sum(result)
21        