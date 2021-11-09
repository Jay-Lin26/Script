# encoding = utf-8

def bank_card_verify(card_number):
    number = list(card_number)      # 将字符串转为列表
    card_len = len(number) % 2      # 取模
    """
    卡号位数为 偶数 的；第一位的权重就是2,第二位是1,一次下去就是2,1,2,1,2,1...
    卡号位数为 奇数 的；第一位的权重就是1,第二位是2,依次下去就是1,2,1,2,1,2...
    卡号的总体分值计算：
        当前位置的卡号*权重值；
        结果如果大于9,则减去9；
        最终将所有位的分值叠加起来就是总分值
    总分值%10 得到结果为0则是正确的，不为0则是错误的卡号
    """
    num = 0     # 计算后的总和
    index = 0   # 列表当前位置
    if card_len == 0:   # 偶数
        for j in list(number):  # 遍历数组
            index += 1
            if index % 2 == 0:  # 当前位数是偶数，则 j * 1
                num += int(j) * 1
            else:  # 当前位数是奇数，则 j * 2
                if int(j) * 2 > 9:  # 结果如果大于9,则减去9
                    num += int(j) * 2 - 9
                else:
                    num += int(j) * 2
        if num % 10 == 0:
            print("卡号正确")
        else:
            print("卡号错误")
    else:                # 奇数
        for j in list(number):  # 遍历数组
            index += 1
            if index % 2 == 0:  # 当前位数是偶数，则 j * 2
                if int(j) * 2 > 9:  # 结果如果大于9,则减去9
                    num += int(j) * 2 - 9
                else:
                    num += int(j) * 2
            else:  # 当前位数是奇数，则 j * 1
                num += int(j) * 1
        if num % 10 == 0:
            print("卡号正确")
        else:
            print("卡号错误")


if __name__ == '__main__':
    bank_card_verify('1111110100000000')
