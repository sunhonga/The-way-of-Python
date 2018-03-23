# coding=utf-8
import time,xlsxwriter
class TxtLoginfo (object):
    def __init__(self,path = '',mode = 'w'):
        fname = path + time.strftime('%Y-%m-%d',time.localtime())
        self.log = open(path + fname + '.txt',mode)
     #数据初始化，在path路径下生成一个名字为当时时间的TXT的文件。
    def log_write (self ,msg) :
        self.log.write(msg)
    #对生成的TXT文件进行写操作
    def log_close(self):
        self.log.close()
    #对生成的文件关闭
class XlsLoginfo (object):
    def __init__(self,path=''):
        fname = path + time.strftime('%Y-%m-%d', time.localtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(fname+'.xls')
    def xl_write(self,*args):
        col = 0
        for val in args :
            self.sheet.write_string(self.row,col,val)
            col += 1
        self.row += 1
    def log_init(self,sheetname,*title):
        self.sheet = self.xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E',30)
        self.xl_write(*title)
    def log_write(self,*args):
        self.xl_write(*args)
    def log_close(self):
        self.xl.close()
if __name__ == '__main__':
    log = TxtLoginfo()
    log.log_write('test Loginfo 测试')
    log.log_close()
    xlinfo=XlsLoginfo()
    xlinfo.log_init('test','uname','pwd','result','info')
    xlinfo.log_close()