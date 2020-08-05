# test log
import logging
logging.basicConfig(level=logging.INFO)

# try:
#     print('try...')
#     r = 10 / 10
#     print('result:', r)
# except TypeError as e:
#     print('TypeError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('No Error!')
# finally:
#     print('finally...')
# print('end try')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

