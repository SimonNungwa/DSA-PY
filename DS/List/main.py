# implement list methods manually


scores = [2, 4, 6, 8]
scoresInNum = ["Two", "Four", "Six", "Eight"]

# indexing
scores[0]


# returns number of times the arg appeared in the list
print(scoresInNum.count(scoresInNum[2]))


# implement count 
def count_occurrences(lst, target):
    count = 0  
    for element in lst:  
        if element == target:  
            count += 1 
    return count 
