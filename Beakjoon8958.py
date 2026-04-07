import sys

t = int(sys.stdin.readline())

for _ in range(t):
    ox_result = sys.stdin.readline().strip()
    total_score = 0
    current_consecutive = 0
    
    for char in ox_result:
        if char == 'O':
            current_consecutive += 1
            total_score += current_consecutive
        else:
            current_consecutive = 0
            
    print(total_score
         )
