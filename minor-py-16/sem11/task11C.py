deck = []

if __name__ == '__main__':
    while True:
        args = input().split()
        if args[0] == 'push_front':
            n = int(args[1])
            deck = [n] + deck
            print('ok')
        if args[0] == 'push_back':
            n = int(args[1])
            deck.append(n)
            print('ok')
        elif args[0] == 'pop_front':
            item = deck[0]
            deck = deck[1:]
            print(item)
        elif args[0] == 'pop_back':
            item = deck.pop()
            print(item)
        elif args[0] == 'front':
            print(deck[0])
        elif args[0] == 'back':
            print(deck[-1:][0])
        elif args[0] == 'size':
            print(len(deck))
        elif args[0] == 'clear':
            deck[:] = []
            print('ok')
        elif args[0] == 'exit':
            print('bye')
            break
