# encoding = utf-8

def question_1():
    num_list = []
    """
    编写一个程序，找出所有能被 7 整除但不是 5 倍数的数字，在 2000 到 3200 之间（两者都包括在内）。得到的数字应该以逗号分隔的顺序打印在一行上。
    """
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')
    print('\b')


def question_2(num):
    count = 1
    """
    计算给定数字的阶乘
    """
    for i in range(1, num+1):
        count *= i
    print(count)


if __name__ == '__main__':
    question_2(8)