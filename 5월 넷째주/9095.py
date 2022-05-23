# 백준 알고리즘
# 9095번
# 1, 2, 3 더하기

num = int(input())

def sum(number):
    if number==1:
        print(1)
    elif number == 2:
        return 2
    elif number == 3:
        return 4
    else:
        return sum(n-1)+sum(n-2)+sum(n-3)

for i in range(num):
    n = int(input())
    print(sum(n))