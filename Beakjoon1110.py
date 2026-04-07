n = int(input()
       )
number = n
count = 0
while True:
    digit_sum = (number // 10) + (number % 10)
    number = ((number % 10) * 10) + (digit_sum % 10)
    count += 1
    
    if number == n:
        break
print(count)
