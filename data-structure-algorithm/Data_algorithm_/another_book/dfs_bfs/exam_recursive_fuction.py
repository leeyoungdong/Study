def recursive_fuction(i):
    if i == 100:
        return
    
    print(i, '번째', i+1, '번째 재귀 함수 호출')
    recursive_fuction(i+1)
    print(i,'번째 재귀함수 종료')

recursive_fuction(1)