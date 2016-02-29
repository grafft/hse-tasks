def check_diag(n, matrix):
    return any([matrix[i][i] == 1 for i in range(n)])


def is_orient(n, matrix):
    for i in range(n):
        for j in range(n/2):
            if not matrix[i][j] == matrix[j][i]:
                return True
    return False


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print('NO') if check_diag(n, matrix) else print('YES')
    print('NO') if is_orient(n, matrix) else print('YES')
