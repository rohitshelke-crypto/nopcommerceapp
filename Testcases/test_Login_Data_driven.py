'''

##Its not working


##we are performing data  driven testing on login test case.
# first we need to add excel file in our created TestData folder,we can directly copy that excel file and paste it in our TestData foldeer
##In same way we can copy and paste xlutility file and paste it in our utility folder



'''


from selenium import  webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from PageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logGen

from utilities import xlutills



class Test_002_Login_Data_driven:
    baseurl=ReadConfig.getApplicationURL()
    #path="F:\\selenium_hybrid_framework\\TestData\\signup.xlsx"
    path=".//TestData/signup.xlsx"
    logger=logGen.log_gen()

    #@pytest.mark.regression
    def test_Login_data_driven(self,setup):
        self.logger.info("*********Test_002_Login_Data_driven**********")
        self.logger.info("*********Verifying test_login data driven test**********")
        self.driver=setup
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)

        self.rows=xlutills.getRowcount(self.path,'login')   ##it will give you row of the count
        print("number of rows i in excel Five",self.rows)

        lst_status=[]   ##empty list variable,here we are creating arry ,we are string the results are here,as per the condition all the result should match if anything is fail then test cases will failed

        for r in range(2,self.rows+1):
            self.username=xlutills.readData(self.path,'login',r,1)
            self.password = xlutills.readData(self.path, 'login', r, 2)
            self.exp = xlutills.readData(self.path, 'login', r, 3)
            ##In above we are reading the exp value baeacue we need to compare ,we are performing neeative testing as well

            self.lp.setUsername(self.user)   ##whatever the username or pass will be there excel it will capture that here
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)


             ##below performing some validation by title
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"


            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Passed****")
                    self.lp.clicklogout();
                    lst_status.append("Pass")  ##passing the value is arry

                elif self.exp=='Fail':
                    self.logger.info("****Failed****")
                    self.lp.clicklogout();
                    lst_status.append("Fail")
                    ##This is one combination of validation

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****failed****")
                    self.lp.clicklogout();
                    lst_status.append("Fail")  ##passing the value is arry

                elif self.exp=='Fail':
                    self.logger.info("****Passesd****")
                    self.lp.clicklogout();
                    lst_status.append("Pass")

    ##putting validation for lst_status arry
            if "Fail" not in lst_status:
                self.logger.info("Login DDT  test is passesd")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT  test is failed")
                self.driver.close()
                assert False


        self.logger.info("End of Login data driven tstin")
        self.logger.info("  Completed Test_case_002")




















