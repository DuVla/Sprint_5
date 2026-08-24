from selenium.webdriver.common.by import By
# Форма входа
LOGIN_EMAIL_INPUT = (By.NAME, "name") #Поле Email на форме входа/регистрации
LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль") #Поле Пароль на форме входа/регистрации
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка отправки формы логина
LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']") # ссылка войти на странице регистрации и восстановлении пароля
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка войти в аккаунт на главной странице

# Регистрация и восстановление пароля
REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']") # Ссылка зарегистрироваться
FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']") # Ссылка восстановления пароля
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #форма регистрации
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") #форма регистрации
PASSWORD_ERROR = (By. CLASS_NAME, "input__error") # текст ошибки при некорректном пароле
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
REGISTRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
# header сайта
PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']") # ссылка на личный кабинет
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # Конструктор
LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a") # LOGO

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка выйти на главной странице

# Раздел конструктор
BUNS = (By.XPATH, "//span[text()='Булки']")
SAUCES = (By.XPATH, "//span[text()='Соусы']")
FILLINGS = (By.XPATH, "//span[text()='Начинки']")
BUNS_CONTAINER = (By.XPATH, "//span[text()='Булки']/..")
SAUCES_CONTAINER = (By.XPATH, "//span[text()='Соусы']/..")
FILLINGS_CONTAINER = (By.XPATH, "//span[text()='Начинки']/..")
