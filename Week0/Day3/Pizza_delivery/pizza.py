from time import time
from datetime import datetime


def main():
    orders = []
    while True:
        command = input("Enter command>")
        if 'take' in command:
            command = command.split(' ')
            orders.append((command[1], float(command[2])))

        elif command == 'finish':
            return 0

        elif command == 'status':
            for client, price in orders:
                print("Taking order from %s for %.2f" % (client, price))

        elif command == 'save':
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            file = open('orders_%s' % stamp, 'w')
            for client, price in orders:
                file.write(("Taking order from %s for %.2f\n" % (client, price)))


if __name__ == '__main__':
    main()
