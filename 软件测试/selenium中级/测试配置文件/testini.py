# coding=utf-8
import configparser
import os
class TestReadConfigFile(object) :
    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))#获取项目根目录的相对路径
        print(root_dir)
        config = configparser.ConfigParser()
        file_path = root_dir + '/config/config.ini'
        config.read(file_path)
        browser = config.get('browserType','browserName')
        url = config.get ('testServer','url')
        return browser,url
trcf = TestReadConfigFile()
print(trcf.get_value())

