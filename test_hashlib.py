# 根据用户输入的口令，计算出存储在数据库中的MD5口令
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
import hashlib


def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    for k, v in db.items():
        if k == user:
            if v == md5.hexdigest():
                return True


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
