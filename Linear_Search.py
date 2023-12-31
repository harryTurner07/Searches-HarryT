def linear_search(items, search_item):
    """
    A linear search program that goes along every item in a given list and checks if the item is in it
    If so it outputs it's position via a "counter" - read the bottom note 'IMPORTANT'.
    """
    # Local variable to be called later in the program
    selected_item = ""
    x = 0
    while selected_item != search_item:
        selected_item = items[x]
        x = x + 1   # x is used to count up the list and so the program has something to count on to see if the length was exceeded
        if x > len(items):
            return "The item is not in the list"
    return "The index is" + " " + str(x)

list_of_ITEMS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print("Actually prints out the location of it - doesn't count from 0 / zero")
print(linear_search(list_of_ITEMS, 1))
"""
IMPORTANT - Works but it outputs an error if the index is out of range due to the way
I coded it.   It's a problem for future me...
"""