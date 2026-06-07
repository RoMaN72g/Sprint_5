import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from generators import generate_email, generate_password
from locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC
from urls import LOGIN_URL, REGISTER_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    email = generate_email()
    password = generate_password()
    name = 'Роман'
    return {'email': email, 'password': password, 'name': name}

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def registered_user(driver, user_data, wait):
    driver.get(REGISTER_URL)
    wait.until(EC.visibility_of_element_located(SL.INPUT_NAME))
    driver.find_element(*SL.INPUT_NAME).send_keys(user_data['name'])
    driver.find_element(*SL.INPUT_EMAIL).send_keys(user_data['email'])
    driver.find_element(*SL.INPUT_PASS).send_keys(user_data['password'])
    driver.find_element(*SL.REGISTER_BTN).click()
    return user_data

@pytest.fixture
def account_user(driver,registered_user,wait):
    driver.get(LOGIN_URL)
    wait.until(EC.visibility_of_element_located(SL.INPUT_EMAIL_ACC))
    driver.find_element(*SL.INPUT_EMAIL_ACC).send_keys(registered_user['email'])
    driver.find_element(*SL.INPUT_PASS_ACC).send_keys(registered_user['password'])
    driver.find_element(*SL.ENTER_ACC_BTN).click()
    return registered_user





