#백준 알고리즘 1946번
#신입 사원

t = int(input())

for i in range(t):
    cnt = 1
    people = []

    n = int(input())
    for i in range(n):
        paper, interview = map(int, input().split())
        people.append([paper, interview])

    people.sort()
    max = people[0][1]

    for i in range(1, n):
        if max > people[i][1]:
            cnt += 1
            max = people[i][1]

    print(cnt)