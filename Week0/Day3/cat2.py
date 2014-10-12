import sys


def main():
    for index in range(1, len(sys.argv)):
        file = open(sys.argv[index], "r")
        print(file.read())
        file.close()

if __name__ == '__main__':
    main()

