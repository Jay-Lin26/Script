from random import randint


# 随机生成手机号码
def random_phone_number():
    _head = ['130', '133', '135', '150', '170']
    _body = ''
    for i in range(8):
        _body = str(randint(0, 9)) + _body
    phone = _head[randint(0, 4)] + _body
    return phone


