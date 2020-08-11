# 正则表达式
import re


# someone@gmail.com
# bill.gates@microsoft.com
def is_valid_email(addr):
    if re.match(r'^[0-9a-zA-Z\.]+@[0-9a-zA-Z\.]+?(.com)$', addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
def name_of_email(addr):
    g = re.match(r'\<?([\w\s]+)\>?\s*(\w*)@([0-9a-zA-Z\.]+)$', addr)
    if g:
        return g.group(1)
    else:
        return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
