import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    k = int(input_data[0])
    l = int(input_data[1])
    student_ids = input_data[2:]
    
    last_click = {}
    
    for i in range(l):
        last_click[student_ids[i]] = i
        
    waiting_list = sorted(last_click.keys(), key=lambda x: last_click[x])
    
    count = 0
    for student in waiting_list:
        if count == k:
            break
        print(student)
        count += 1

if __name__ == "__main__":
    solve(
    )
