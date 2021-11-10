# encoding = utf-8


def question(number):
    pass
    """
    使用给定的整数 n，编写一个程序来生成一个包含 (i, ixi) 的字典，该字典是 1 和 n 之间的整数（都包括在内）。然后程序应该打印字典。假设以下输入被提供给程序：8
    """
    num_dict = {}
    for i in range(1, number+1):
        num_dict[i] = i * i
    print(num_dict)


if __name__ == '__main__':
    question(8)
