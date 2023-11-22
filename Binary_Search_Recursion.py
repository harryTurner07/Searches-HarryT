def binary_search_recursion(items, search_item):
    # Definitions for the start & end index
    start_index = items[0]
    end_index = items[-1]
    """
    A Binary search using recursion, returning the index of the item in the list or -1 if not in the list.
    The start index should be 0 and the end index should be 1 less than the length of the list.
    """
    # Base cases for if the item isn't in the list or if the item has been found
    if start_index > end_index:
        return -1
    middle_index = (start_index - end_index) // 2
    current_item = items[middle_index]
    if current_item == search_item:
        return middle_index
    elif current_item < search_item:
        return binary_search_recursion(items, middle_index + 1, end_index, search_item)
    else:
        return binary_search_recursion(items, start_index, middle_index - 1, search_item);

list_of_ITEMS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
binary_search_recursion()