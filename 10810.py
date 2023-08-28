n, m = map(int,input().split()) # 첫 번째 입력은 두 개의 정수
basket = [0] * n # 모든 바구니는 0으로 지정, 바구니는 총 n개

for I in range(0, m) : # m개의 줄에 걸쳐 공을 넣는 방법이 입력되니 반복문을 통해 입력을 m번 받음
    i, j, k = map(int,input().split()) # i번 바구니부터 ~ j번 바구니까지 k공을 넣음
    for x in range(i, j+1): # 1번 바구니부터 넣는다고 하면
        basket[x-1] = k # basket[0] 바구니에 넣어야 하기 때문에 인덱스를 x-1
                        # k번호가 적혀있는 공을 대입, 새로운 공을 넣는 것
                        
for x in range(0, n) : # 반복문을 활용해 바구니 개수만큼 출력
    print(basket[x], end = " ")
    
    