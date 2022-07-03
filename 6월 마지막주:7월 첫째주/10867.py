#백준 알고리즘 10867번
#중복 빼고 정렬하기

n = int(input())

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

for i in arr:
    print(i, end='')