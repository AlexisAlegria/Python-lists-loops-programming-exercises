
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def my_function(name):
    return name.startswith("R")

resulting_names = list(filter(my_function,all_names))

print(resulting_names)




