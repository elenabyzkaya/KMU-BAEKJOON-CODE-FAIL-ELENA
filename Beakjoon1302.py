import sys

def solve():
    input_data = sys.stdin.read().split(
    )
    
    if not input_data:
        return
        
    n = int(input_data[0])
    books = input_data[1:n+1]
    
    counts = {}
    for book in books:
        if book in counts:
            counts[book] += 1
        else:
            counts[book] = 1
            
    max_count = max(counts.values()
                   )
    
    candidates = []
    for book, count in counts.items():
        if count == max_count:
            candidates.append(book)
            
    candidates.sort()
    print(candidates[0])

if __name__ == "__main__":
    solve(
    )
