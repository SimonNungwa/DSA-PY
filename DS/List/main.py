# implement list methods manually


scores = [2, 4, 6, 8]
scoresInNum = ["Two", "Four", "Six", "Eight"]



# implement count 
def count_occurrences(lst, target):
    count = 0  
    for element in lst:  
        if element == target:  
            count += 1 
    return count 


# implement append method
def appendArrayElement(lst):
    value = input("Enter value to be appended: ")  # Get user input
    new_lst = [0] * (len(lst) + 1)  # Create a new list with one extra space
    
    # Copy all elements to the new list
    for i in range(len(lst)):
        new_lst[i] = lst[i]

    # Add new value at the last index
    new_lst[len(lst)] = value  

    return new_lst  # Return the updated list

