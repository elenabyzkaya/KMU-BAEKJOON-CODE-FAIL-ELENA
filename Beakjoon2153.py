import sys

word = sys.stdin.readline().strip()
total = 0

for char in word:
    if 'a' <= char <= 'z':
        total += ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        total += ord(char) - ord('A') + 27

is_prime = True
for i in range(2, int(total**0.5) + 1):
    if total % i == 0:
        is_prime = False
        break

if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
