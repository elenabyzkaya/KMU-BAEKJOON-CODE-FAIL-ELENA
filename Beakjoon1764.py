import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    heard = set(input_data[2 : 2+n])
    seen = set(input_data[2+n : 2+n+m])
    
    result = sorted(list(heard & seen))
    
    print(len(result))
    if result:
        print('\n'.join(result))

if __name__ == "__main__":
    solve(
    )
