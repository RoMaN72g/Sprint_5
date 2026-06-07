from locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC
from urls import REGISTER_URL

def test_registration_via_personal_account(driver, user_data, wait):
    driver.get(REGISTER_URL)
    wait.until(EC.visibility_of_element_located(SL.INPUT_NAME))
    driver.find_element(*SL.INPUT_NAME).send_keys(user_data['name'])
    driver.find_element(*SL.INPUT_EMAIL).send_keys(user_data['email'])
    driver.find_element(*SL.INPUT_PASS).send_keys(user_data['password'])
    driver.find_element(*SL.REGISTER_BTN).click()
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(user_data['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(user_data['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    assert wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))


def test_registration_short_password_error(driver, user_data, wait):
    driver.get(REGISTER_URL)
    wait.until(EC.visibility_of_element_located(SL.INPUT_NAME))
    driver.find_element(*SL.INPUT_NAME).send_keys(user_data['name'])
    driver.find_element(*SL.INPUT_EMAIL).send_keys(user_data['email'])
    driver.find_element(*SL.INPUT_PASS).send_keys('qaz12')
    driver.find_element(*SL.INPUT_NAME).click()
    assert wait.until(EC.visibility_of_element_located(SL.ERROR_PASS))


