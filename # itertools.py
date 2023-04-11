# itertools.combinations() in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.combinations() in Python - Hacker Rank Solution START
from itertools import combinations

io = input().split()
S = io[0]
k = int(io[1])
for i in range(1,k+1):
    for j in combinations(sorted(S),i):
        print("".join(j))
# itertools.combinations() in Python - Hacker Rank Solution END