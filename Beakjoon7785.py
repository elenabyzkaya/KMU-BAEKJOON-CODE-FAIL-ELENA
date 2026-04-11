import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    logs = input_data[1:]
    
    current_employees = set()
    
    for i in range(0, len(logs), 2):
        name = logs[i]
        action = logs[i+1]
        
        if action == "enter":
            current_employees.add(name)
        else:
            current_employees.discard(name)
            
    result = sorted(current_employees, reverse=True)
    
    print('\n'.join(result))

if __name__ == "__main__":
    solve()
