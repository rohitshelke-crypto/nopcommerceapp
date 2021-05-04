import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class Add_customer:

    lnk_customer_menu_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    lnk_customer_menu_item_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    clk_button_addnew_xpath = """/html/body/div[3]/div[1]/form[1]/div/div/a"""

    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    Rd_gander_male_id = "Gender_Male"
    Rd_gander_female_id = "Gender_Female"
    txt_dateofbirth_xpath = "//input[@id='DateOfBirth']"
    txt_comanyname_xpath = "//input[@id='Company']"
    txt_admincpmment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    #drop_down_vendor_xpath = """/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[2]/select"""

    #drop_down_vendor_xpath_vendor2="// option[contains(text(), 'Vendor 2')]"



    def __init__(self,driver):
        self.driver=driver

    def clickcustomermenu(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menu_xpath).click()

    def clickcustomermenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menu_item_xpath).click()

    def Add_new(self):
        self.driver.find_element_by_xpath(self.clk_button_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.Rd_gander_male_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.Rd_gander_female_id).click()
        else:
            self.driver.find_element_by_id(self.Rd_gander_male_id).click()

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def setDOB(self, dateofbirth):
        self.driver.find_element_by_xpath(self.txt_dateofbirth_xpath).send_keys(dateofbirth)

    def setCompanyName(self, C_name):
        self.driver.find_element_by_xpath(self.txt_comanyname_xpath).send_keys(C_name)

    def setAdmincontent(self, A_content):
        self.driver.find_element_by_xpath(self.txt_admincpmment_xpath).send_keys(A_content)

    def clickbtnsave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    #def setDropdownVendor(self,value):
        #self.drp=Select(self.driver.find_element_by_xpath(self.drop_down_vendor).click())
        #self.drp.select_by_visible_text(value)


























