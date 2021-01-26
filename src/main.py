import time

# read from file
def read_file(filename):
    f = open("../test/" + filename, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines

# get operands and result string from problem
def get_op_and_res(input_file):
    op = []
    res = [input_file[-1]]
    for string in input_file[:-2]:
        op.append(string.replace("+", ""))
    return op, res

# get first letter of operands
def get_first_letter(list_string):
    first_char = []
    for i in range(len(list_string) - 2):
        letter = list_string[i]
        first_char.append(letter[0])
    return first_char

# create list of unique characters without + and -
def unique_char(list_string):
    char = []
    for string in list_string:
        for letter in string:
            if letter not in char and letter != "-" and letter != "+":
                char.append(letter)
    return char

# convert character to integer
def to_integer(string, dict_sol):
    total = ''
    for char in string:
        if char in dict_sol:
            total += str(dict_sol[char])
    return int(total)

# algorithm taken from python docs (https://docs.python.org/3/library/itertools.html#itertools.permutations)
# Parameters: list_num (list of numbers), r (length of permutation elements)
# DISCLAIMER: I don't know if this classify as brute force or not, tried to use backtracking and
#             it somehow performed much worse than this ¯\_(ツ)_/¯
def permutations(list_num, r):
    pool = tuple(list_num)
    n = len(pool)
    if r > n:
        return
    index = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in index[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                index[i:] = index[i+1:] + index[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                index[i], index[-j] = index[-j], index[i]
                yield tuple(pool[i] for i in index[:r])
                break
        else:
            return

# solver
# note: can only search for one solution
def solve(op, res, char, first, list_num):
    count = 0
    for perm in permutations(list_num, len(char)):
        dict_sol = dict(zip(char, perm)) 
        count += 1
        for num in first:
            if dict_sol[num] != 0:    # first digit of operands can't be 0
                total_op = 0
                total_res = 0
                for string in op:
                    total_op += to_integer(string, dict_sol)
                for string in res:
                    total_res += to_integer(string, dict_sol)
                
                # when solution is found, print it
                if total_op == total_res and len(str(total_res)) == len(res[0]):
                    print("SOLUTION:")
                    for string in op[:-1]:
                        print(to_integer(string, dict_sol))
                    print(to_integer(op[-1], dict_sol), "+", sep='')
                    print("------")
                    print(total_res)
                    return count


# main program
if __name__ == "__main__":
    filename = input("Masukkan test case (dengan .txt): ")

    # begin time
    start = time.time()

    # print problem
    f = open("../test/" + filename, 'r')
    print()
    print("PROBLEM:")
    print(f.read())
    print()
    f.close()

    # initialize parameters
    input_file = read_file(filename)
    op, res = get_op_and_res(input_file)
    char = unique_char(input_file)
    first = get_first_letter(input_file)
    list_num = [0,1,2,3,4,5,6,7,8,9]

    # solve
    count = solve(op, res, char, first, list_num)

    # print performance
    print("\nWaktu Eksekusi Program: {:.2f}".format(time.time() - start), "detik")
    print("Jumlah Total Tes:", count)

    print("\nPress enter to exit")
    input()