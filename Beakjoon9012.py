import sys

t = int(sys.stdin.readline())

for _ in range(t):
    ps = sys.stdin.readline().strip()
    balance = 0
    is_vps = True
    
    for char in ps:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance < 0:
            is_vps = False
            break
            
    if is_vps and balance == 0:
        print("YES")
    else:
        print("NO")
