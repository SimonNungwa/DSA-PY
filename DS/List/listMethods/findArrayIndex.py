def findIndex(lst, target):
    for idx, element in enumerate(lst):  # Use enumerate for index tracking
        if element == target:
            return idx
    return -1  # Return -1 if the target is not found
