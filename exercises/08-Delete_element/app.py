people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_list = []
    for person in people:
        new_list.append(person)

    for i in range(len(new_list)-1):
        if(new_list[i] == person_name):
            new_list.remove(new_list[i])

    return new_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))