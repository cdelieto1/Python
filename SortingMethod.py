def sort_numbers(sort):
    new_list = []
    while sort:
        minimum = sort[0]  # arbitrary number in list. won't work if i start with 1  
        for x in sort: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        sort.remove(minimum)
    return new_list

x = [67, 45, 2, 13, 1, 998]
y = [89, 23, 33, 45, 10, 12, 45, 45, 45]
       
print sort_numbers(x)
print sort_numbers(y)