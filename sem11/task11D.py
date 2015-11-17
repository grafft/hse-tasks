def push(q, n):
    q.append(n)


def pop(q):
    item = q[0]
    q.remove(item)
    return item


if __name__ == '__main__':
    cards_1 = list(map(int, input().split()))
    cards_2 = list(map(int, input().split()))

    i = 0
    while cards_1 and cards_2 and i < 1000000:
        card_1 = pop(cards_1)
        card_2 = pop(cards_2)
        if card_1 == 0 and card_2 == 9:
            push(cards_1, card_1)
            push(cards_1, card_2)
        elif card_1 == 9 and card_2 == 0:
            push(cards_2, card_1)
            push(cards_2, card_2)
        elif card_1 > card_2:
            push(cards_1, card_1)
            push(cards_1, card_2)
        elif card_2 > card_1:
            push(cards_2, card_1)
            push(cards_2, card_2)

        i += 1

    if not cards_1:
        print('second {0}'.format(i))
    elif not cards_2:
        print('first {0}'.format(i))
    else:
        print('botva')
