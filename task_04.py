def sort_list(list: list):
    list.sort(reverse=True)
    if (len(list) > 0): list.append(list[-1])
    print(list)

sort_list([]) #=> [] 
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2] 
sort_list([1]) #=>[1,1] 
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]