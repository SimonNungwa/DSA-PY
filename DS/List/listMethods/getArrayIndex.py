def getArrayIndex(lst, idx):
    if 0 <= idx < len(lst):  # Check if index is valid
        return lst[idx]      # Return the element at the index
    else:
        raise IndexError("Index out of range")
