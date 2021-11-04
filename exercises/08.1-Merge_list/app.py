chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    
    for x in list1:
        new_list.append(x)

    for y in list2:
        new_list.append(y)
    
    return new_list

print(merge_list(chunk_one, chunk_two))
