def push(s, *args):
    print('push', int(args[0]))


def pop(s, *args):
    print('pop')


def exit(s, *args):
    return 'bye'


d = {'push': push, 'pop': pop, 'exit': exit}

if __name__ == '__main__':
    s = []
    while True:
        command = input().split()
        result = d[command[0]](s, *command[1:])
        if result == 'bye':
            print(result)
            break
