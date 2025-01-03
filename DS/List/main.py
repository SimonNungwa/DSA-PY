# implement list methods manually


scores = [2, 4, 6, 8]
scoresInNum = ["Two", "Four", "Six", "Eight"]

# indexing
scores[0]


# returns number of times the arg appeared in the list
print(scoresInNum.count(scoresInNum[2]))


# implement count 
for idx in range(scoresInNum):
    if idx != scoresInNum[idx + 1]:
        idx += 1
    else:
        # find a way to return number of times 
        return 