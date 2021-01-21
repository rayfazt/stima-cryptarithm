from time import time

def read_file(filename):
    f = open(filename, 'r')


def main():
    tc = input("Masukkan test case: ")
    read_file(tc)

if __name__ == "__main__":
    main()