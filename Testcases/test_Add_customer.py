

#pytest -v -s F:\selenium_hybrid_framework\Testcases\test_Add_customer.py --browser chrome --html=F:\selenium_hybrid_framework\Reports\Add_New_cust.html
#use this command it will create html file also and if test case is got failed then it ll save the screenshot as well



from selenium import  webdriver
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import string
import random
from PageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logGen
from PageObjects.AddCustomerPage import Add_customer
from PageObjects.LoginPage import LoginPage
import time



class Test_003_AddCustomer:
    baseurl=ReadConfig.getApplicationURL()
    usernamew=ReadConfig.getuseremailL()
    passord=ReadConfig.getuserpassword()
    logger=logGen.log_gen()


    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("****Test_003_Addcustomer****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.usernamew)
        self.lp.setPassword(self.passord)
        self.lp.clicklogin()


        self.addcust = Add_customer(self.driver)

        self.addcust.clickcustomermenu()

        self.addcust.clickcustomermenuItem()


        self.addcust.Add_new()

        self.email = random_generator() + "@gmail.com"  ##creating a random data,the method has given below
        self.addcust.setEmail(self.email)

        self.addcust.setPassword('12345')

        self.firstname = random_generator()
        self.addcust.setFirstname(self.firstname)

       # self.addcust.setFirstname('rohit')
        self.addcust.setLastname('shelke')
        self.addcust.setDOB("2/05/1995")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("cattleya")
        self.addcust.setAdmincontent("gshvghs")
        #self.addcust.setDropdownVendor('Vendor 2')

        self.addcust.clickbtnsave()

        self.logger.info("******Add customer validaion started*****")

        ##below method it will capture everything on the page and it will convert it into text and will save it in variable self.msg
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "The new customer has been added successfully" in self.msg:  ##checking "The new customer has been added successfully" this line is present in variable called self .msg
            assert True == True
            print("Add custmeter test is passed")
            self.logger.info("Add custmeter test is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_sc2.png")
            self.logger.info("Add custmeter test is failed")
            assert True == False

        self.driver.close()
        self.logger.info("****end of test_add_customer test case")


#For creating random data we need to use this method
def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))








