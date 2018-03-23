# coding=utf-8
import requests
form_data = {
    'phone':'asdf',
    'password':'adsf',
    'oneMonth':1
    }
reponse = requests.post(url='http://dig.chouti.com/login',data=form_data)
print(reponse.text)
requests.get()