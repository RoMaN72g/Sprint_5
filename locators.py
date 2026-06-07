from selenium.webdriver.common.by import By
class StellarLocators:


    # Гиперссылка 'Личный Кабинет' переводит в личный кабинет или к форме входа в аккаунт.
    PER_ACC_BUTTON = (By.XPATH, "//a[@href='/account']")

    # Кнопка 'Войти в аккаунт' переводит к форме входа в аккаунт.
    ENTER_IN_ACC_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Форма входа в аккаунт.
    # Поле ввода 'Email'.
    INPUT_EMAIL_ACC = (By.CSS_SELECTOR, "input[name='name']")

    # Поле ввода 'Пароль'.
    INPUT_PASS_ACC = (By.CSS_SELECTOR, "input[name='Пароль']")

    # Кнопка 'Войти'.
    ENTER_ACC_BTN = (By.XPATH, "//button[contains(@class, 'type_primary')]")

    # Гиперссылка 'Зарегистрироваться' переводит к форме регистрации.
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

    # Гиперссылка 'Восстановить пароль' переаодит к форме востановления пароля.
    RECOVER_PASS = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Форма регистрации.
    # Поле ввода "Имя".
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Поле ввода 'Email'.
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле ввода "Пароль".
    INPUT_PASS = (By.CSS_SELECTOR, "input[name='Пароль']")

    # Кнопка "Зарегистрироваться".
    REGISTER_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Гиперссылка "Войти", переводит к форме входа в аккаунт.
    ENTER_LINK = (By.XPATH, "//a[text()='Войти']")

    # Текст ошибки при вводе некорректного пароля.
    ERROR_PASS = (By.XPATH, "//div[contains(@class, 'error')]")

    # Разделы конструктора.
    # Раздел "Булки".
    BUN_TAB = (By.XPATH, "//div[span[text()='Булки']]")
    # Активный раздел "Булки".
    ACTIVE_BUN_TAB = (By.XPATH, "//div[contains(@class, 'current') and span[text()='Булки']]")

    # Раздел "Соусы".
    SAUCE_TAB = (By.XPATH, "//div[span[text()='Соусы']]")
    # Активный раздел "Соусы".
    ACTIVE_SAUCE_TAB = (By.XPATH, "//div[contains(@class, 'current') and span[text()='Соусы']]")

    # Раздел "Начинки".
    FILLING_TAB = (By.XPATH, "//div[span[text()='Начинки']]")
    # Активный раздел "Начинки".
    ACTIVE_FILLING_TAB = (By.XPATH, "//div[contains(@class, 'current') and span[text()='Начинки']]")


    # Кнопка "Оформить заказ" для проверки входа на страницу с аккаунтом.
    ORDER_BTN = (By.XPATH, "//button[contains(@class, 'type_primary')]")

    # Логотип 'Stellar Burger'.
    LOGO_SB = (By.XPATH, "//div[contains(@class, 'header__logo')]")

    # Гиперссылка "Войти" переводит к форме входа в аккаунт из формы востановления пароля.
    PASS_ENTER_LINK = (By.XPATH, "//a[text()='Войти']")

    # Кнопка выхода из аккаунта в личном кабинете.
    LOGOUT_BTN =(By.XPATH, "//button[contains(text(),'Выход')]")

    # Гиперссылка "Конструктор".
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
