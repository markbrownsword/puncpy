from puncpy.apostrophe import Apostrophe


apostrophe = Apostrophe()
result = apostrophe.execute('It\'s getting harder')
if len(result) > 0:
    print('Success')
else:
    print('Fail')
