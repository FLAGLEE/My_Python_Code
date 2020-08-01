# test try
try:
    print('try...')
    r = 10 / 10
    print('result:', r)
except TypeError as e:
    print('TypeError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No Error!')
finally:
    print('finally...')
print('end try')
