def print_calendar(month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'
    ]

    start_day = 4
    for m in range(month - 1):
        start_day = (start_day + days_in_month[m]) % 7

    print(f"\n---{month_names[month - 1]}---")
    print("--일- 월- 화- 수- 목- 금- 토")

    print("     " * start_day, end="")
    day = 1
    current_col = start_day
    while day <= days_in_month[month - 1]:
        print(f"{day:3d}", end=" ")
        current_col += 1
        if current_col == 7:
            print()
            current_col = 0
        day += 1
    
    if current_col != 0:
        print()
month = int(input("Enter your month: "))
print_calendar(month)
