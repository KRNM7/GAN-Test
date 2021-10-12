import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from helper.sign_up_profile_info import *
from helper.test_helper import *


class GanAutomationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_missing_dob(self):
        self.driver.get("https://moneygaming.qa.gameaccount.com/") 
        self.run_registration_flow(full_sign_up_profile_info) 

        missing_dob_flag = wait_for_element(self.driver, By.XPATH, "//label[@class='error' and(@for='dob')]")
        self.assertEqual(missing_dob_flag.text, "This field is required")


    def run_registration_flow(self, profile_info):
        self.driver.get("https://moneygaming.qa.gameaccount.com/")

        sign_up_button = wait_for_located_element(self.driver, By.CLASS_NAME, "newUser")
        sign_up_button.click()
        
        user_title = wait_for_located_element(self.driver, By.CLASS_NAME, "title")
        user_title.click()

        user_title_drop = Select(wait_for_located_element(self.driver, By.CLASS_NAME, "title"))
        user_title_drop.select_by_value('Ms')

        first_name_field_id = "map(firstName)"
        first_name_field =  wait_for_element(self.driver, By.NAME, first_name_field_id)
        first_name_field.click()
        first_name_field.send_keys(profile_info[first_name_field_id])

        surname_field_id = "map(lastName)"
        profile_info[first_name_field_id]
        surname_field = wait_for_element(self.driver, By.NAME, surname_field_id)
        surname_field.click()
        surname_field.send_keys(profile_info[surname_field_id])

        email_field_id = "map(email)"
        email_field =  wait_for_element(self.driver, By.NAME, email_field_id)
        email_field.send_keys(profile_info[email_field_id])

        telephone_field_id = "map(phone)"
        telephone_field = wait_for_element(self.driver, By.NAME, telephone_field_id)
        telephone_field.send_keys(profile_info[telephone_field_id])

        mobile_field_id = "map(mobile)"
        mobile_field = wait_for_element(self.driver, By.NAME, mobile_field_id)
        mobile_field.send_keys(profile_info[mobile_field_id])

        address_1_field_id = "map(address1)"
        address_1_field = wait_for_element(self.driver, By.NAME, address_1_field_id)
        address_1_field.send_keys(profile_info[address_1_field_id])

        address_2_field_id = "map(address2)"
        address_2_field = wait_for_element(self.driver, By.NAME, address_2_field_id)
        address_2_field.send_keys(profile_info[address_2_field_id])

        city_field_id = "map(addressCity)"
        city_field = wait_for_element(self.driver, By.NAME, city_field_id)
        city_field.send_keys(profile_info[city_field_id])

        county_field_id = "map(stateProv)"
        county_field = wait_for_element(self.driver, By.NAME, county_field_id)
        county_field.send_keys(profile_info[county_field_id])

        postcode_field_id = "map(postCode)"
        postcode_field = wait_for_element(self.driver, By.NAME, postcode_field_id)
        postcode_field.send_keys(profile_info[postcode_field_id])

        country_field_id = "countryList"
        country_field = wait_for_element(self.driver, By.ID, country_field_id)
        country_field.send_keys(profile_info[country_field_id])

        username_field_id = "map(userName)"
        username_field = wait_for_element(self.driver, By.NAME, username_field_id)
        username_field.send_keys(profile_info[username_field_id])

        password_field_id = "password"
        password_field = wait_for_element(self.driver, By.ID, password_field_id)
        password_field.send_keys(profile_info[password_field_id])

        confirm_password_field_id = "map(passwordConfirm)"
        confirm_password_field = wait_for_element(self.driver, By.NAME, confirm_password_field_id)
        confirm_password_field.send_keys(profile_info[confirm_password_field_id])

        security_question_1_dropdown_id = "map(securityQuestionOne)"
        security_question_1_dropdown = Select(wait_for_element(self.driver, By.NAME, security_question_1_dropdown_id))
        security_question_1_dropdown.select_by_value(profile_info[security_question_1_dropdown_id])

        security_answer_field_id = "map(securityAnswerOne)"
        security_answer_field = wait_for_element(self.driver, By.NAME, security_answer_field_id)
        security_answer_field.send_keys(profile_info[security_answer_field_id])

        ## Scroll down ###
        
        target = self.driver.find_element_by_link_text('Contact Us')
        target.location_once_scrolled_into_view

        security_question_2_dropdown_id = "map(securityQuestionTwo)"
        security_question_2_dropdown = Select(wait_for_element(self.driver, By.NAME, security_question_2_dropdown_id))
        security_question_2_dropdown.select_by_value(profile_info [security_question_2_dropdown_id])     

        security_answer_2_field_id = "map(securityAnswerTwo)"
        security_answer_2_field = wait_for_element(self.driver, By.NAME, security_answer_2_field_id)
        security_answer_2_field.send_keys(profile_info[security_answer_2_field_id])

        currency_dropdown_id = "map(currency)"
        currency_dropdown = Select(wait_for_element(self.driver, By.NAME, currency_dropdown_id))
        currency_dropdown.select_by_value(profile_info[currency_dropdown_id])  

        uncheck_phone_marketing_id = "map(marketingPhone)"
        uncheck_phone_marketing = wait_for_element(self.driver, By.NAME, uncheck_phone_marketing_id)
        uncheck_phone_marketing.click()

        terms_checkbox = wait_for_element(self.driver, By.NAME, "map(terms)")
        terms_checkbox.click()

        submit_button = wait_for_element(self.driver, By.CLASS_NAME, "promoReg")
        submit_button.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
