
import configparser

config=configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=config.get('Common Data','baseurl')
        return url

    @staticmethod
    def getuseremailL():
        username = config.get('Common Data', 'username')
        return username

    @staticmethod
    def getuserpassword():
        password = config.get('Common Data', 'password')
        return password




