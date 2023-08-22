while(1): # 무한 반복, while True : 라고 쓸 수도 있음
    x,y = map(int, input().split()) # 입력
    
    if x == 0 and y == 0: # x와 y가 0일 때 탈출
        break
    
    if x < y and y % x == 0: # y가 x보다 크고, 나머지가 0일 때 (x가 y의 약수일 때)
        print("factor")
    elif x < y and x %  y == 0: # y가 x보다 크고, 나머지가 0일 때 (y가 x의 배수일 때)
        print("multiple")
    else : # 그 이외에
        print("neither")