# 백준 알고리즘 11729
# 하노이탑

num = int(input())

def hanoi(num, a, b, c):
    if num==1:
        print(a, c)
        return

    hanoi(num-1, a, c, b)
    print(a, c)
    hanoi(num-1, b, a, c)

sum = 2**num-1
print(sum)
hanoi(num, 1, 2, 3)