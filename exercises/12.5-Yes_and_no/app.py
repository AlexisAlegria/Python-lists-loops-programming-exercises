theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

result=list(map(lambda x: "wiki" if x == 1 else "woko", theBools))
print(result)

# def listConverter(item):
#     if item == 1:
#         item == "wiki"
#     else:
#         item == "woko"

#     return item

# new_list = list(map(listConverter, theBools))
# print(new_list)