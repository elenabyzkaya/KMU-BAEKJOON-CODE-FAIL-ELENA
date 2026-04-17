hour, minute = map(int, input().split())

cook_time = int(input())

total_minute = hour * 60 + minute + cook_time

final_hour = (total_minute // 60) % 24

final_minute = total_minute % 60
print(final_hour, final_minute)
