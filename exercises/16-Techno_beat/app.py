def lyrics_generator(sequence):
    output = []
    counter = 0

    for i in sequence:
        if i == 0:
            output.append("Boom")
        elif i == 1:
            output.append("Drop the base")
            counter = counter + 1
            if counter == 3:
              output.append("!!!Break the base!!!")
    final_output = " ".join(output)
    return final_output
    

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))