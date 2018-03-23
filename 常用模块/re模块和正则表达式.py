import re
'''
re.match('h','hello python')   match是从头开始匹配，匹配到就有返回，没匹配到无返回。通过
re.match('.','hello python')        .group()获得返回值 
re.match('[hH]','Hello python')
re.match('no.[0-9]','no.1 python')
re.match('no.\d','hello python') 
pytho中字符串前面加上r表示原生字符串，正则表达式里使用"\"作为转义字符，假如你需要匹配文本中的字符"\"
那么使用正则表达式你将需要四个反斜杠"\\\\",前面两个和后面两个分别用于编程语言里转义成反斜杠，转换成
两个反斜杠后在在正则表达式里转义成一个反斜杠。python里的原生字符串很好地解决了这个问题。
re.match("c:\\\\a","c:\\a\\b\\c").group() 结果c:\a
re.match(r"c:\\a","c:\\a\\b\\c").group()  结果c:\a
re.search('\d+','阅读次数为999，评论次数为888').group()  结果为'999'search只匹配一次就返回
re.findall ('\d+','阅读次数为999，评论次数为888').group()  结果为['999','888']findall匹配所有并返回一个列表
re.sub('\d+','777','阅读次数为999，评论次数为888').group() 结果为阅读次数为777，评论次数为777
re.split(':| ','info:aaa bbb:ccc').group() 结果为['info','aaa','bbb','ccc']
'''
def phonemuber(a):
    if len(a) !=11:
        return False
    if not str.isdigit(a):
        return False
    if a[:3] not in ['135','138','187']:
        return  False
    return  True
print(phonemuber("135155"))
print(phonemuber("1351234abcd"))
print(phonemuber("13615545678"))
print(phonemuber("13523415515"))
# print(str.isdigit('45564'))
# print(str.isdigit('asdas'))
# print(str.isdigit('4sd234'))
print(re.match("c:\\\\a","c:\\a\\b\\c").group())
print(re.match(r"c:\\a","c:\\a\\b\\c").group())