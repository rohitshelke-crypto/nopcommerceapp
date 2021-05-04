

import time
import string
from PageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logGen
from PageObjects.AddCustomerPage import Add_customer
from PageObjects.SearchCustomerPage import Searchcustomer
import pytest


class Test_searchcustomerbyName__005:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremailL()
    password = ReadConfig.getuserpassword()
    logger = logGen.log_gen()


    @pytest.mark.regression
    def test_searchCustomerbyName(self,setup):
        self.logger.info("****Test_005_SearchcustomerbyName****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("******Staring Search customer by Name")

        self.Add_cust=Add_customer(self.driver)
        self.Add_cust.clickcustomermenu()
        self.Add_cust.clickcustomermenuItem()


        self.logger.info("******Starting Search customer by Name")

        searchcust=Searchcustomer(self.driver)
        searchcust.setFirstname("Victoria")
        searchcust.setLastname("Terces")
        searchcust.clicksearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")

        assert True==status


        self.logger.info("******Starting Search customer by Name Test case is finished")

        self.driver.close();










