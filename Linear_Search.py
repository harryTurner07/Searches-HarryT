def linear_search(items, search_item):
    selected_item = ""
    x = 0
    while selected_item != search_item:
        selected_item = items[x]
        x = x + 1
        if x > len(items):
            return "The item is not in the list"
    return "The index is" + " " + str(x)

list_of_ITEMS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print("Actually prints out the location of it - doesn't count from 0 / zero")
print(linear_search(list_of_ITEMS, 1))