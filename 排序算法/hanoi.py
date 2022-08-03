def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("把%s上的盘子移动到%s" % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, 'a', 'b', 'c');
