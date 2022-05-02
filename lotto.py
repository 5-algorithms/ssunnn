# 0502 알고리즘 스터디
# 백준 알고리즘 6603

def lotto(index, start): # combination의 인덱스, S의 시작 인덱스
    if index==6: # 인덱스 값이 6일시 combination 리스트 문자열로 출력
        print("".join(combination)) 
        return
    for i in range(start, k):
        combination[index]=S[i]
        lotto(index+1, i+1)

combination=[0]*6 

while True:
    num = list(input().split()) # 입력
    k, S = int(num[0]), num[1:] # 개수와 순열 분리
    if k==0: # 개수가 0이면 프로그램 종료
        break
    lotto(0, 0) # 로또 함수 돌리기
    print()