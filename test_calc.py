import pytest
from pythoncode.calculator import *

class TestCal:
    '''cal测试类'''

    def setup_class(self):
        self.cal=Calculator()
        print('开始测试')
    def teardown_class(self):
        print('测试结束')
    @pytest.mark.parametrize("a,b,expect",[(2,3,5),(-1,2,1),(90000,8900,98900)],ids=["int", "minus", "bigint"])
    def test_add(self,a,b,expect):
        '''测试add方法'''
        assert expect==self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [(2, 3, -1), (-1, 2, -3), (900, 800, 100)],ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expect):
        '''测试sub'''
        assert expect==self.cal.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [(2, 3, 6), (-1, 2, -2), (900, 800, 720000)],ids=["int", "minus", "bigint"])
    def test_mul(self,a,b,expect):
        '''测试mul'''
        assert expect==self.cal.mul(a,b)

    @pytest.mark.parametrize("a,b,expect", [(8, 2, 4), (-1, 2, -0.5), (900, 90, 10)],ids=["int", "minus", "bigint"])
    def test_div(self,a,b,expect):
        '''测试div方法'''
        assert expect==self.cal.div(a,b)