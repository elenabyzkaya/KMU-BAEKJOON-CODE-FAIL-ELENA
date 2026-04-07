n = int(input())

if n == 1:
    print("*")
else:
    for i in range(2 * n):
        line = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                line += "*"
            else:
                line += " "
        print(line.rstrip())
