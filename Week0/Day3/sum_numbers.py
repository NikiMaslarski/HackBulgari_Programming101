import sys


def main():
    file = open(sys.argv[1], 'r')
    numbers = file.read()
    sum = 0
    numbers = numbers.split(" ")
    for number in numbers:
        sum += int(number)
    print(sum)
    file.close()


if __name__ == '__main__':
    main()

