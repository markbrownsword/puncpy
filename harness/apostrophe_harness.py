from puncpy.apostrophe import Apostrophe


apostrophe = Apostrophe()
result = apostrophe.execute('Test!')
if len(result) > 0:
    print('Success')
else:
    print('Fail')
