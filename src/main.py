from time import time

# read from file
def read_file(filename):
    f = open("../test/" + filename, 'r')
    lines = [line.rstrip() for line in f]
    f.close()

    return lines

# get first letter of operands
def get_first_letter(list_string):
    first = []
    for i in range(len(list_string) - 2):
        letter = list_string[i]
        first.append(letter[0])

    return first

# create list of unique characters without + and -
def unique_char(list_string):
    char = []
    for string in list_string:
        for letter in string:
            if letter not in char and letter != "-" and letter != "+":
                char.append(letter)
    
    return char

# convert character to integer
def to_integer():
    # to do
    return 0

if __name__ == "__main__":
    filename = input("Masukkan test case: ")
    input_file = read_file(filename)
    char = unique_char(input_file)
    first = get_first_letter(input_file)
    
    #list_list = [[char],[0 for i in range(len(char))]]
    #print(input_file)
    #print(char)
    #print(first)