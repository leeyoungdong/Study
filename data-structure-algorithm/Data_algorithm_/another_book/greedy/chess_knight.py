num = input()

number  = int(num[1])
column = int(ord(num[0]) - int(ord('a'))) + 1

moving = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result = 0

for step in moving:
    next_row = number + step[0]
    next_column = column + step[1]
    
    if  next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result +=1

print(result)