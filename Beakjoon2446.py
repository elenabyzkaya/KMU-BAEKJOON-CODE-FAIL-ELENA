n = int(input())

for i in range(n):
    spaces = " " * i
    stars = "*" * (2 * (n - i) - 1)
    print(spaces + stars)

for i in range(n - 2, -1, -1):
    spaces = " " * i
    stars = "*" * (2 * (n - i) - 1)
    print(spaces + stars)
