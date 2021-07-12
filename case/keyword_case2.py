# coding=utf-8
import unittest

import HTMLTestRunner
import ddt
import self
from selenium import webdriver

from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod, action_method
import codecs
import pandas as pd
import sys
import os
basepath = os.getcwd()
sys.path.append(basepath)
data = ExcelUtil(basepath + '\\config\\keyword.xls').get_data()
cs=ExcelUtil(basepath + '\\config\\keyword.xls').get_lines()
writb=ExcelUtil(basepath + '\\config\\keyword.xls')

@ddt.ddt
class TestKeywordCase(unittest.TestCase):

    @ddt.data(*data)
    def test_run_main(self,data):

        caseid=data[0]

        is_run = data[3]
        if is_run == 'yes':
            "预期结果(调用方法)"
            except_result_method = data[7]
            "实际结果"
            except_result = data[8]
            "调用执行方法"
            method = data[4]
            "输入的数据"
            send_value = data[5]
            "操作的元素名称"
            handle_value = data[6]

            action_method.run_method(method, send_value, handle_value)
            if except_result != '':
                except_value = action_method.get_except_result_value(except_result)
                if except_value[0] == 'text':
                    result = action_method.run_method(except_result_method)
                    if except_value[1] in result:
                        writb.write_value(i, 'pass')
                    else:
                        writb.write_value(i, 'fail')
                elif except_value[0] == 'element':
                    result = action_method.run_method(except_result_method, except_value[1])
                    if result:
                        writb.write_value(i, 'pass')
                    else:
                        writb.write_value(i, 'fail')
                else:
                    print("没有else")
            else:
                print('预期结果为空')


if __name__ == '__main__':
    case_path = basepath + "/case"
    report_path = basepath + "/report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="keyword_case2.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Mushishi", description="this is test")
        runner.run(discover)