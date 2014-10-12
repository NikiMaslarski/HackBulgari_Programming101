import sys


def main():
    file = open("MEGATRON", 'a')
    for index in range(1, len(sys.argv)):
        file_for_concat = open(sys.argv[index], 'r')
        file.write(file_for_concat.read() + '\n')
        file_for_concat.close()
    file.close()


if __name__ == '__main__':
    main()

