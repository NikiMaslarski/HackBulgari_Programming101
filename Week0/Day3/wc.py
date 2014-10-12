import sys


def main():
    file = open(sys.argv[2], 'r')
    content = file.read()
    if sys.argv[1] == 'chars':
        pass

    elif sys.argv[1] == 'words':
        content = content.split()

    elif sys.argv[1] == 'lines':
        content = content.split('\n')

    print(len(content))


if __name__ == "__main__":
    main()

