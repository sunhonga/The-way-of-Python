# coding=utf-8
import xlrd
def get_webinfo(path):
    webinfo={}
    with open(path,'r',encoding='gbk') as f :
        for line in f.readlines() :
            result = line.strip().split('=')
            webinfo.update(dict([result]))
    return webinfo
class TxtUserinfo(object):
    def __init__(self,path = ''):
        self.path =  path
    def get_userinfo(self):
        userinfo=[]
        dict1 = {}
        with open(self.path,'r',encoding='gbk') as f :
            for line in f.readlines() :
                result = line.strip().split(' ')
                for i in result :
                    re=i.split('=')
                    dict1.update(dict([re]))
                userinfo.append(dict1)
        return  userinfo
class XLUserinfo(object):
    def __init__(self,path = ''):
        self.xl=xlrd.open_workbook(path)
    #数据初始化，对象的xl为一个xl的文件
    def get_sheet_info(self):
        listkey = ['uname','pwd']
        infolist = []
        for row in range (1,self.sheet.nrows):
            info = self.sheet.row_values(row)
            tmp = zip(listkey,info)
            infolist.append(dict(tmp))
        return infolist
    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()
    def get_sheetinfo_by_index(self,index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()
if __name__ == '__main__':
    webinfo=get_webinfo(r'F:\jichu\软件测试\麦子学院测试\webinfo.txt')
    print(webinfo)
    #获取txt里面的用户数据
    #userinfo = get_userinfo(r'F:\jichu\软件测试\麦子学院测试\userinfo.txt')
    txtuserinfo = TxtUserinfo(r'F:\jichu\软件测试\麦子学院测试\userinfo.txt')
    userinfo = txtuserinfo.get_userinfo()
    print(userinfo)
    #获取xls的用户数据
    xinfo = XLUserinfo(r'F:\jichu\软件测试\麦子学院测试\userinfo.xls')
    info = xinfo.get_sheetinfo_by_index(0)
    print(info)
    info1 = xinfo.get_sheetinfo_by_name('Sheet1')
    print(info1)