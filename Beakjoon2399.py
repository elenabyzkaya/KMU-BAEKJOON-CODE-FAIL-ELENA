import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

total_sum = 0
for i in range(n):
    total_sum += x[i] * (i - (n - 1 - i))

print(total_sum * 2
     )
