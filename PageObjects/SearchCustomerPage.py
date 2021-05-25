import pytest
from selenium import webdriver

class Searchcustomer:

    txt_email_ID = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    table_search_xpath = "//table[@role='grid']"


    table_xpath="""/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div"""
    #table_xpath_Sir = "//table[@id='customers-grid']"
    #table_xpath ="""//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]"""
    table_Row_xpath = "//table[@id='customers-grid']//tbody/tr"

    table_coloumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txt_email_ID).clear()
        self.driver.find_element_by_id(self.txt_email_ID).send_keys(email)

    def setFirstname(self, fname):
        self.driver.find_element_by_id(self.txt_firstname_id).clear()
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(fname)

    def setLastname(self, Lname):
        self.driver.find_element_by_id(self.txt_lastname_id).clear()
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(Lname)

    def clicksearch(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def getNoofRow(self):
        return len(self.driver.find_elements_by_xpath(self.table_Row_xpath))

    ##here length method will find how many rows we have
    ##here length method will find how many coloumns we have and it will return
    def getNoofColoumn(self):
        return len(self.driver.find_elements_by_xpath(self.table_coloumn_xpath))


    def searchCustomerByEmail(self,email):  ##This point it will pass email id  to this method
        flag = False   ##its a initial variable ,if we found record in table then flag value will be true else its false
        for r in range(1,self.getNoofRow()+ 1):   ##here we are counting the number of rows ,whrereven its exactly present ,means will start from 1 and getNoofRow +1 means it will take till last row
            table = self.driver.find_element_by_xpath(self.table_xpath)  ##if above condition is true then it will come here,here we have given table xpath
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r)+"]/td[2]").text  ##putting that xpath in emailid variable and we are giving the xpath of the element ,"+ str(r)+" it means row number and "/td[2]" it means coloumn number ,because our email is present in second coloumn ,so second coloumn will be same but rownumber will keep changing and the above using for loop we have mentioned method is there getNoofRows+1 means it will check every row .
##means in in simple word we have created one variable called email id then we are putting table xptah in that variable means (table = self.driver.find_element_by_xpath(self.table_xpath)) then we are giving xpath of getNoOfrows "/table[@id='customers-grid']/tbody/tr"  and this means /td[2] its coloumn 2
            if emailid == email:  ## In this validation whatever the emailid we are capturing that will match with email or not ,that email we will specify
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getNoofRow() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r)+"]/td[3]").text
            if name == Name:   ##if we got the email id then flag value will be true and it will return the flag nad suppose if we not get that email id then flag value will be false
                flag = True
                break
        return flag















