import pytest
from pythoncode.calculator import *
import yaml


def get_datas_from_yaml(path):
    with open(path) as f:
        datas=yaml.safe_load(f)
        return datas

class TestCal:
    '''cal测试类'''
    path='./data.yml'
    data=get_datas_from_yaml(path)
    add_data=data['add_datas']
    sub_data=data['sub_datas']
    mul_data=data['mul_datas']
    div_data=data['div_datas']

    ids=data['myid']
    # def setup_class(self):
    #     self.cal=Calculator()
    #     print('开始测试')
    # def teardown_class(self):
    #     print('测试结束')
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b,expect",add_data,ids=ids)
    def test_add(self,a,b,expect,calu_object):
        '''测试add方法
        '''
        assert expect==calu_object.add(a,b)


    @pytest.mark.parametrize("a,b,expect",sub_data,ids=ids)
    def test_sub(self,a,b,expect,calu_object):
        '''测试sub'''
        assert expect==calu_object.sub(a,b)

    @pytest.mark.parametrize("a,b,expect",mul_data,ids=ids)
    def test_mul(self,a,b,expect,calu_object):
        '''测试mul'''
        assert expect==calu_object.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",div_data,ids=ids)
    def test_div(self,a,b,expect,calu_object):
        '''测试div方法'''
        assert expect==calu_object.div(a,b)

if __name__ == '__main__':
    path="./data.yml"
    data=get_datas_from_yaml(path)
    print(data)
    # print(data['add_datas'])
    # print(data['myid'])
