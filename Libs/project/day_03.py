# encoding = utf-8


def question(number):
    num_dict = {}
    """
    使用给定的整数 n，编写一个程序来生成一个包含 (i, ixi) 的字典，该字典是 1 和 n 之间的整数（都包括在内）。然后程序应该打印字典。假设以下输入被提供给程序：8
    """
    for i in range(1, number+1):
        num_dict[i] = i * i
    print(num_dict)


def question_2():
    """
    打印99乘法表
    """
    for a in range(1, 10):
        for b in range(1, a+1):
            print("%d * %d = %d" % (b, a, a*b), end='\t')
        print('\n')


def question_3():
    num_list = []
    """
    求可用被17整除的所有三位数 
    """
    for i in range(99, 999):
        if i % 17 == 0:
            num_list.append(i)
    print(num_list)


def question_4():
    num_list = [1, 2, 3, 4]
    result_list = []
    """
    有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
    """
    for a in num_list:
        for b in num_list:
            for c in num_list:
                if a != b and a != c and b != c:
                    number = "%d%d%d" % (c, b, a)
                    if number not in result_list:
                        result_list.append(int(number))
    A_len = len(result_list)
    print("总共有" + str(A_len) + "个组合，分别是：%s" % result_list)


if __name__ == '__main__':
    question_4()
