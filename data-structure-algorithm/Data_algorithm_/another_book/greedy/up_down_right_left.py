num = int(input())
data = input().split()

x, y = 1, 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ["L","R","U","D"]

for plan in data:
    
    for i in range(len(move)):
        if plan == move[i]:

            nx = x + dx[i]
            print(dx[i])
            ny = y + dy[i]  
            print(dy[i])
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue

    x, y = nx, ny

print(x,y)