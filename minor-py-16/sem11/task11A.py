stack = []

if __name__ == '__main__':
    while True:
        args = input().split()
        if args[0] == 'push':
            n = int(args[1])
            stack.append(n)
            print('ok')
        elif args[0] == 'pop':
            item = stack.pop()
            print(item)
        elif args[0] == 'back':
            print(stack[-1:][0])
        elif args[0] == 'size':
            print(len(stack))
        elif args[0] == 'clear':
            stack[:] = []
            print('ok')
        elif args[0] == 'exit':
            print('bye')
            break
