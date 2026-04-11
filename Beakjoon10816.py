import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

counts = Counter(cards)

result = []
for q in queries:
    result.append(str(counts[q]))

print(" ".join(result))
