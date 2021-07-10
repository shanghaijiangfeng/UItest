#coding=utf-8
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import codecs
import pandas as pd
import sys
import os
basepath=os.getcwd()
sys.path.append(basepath)


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()       
        handle_excel = ExcelUtil(basepath+'\\config\\keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                except_result_method2 = handle_excel.get_col_value(i, 7)
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i,8)
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i,5)
                    handle_value = handle_excel.get_col_value(i,6)
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    elif except_result_method2 == '':
                        handle_excel.write_value(i, 'pass')
                    else:
                        print('预期结果为空')


        xd = pd.ExcelFile(basepath+'\\config\\keyword.xls')
        pd.set_option('display.max_colwidth', 1000)  # 设置列的宽度，以防止出现省略号
        df = xd.parse()
        with codecs.open(basepath+'\\config\\keyword.html','w') as html_file:
            html_file.write(df.to_html(header=True, index=False))


                        
    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        if send_value == '' and handle_value !='':
            result = method_value(handle_value)
        elif send_value == '' and handle_value =='':
            result = method_value()
        elif send_value != '' and handle_value =='':
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result

if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()