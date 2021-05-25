

##This method if you want to execute the test with only specific broswser

from selenium import  webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
        driver=webdriver.Chrome(executable_path="G:\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.implicitly_wait(10)
        return driver




##In this method if you want to execute test cases with your desired browser ,you can give here multiple browsers and run your code
##use command pytest -v -s F:\selenium_hybrid_framework\Testcases\test_Login.py --browser chrome
# or pytest -v -s F:\selenium_hybrid_framework\Testcases\test_Login.py --browser firefox


'''
from selenium import  webdriver
import pytest
#from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="G:\\Downloads\\chromedriver_win32\\chromedriver.exe")
        print('launchng chrome browser.....')

    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="G:\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe")
        print('launching firefox driver.....')

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
'''

'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=['chrome','firefox'],scope='class')   ##defining two browser using param
def init_driver(request):
    if request.param=='chrome':
        web_driver=webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver = web_driver


    if request.param=='firefox':
        web_driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver=web_driver
    yield
    web_driver.close()


'''
##########Creating Pytest HTML Report ##############
##saving that HTML report in report folder that we created

##use this command while executing :
#pytest -v -s -n 2 --html=F:\selenium_hybrid_framework\Reports\report_new.html F:\selenium_hybrid_framework\Testcases\test_Login.py --browser chrome
##check the report in your created Reports folder,you ll get the html file



'''

from selenium import webdriver
import pytest

def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module name']='Customers'
    config._metadata['Tester']='Rohit'

## It is hook for delete/modify Enviroment info to HTML report###
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)


'''
'''


from selenium import webdriver
import pytest

def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module name']='Add_New_Customer'
    config._metadata['Tester']='Rohit'

## It is hook for delete/modify Enviroment info to HTML report###
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)




'''

