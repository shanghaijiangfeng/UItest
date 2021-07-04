#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        #获取当前路径
        case_path = os.path.join(os.getcwd())
        #添加路径到suite，case名称，匹配所有前缀是unittest的case
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        #用例添加进run
        unittest.TextTestRunner().run(suite)
        

if __name__ == '__main__':
    unittest.main()
