from selenium import  webdriver

class LoginPage:
    testbox_username_id='Email'
    testbox_passwrd_id='Password'
    button_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_linktext='Logout'



    def __init__(self,driver):
        self.driver=driver


    def setUsername(self,username):
        self.driver.find_element_by_id(self.testbox_username_id).clear()
        self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element_by_id(self.testbox_passwrd_id).clear()
        self.driver.find_element_by_id(self.testbox_passwrd_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.Logout).click()