# coding = utf-8
import math


def question(wages):
    price = int(wages)
    """
    企业发放的奖金根据利润提成。
    利润低于或等于10万元时，奖金可提10%；
    高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%;
    高于100万元时，超过100万元的部分按1%提成，
    从键盘输入当月利润I，求应发放奖金总数？
    """
    """
    # 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    # 题目：判断101-200之间有多少个素数，并输出所有素数。
    # 题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
    """
    if price <= 10:
        money = price * 0.1
        return money
    elif 10 < price <= 20:
        money = 1 + (price - 10) * 0.075
        return money
    elif 20 < price <= 40:
        money = 1.75 + (price - 20) * 0.05
        return money
    elif 40 < price <= 60:
        money = 2.75 + (price - 40) * 0.03
        return money
    elif 60 < price <= 100:
        money = 3.35 + (price - 60) * 0.015
        return money
    elif price > 100:
        money = 3.95 + (price - 100) * 0.01
        return money


def question_2():
    i = 0
    """
    题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    """
    while True:
        i += 1
        m = int(math.sqrt(i + 100))
        n = int(math.sqrt(i + 168))
        if (m * m) == (i + 100) and (n * n) == (i + 168):
            print(i)
            break


def question_3(date="2021-1-18"):
    i = date.split('-')
    year = int(i[0])
    month = int(i[1])
    day = int(i[2])
    print(year, month, day)
    """
    题目：输入某年某月某日，判断这一天是这一年的第几天？
    """
    if year % 4 == 0:
        j = 366
    else:
        j = 365


if __name__ == '__main__':
    question_3()