# coding=utf-8
import unittest,time,os,smtplib
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
#     ==========定义发送邮件==========
def send_mail(file_new):

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    #编写HTML类型的邮件
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('自动化测试报告','utf-8')             #邮件主题
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login('1341484113@qq.com', 'fbwvwiigseokijhi')            #登录邮箱
    s.sendmail('1341484113@qq.com', '1341484113@qq.com', msg.as_string())  #发送邮件
    s.quit()
    print('发送成功')
#     ==========查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport) :
    lists = os.listdir(testreport)                                             #生产testreport目录下的所有文件的lists列表
    lists.sort(key=lambda fn : os.path.getmtime(testreport+'\\'+fn))          #调用匿名函数对lists进行排序
    file_new = os.path.join(testreport,lists[-1])                              #拼接文件名
    return file_new

if __name__ == '__main__' :
    test_dir = './test_case'                                  #指定需要测试的路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')        #发现所有指定路径下的测试用例
    test_report = r'F:\jichu\Web测试用例\report'            #指定报告的输出路径
    now = time.strftime('%Y-%m-%d %H_%M_%S')                 #格式化时间
    filename = './report/'+ now + 'result.html'              #生成相应文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)                                           #执行测试用例
    fp.close()
    new_report = new_report(test_report)                     #调用函数找到最新的文件
    print(new_report)
    send_mail(new_report)