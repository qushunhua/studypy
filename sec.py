import pytest



class Test1:
    def test_one(self):
        x="this"
        assert 'h' in x
if __name__ == '__main__':
    pytest.main('-q ')