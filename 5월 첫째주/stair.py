num=int(input())
s=[0 for i in range(301)]
total=[0 for i in range(301)]

for i in range(num):
    s[i]=int(input())

total[0]=s[0]
total[1]=s[0]+s[1]
total[2]=max(s[0]+s[2], s[1]+s[2])

for i in range(3, num):
    total[i]=max(total[i-3]+s[i-1]+s[i], total[i-2]+s[i])
print(total[num-1])