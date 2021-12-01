# coding = utf-8
from random import randint

number = randint(0, 1000)

if number == 1:
    print('一等奖')
elif number == 2:
    print('二等奖')
elif number == 3:
    print('三等奖')
else:
    print('四等奖')