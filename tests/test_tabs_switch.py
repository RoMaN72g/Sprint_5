from locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_URL

def test_switch_to_sauce_tab(driver, wait):
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(SL.SAUCE_TAB)).click()
    assert wait.until(EC.visibility_of_element_located(SL.ACTIVE_SAUCE_TAB))


def test_switch_to_filling_tab(driver, wait):
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(SL.FILLING_TAB)).click()
    assert wait.until(EC.visibility_of_element_located(SL.ACTIVE_FILLING_TAB))


def test_switch_to_bun_tab(driver, wait):
    driver.get(MAIN_URL)
    wait.until(EC.element_to_be_clickable(SL.SAUCE_TAB)).click()
    wait.until(EC.visibility_of_element_located(SL.ACTIVE_SAUCE_TAB))
    wait.until(EC.element_to_be_clickable(SL.BUN_TAB)).click()
    assert wait.until(EC.visibility_of_element_located(SL.ACTIVE_BUN_TAB))










