# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
#发送邮箱用户/密码
msg_from = '1341484113@qq.com'
password = 'fbwvwiigseokijhi'
msg_to = '1341484113@qq.com'
#编写HTML类型的邮件正文（email构成邮件内容）
msg = MIMEText('<html><h1>马爷你好！<h1></html>','html','utf-8') #正文
msg['Subject'] = Header('Pyhton email test','utf-8')  #主题
msg['To'] = '马大帅'
msg['From'] = '灰太狼抓羊的日子'
#smtplib来发送邮件
try:
  s = smtplib.SMTP_SSL("smtp.qq.com", 465)
  #s.set_debuglevel(1)
  s.login(msg_from, password)
  s.sendmail(msg_from, msg_to, msg.as_string())
  s.quit()
  print ("发送成功")
except (s.smtplib.SMTPException, e):
  print ("发送失败")