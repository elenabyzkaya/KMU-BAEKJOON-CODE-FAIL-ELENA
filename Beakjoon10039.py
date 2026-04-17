total_score = 0
    
for _ in range(5):
    score = int(input())
       
    if score < 40:
        score = 40
              
    total_score += score
    
    average = total_score // 5
print(average)
