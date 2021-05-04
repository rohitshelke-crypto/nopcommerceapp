
import time
import string
from PageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logGen
from PageObjects.AddCustomerPage import Add_customer
from PageObjects.SearchCustomerPage import Searchcustomer
import pytest


class Test_searchcustomerbyEmail__004:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremailL()
    password = ReadConfig.getuserpassword()
    logger = logGen.log_gen()

    @pytest.mark.regression
    def test_searchCustomerbyemail(self,setup):

        self.logger.info("****Test_004_SearchcustomerbyEmail****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("******Staring Search customer by Email")

        self.Add_cust=Add_customer(self.driver)
        self.Add_cust.clickcustomermenu()
        self.Add_cust.clickcustomermenuItem()


        self.logger.info("******Starting Search customer by Email")

        searchcust=Searchcustomer(self.driver)
        searchcust.setEmail("james_pan@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("james_pan@nopCommerce.com")

        assert True==status


        self.logger.info("******Starting Search customer by Email Test case is finished")

        time.sleep(5)

        self.driver.close();










