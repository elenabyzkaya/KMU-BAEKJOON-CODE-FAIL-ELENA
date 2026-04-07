import sys

c = int(sys.stdin.readline())

for _ in range(c):
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    scores = data[1:]
    
    avg = sum(scores) / n
    
    above_avg_count = 0
    for score in scores:
        if score > avg:
            above_avg_count += 1
            
    ratio = (above_avg_count / n) * 100
    
    print(f"{ratio:.3f}%")
