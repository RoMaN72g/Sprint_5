from locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_personal_account(driver, wait, account_user):
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    driver.find_element(*SL.PER_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.LOGOUT_BTN))
    assert "/profile" in driver.current_url

def test_switch_to_constructor_with_constructor_link(driver, wait, account_user):
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    driver.find_element(*SL.PER_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.LOGOUT_BTN))
    driver.find_element(*SL.CONSTRUCTOR_LINK).click()
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

def test_switch_to_constructor_with_logo_link(driver, wait, account_user):
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    driver.find_element(*SL.PER_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.LOGOUT_BTN))
    driver.find_element(*SL.LOGO_SB).click()
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    assert driver.find_element(*SL.ORDER_BTN).is_displayed()

def test_logout_from_account(driver, wait, account_user):
    wait.until(EC.visibility_of_element_located(SL.ORDER_BTN))
    driver.find_element(*SL.PER_ACC_BUTTON).click()
    wait.until(EC.visibility_of_element_located(SL.LOGOUT_BTN))
    driver.find_element(*SL.LOGOUT_BTN).click()
    wait.until(EC.visibility_of_element_located(SL.ENTER_ACC_BTN))
    assert driver.find_element(*SL.ENTER_ACC_BTN).is_displayed()










