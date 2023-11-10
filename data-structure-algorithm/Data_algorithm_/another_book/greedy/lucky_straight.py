n = input()
n_len = len(n)


left = n[0:n_len//2] 
right = n[n_len//2:]

result=0

for i in left:
    result += int(i)

for i in right:
    result -= int(i)

if result == 0:
    print("LUCKY")
else:
    print("READY")