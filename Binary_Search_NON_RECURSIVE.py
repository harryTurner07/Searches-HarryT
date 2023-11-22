def binary_search(items, search_item):
    """
    A binary search which starts at the middle (midpoint), splits the list in half; checks if the item is in the greater or lower half of the list
    Disregards the other half and continues until the item is found
    """
    found = False
    first = 0
    last = len(items) - 1
    while (first <= last) and (found == False):
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            found == True
        else:
            if items[midpoint] < search_item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    if found == True:
        return "Item found at position", midpoint
    else:
        return "Item not found in list", -1

list_of_ITEMS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(binary_search(list_of_ITEMS, 5))