#백준 알고리즘 1038번 - 지정문제
#감소하는 수

import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()
for i in range(1, 11):
    for com in combinations(range(0, 10), i):
        com = list(com)
        com.sort(reverse=True)
        nums.append(int("".join(map(str, com))))

nums.sort()

try:
    print(nums[n])
except:
    print(-1)