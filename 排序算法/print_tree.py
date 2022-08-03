import math


def print_tree(array, unit_with=2):
    unit_with = len(str(max(array)))
    length = len(array)
    depth = math.ceil(math.log2(length + 1))
    index = 0
    width = 2 ** depth - 1
    for i in range(depth):
        for j in range(2 ** i):
            print("{:^{}}".format(array[index], width * unit_with),
                  end=" " * unit_with)  # 因为首次长度为 15， 第二次长度 变为 两个 7， 与十五比少了1， 第三次长度变为 两个3，与15比少了3，所以每次end，都要带上一个长度间隔
            index += 1
            if index > length - 1:
                break
        width //= 2
        print()


if __name__ == "__main__":
    print_tree([x + 100 for x in range(13)])
