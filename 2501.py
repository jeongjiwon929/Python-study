arr = [] # 배열에 정렬하기 위함
n1, n2 = map(int, input().split())

cnt = 0 # n번 째 작은 수 카운트 변수
for i in range(1, n1+1):
    if n1 % i == 0 : # n1의 약수를 구하는 과정
        arr.append(i) # 약수 정렬함
        cnt += 1
        
if n2 > len(arr): # 약수의 갯수가 n2개보다 적으면 0 출력
    print(0)
else :
    print(arr[n2-1]) # 이해하기
        
    