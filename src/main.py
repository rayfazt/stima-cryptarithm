from time import time

def read_file(filename):
    f = open("../test/" + filename, 'r')

    lines = f.readlines()
    for i in range(len(lines)):
        temp_string = lines[i]
        result_string = ""
        for j in range(len(temp_string)):
            if (temp_string[j] != "\n"):
                result_string += temp_string[j]
        lines[i] = result_string

    f.close()
    return lines


if __name__ == "__main__":
    filename = input("Masukkan test case: ")
    input_file = read_file(filename)