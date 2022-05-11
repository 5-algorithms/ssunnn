# 백준 알고리즘 2920
# 음계

scale = list(map(int, input().split()))

if scale == sorted(scale):
    print("ascending")
elif scale == sorted(scale, reverse=True):
    print("descending")
else:
    print("mixed")