# coding=utf-8
from suds.client import Client
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
result = client.service.getMoblieCodeInfo(18215543902)
print(client)