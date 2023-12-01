puzzle_input = open("puzzle-input.txt", "r") # open the puzzle input

total = 0 

for line in puzzle_input: 
    temp_list = [] 
    for x in line:
        if x.isdigit(): # if x is a digit then we append it to the list of numbers
            temp_list.append(int(x)) 
    # print(temp_list)
    line_value = int(str(temp_list[0]) + str(temp_list[-1])) # create the two digit number
    # print(line_value)
    total += line_value 

print(total)

puzzle_input.close()


