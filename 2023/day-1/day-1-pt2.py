# IN PROGRESS - this is not a correct solution

puzzle_input = open("sample-input.txt", "r") # open the puzzle input

word_to_number = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

backward_word_to_number = {
    "orez": 0,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9
}

total = 0 

# i just need to find the last instance and first instance of a word form number 
# and replace it overlapping letters maybe dont matter in this case

for line in puzzle_input: 
    temp_list = []
    print(line)
    line = line[::-1] # reverse the line
    print(line)
    for word, number in backward_word_to_number.items():
        line = line.replace(word, str(number), 1)
        print(line)
    line = line[::-1] # reverse back
    for word, number in word_to_number.items(): # this will replace the first word and put the number there instead
        line = line.replace(word, str(number), 1)
    print(line)
    for x in line:
        if x.isdigit(): # if x is a digit then we append it to the list of numbers
            temp_list.append(int(x)) 
    print(temp_list)
    line_value = int(str(temp_list[0]) + str(temp_list[-1])) # create the two digit number
    print(line_value)
    total += line_value 

print(total)

puzzle_input.close()
