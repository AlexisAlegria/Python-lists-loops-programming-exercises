list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

#Your code here:
def merge_two_list(items):
    oddList=[]
    evenList=[]
    oddAndEvenList = []

    for x in items:
        if x % 2 != 0:
            oddList.append(x)
        else:
            evenList.append(x)
    
    oddAndEvenList = oddList + evenList

    return oddAndEvenList

print(merge_two_list(list_of_numbers))