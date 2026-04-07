n, k = map(int, input().split())
max_val = 0

for i in range(1, k + 1):
    res = n * i
    rev_res = int(str(res)[::-1])
    if rev_res > max_val:
        max_val = rev_res

print(max_val)
