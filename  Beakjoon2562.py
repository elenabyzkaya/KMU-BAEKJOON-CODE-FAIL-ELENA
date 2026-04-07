import sys

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline()))   

max_val = max(nums)
max_index = nums.index(max_val) + 1

print(max_val)
print(max_index)