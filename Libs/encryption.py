import hashlib


class Encrypt:
    def __init__(self):
        self.md5_obj1 = hashlib.md5()
        self.md5_obj2 = hashlib.md5()
        self.sha1_obj = hashlib.sha1()

    def md5(self, pwd, salt):
        """
        :param pwd: 密码
        :param salt: 密码盐
        :return: md5(md5(pwd).salt)
        """
        self.md5_obj1.update(pwd.encode(encoding='utf-8'))
        first = self.md5_obj1.hexdigest()
        self.md5_obj2.update((first + salt).encode(encoding='utf-8'))
        second = self.md5_obj2.hexdigest()
        print(second)
        return second

    def sha1(self, *args):
        """
        1、检查timestamp 与系统时间是否相差在合理时间内，如10分钟。
        2、将appSecret、timestamp、nonce三个参数进行字典序排序
        3、将三个参数字符串拼接成一个字符串进行SHA1加密
        4、加密后的字符串可与signature对比，若匹配则标识该次请求来源于某应用端，请求是合法的。
        :return: SHA1(params)
        """
        result = ''
        for key in args:
            result += key
        print(result)
        self.sha1_obj.update(result.encode('utf-8'))
        result = self.sha1_obj.hexdigest()
        print(result)
        return result


if __name__ == '__main__':
    a = Encrypt()
    a.md5('bbbbbb', '56b4d6')
    a.sha1('abcdef', '123', '321')
