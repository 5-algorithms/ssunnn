# 백준 알고리즘
# 2108번
# 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    a.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(a)/n))

# 중앙값
a.sort()
print(a[n//2])

# 최빈값
cnt = Counter(a).most_common(2)
if len(cnt)>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위
print(max(a)-min(a))