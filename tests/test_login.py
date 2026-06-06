from locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC

from urls import MAIN_URL, REGISTER_URL, FORGOT_URL


def test_login_via_enter_in_account_button(driver, wait, registered_user):
    driver.get(MAIN_URL)
    wait.until(EC.visibility_of_element_located(SL.ENTER_IN_ACC_BUTTON))
    driver.find_element(*SL.ENTER_IN_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(registered_user['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(registered_user['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

def test_login_via_personal_account_button(driver, wait, registered_user):
    driver.get(MAIN_URL)
    wait.until(EC.visibility_of_element_located(SL.PER_ACC_BUTTON))
    driver.find_element(*SL.PER_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(registered_user['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(registered_user['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

def test_login_via_registration_form(driver, wait, registered_user):
    driver.get(REGISTER_URL)
    wait.until(EC.visibility_of_element_located(SL.ENTER_LINK))
    driver.find_element(*SL.ENTER_LINK).click()
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(registered_user['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(registered_user['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

def test_login_via_password_recovery_form(driver, wait, registered_user):
    driver.get(FORGOT_URL)
    wait.until(EC.visibility_of_element_located(SL.PASS_ENTER_LINK))
    driver.find_element(*SL.PASS_ENTER_LINK).click()
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(registered_user['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(registered_user['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

