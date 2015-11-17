queue = []

if __name__ == '__main__':
    while True:
        args = input().split()
        if args[0] == 'push':
            n = int(args[1])
            queue.append(n)
            print('ok')
        elif args[0] == 'pop':
            item = queue[0]
            queue = queue[1:]
            print(item)
        elif args[0] == 'front':
            print(queue[0])
        elif args[0] == 'size':
            print(len(queue))
        elif args[0] == 'clear':
            queue[:] = []
            print('ok')
        elif args[0] == 'exit':
            print('bye')
            break
