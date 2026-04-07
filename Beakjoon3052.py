mport sys

remainders = set()

for _ in range(10):
    num = int(sys.stdin.readline())
    remainders.add(num % 42
                  )

print(len(remainders))
