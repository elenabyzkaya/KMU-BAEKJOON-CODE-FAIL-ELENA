def d(n):
    return  n + sum(int(digit) for digit in str(n))

self_numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    generated_numbers.add(d(i))

self_numbers -= generated_numbers

for num in sorted(self_numbers):
    print(num)
    
