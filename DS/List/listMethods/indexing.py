import main

# indexing
main.scores[0]


def getArrayIndex(lst, idx):
    if 0 <= idx < len(lst):  # Check if index is valid
        return lst[idx]      # Return the element at the index
    else:
        raise IndexError("Index out of range")

def findIndex(lst, target):
    for idx, element in enumerate(lst):  # Use enumerate for index tracking
        if element == target:
            return idx
    return -1  # Return -1 if the target is not found



# returns number of times the arg appeared in the list
print(main.scoresInNum.count(main.scoresInNum[2]))
