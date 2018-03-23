# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
msg_from = '1341484113@qq.com'
pwd = 'fbwvwiigseokijhi'
msg_to = '1341484113@qq.com'
sendfile = open(r'F:\jichu\Web测试用例\report\2018-01-27 20_48_48result.html','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="2018-01-27 20_48_48result.html"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Python email test'
msgRoot['From'] = '灰太狼抓羊的日子'
msgRoot.attach(att)
try :
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from,pwd)
    s.sendmail(msg_from,msg_to,msgRoot.as_string())
    s.quit()
    print ('发送成功')
except (s.smtplib.SMTPException, e):
    print('发送失败')