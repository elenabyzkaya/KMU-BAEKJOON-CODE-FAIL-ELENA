import sys

def solve():
    n = int(sys.stdin.readline())
    
    if n < 100:
        print(n)
    else:
        count = 99
        for i in range(100, n + 1):
            if i == 1000:
                break
            
            nums = list(map(int, str(i)))
            if (nums[0] - nums[1]) == (nums[1] - nums[2]):
                count += 1
        print(count)

solve()
