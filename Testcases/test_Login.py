from selenium import  webdriver
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



from PageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logGen




class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getuseremailL()
    password=ReadConfig.getuserpassword()

    logger=logGen.log_gen()

    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("*********Test_001_Login********")
        self.logger.info("*********Verifying Home page title**********")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title


        if act_title=='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("******Home page title test is passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle1.png")
            self.driver.close()
            self.logger.error("******Home page title test is failed*******")
            assert  False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("*********Verifying test_login**********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info("******Login  test is passed*******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login1.png")
            self.driver.close()
            self.logger.error("******Login  title test is failed*******")
            assert False
            self.driver.close()
            


