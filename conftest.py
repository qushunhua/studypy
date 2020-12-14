import pytest
from pythoncode.calculator import Calculator

@pytest.fixture(scope='module')
def calu_object():
    calu=Calculator()
    print('测试开始，睁大眼')
    yield calu
    print('测试结束，清理数据')





def get_token(username,password):
    pass