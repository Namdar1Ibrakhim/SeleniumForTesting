import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KryshaKzHomePage:
    LOGIN_BUTTON = (By.CLASS_NAME, "cabinet-link")
    LOGO = (By.CLASS_NAME, "logo")

    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        login_button.click()

    def click_logo(self):
        logo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGO))
        logo.click()

class KryshaKzLoginPage:
    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_INPUT))
        login_input.send_keys(username + Keys.ENTER)

        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.send_keys(password + Keys.ENTER)

class KryshaKzFavoritesPage:
    FIRST_LINK = (By.CSS_SELECTOR, ".hot__item a")
    ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, "button.kr-btn.kr-btn--white.a-fav-btn.a-fav-btn-big")
    FAVORITES_LINK = (By.CLASS_NAME, "favorites-link-item")
    DELETE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, "button.kr-btn.kr-btn--white.a-fav-btn.a-fav-btn-big.favorited")

    def __init__(self, driver):
        self.driver = driver

    def click_first_link(self):
        first_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_LINK))
        first_link.click()

    def add_to_favorites(self):
        add_to_favorites_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ADD_TO_FAVORITES_BUTTON))
        add_to_favorites_button.click()

    def click_favorites_link(self):
        favorites_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FAVORITES_LINK))
        favorites_link.click()

    def delete_from_favorites(self):
        delete_from_favorites_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DELETE_FROM_FAVORITES_BUTTON))
        delete_from_favorites_button.click()

class KryshaKzMessagePage:
    FIRST_LINK = (By.CSS_SELECTOR, ".hot__item a")
    MESSAGE_LINK = (By.CSS_SELECTOR, "a.kr-btn.kr-btn--auto.kr-btn--blue.tm-message-body.message-send-button")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "span.footer__input")

    def __init__(self, driver):
        self.driver = driver

    def click_first_link(self):
        first_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_LINK))
        first_link.click()

    def click_message_link(self):
        message_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MESSAGE_LINK))
        message_link.click()

    def enter_message(self, message):
        message_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MESSAGE_INPUT))
        message_input.send_keys(message)

    def submit(self):
        message_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.MESSAGE_INPUT))
        message_input.submit()



class KryshaKzNotesPage:
    FIRST_LINK = (By.CSS_SELECTOR, ".hot__item a")
    NOTES_LINK = (By.CSS_SELECTOR, "button.kr-btn.kr-btn--white.a-note-btn.a-note-btn-big")
    TEXT_AREA = (By.CSS_SELECTOR, "textarea.ui-input.note-modal__input")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button.a-note-cont__delete")
    DELETE_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button.ui-button.note-delete-modal__btn.note-delete-modal__btn--submit.ui-button--blue')

    def __init__(self, driver):
        self.driver = driver

    def click_first_link(self):
        first_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_LINK))
        first_link.click()

    def click_notes_link(self):
        notes_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NOTES_LINK))
        notes_link.click()

    def enter_note(self, note):
        text_area = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TEXT_AREA))
        text_area.send_keys(note + Keys.ENTER)

    def delete_note(self):
        delete_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DELETE_BUTTON))
        delete_button.click()

    def confirm_delete(self):
        delete_button_submit = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELETE_BUTTON_SUBMIT))
        delete_button_submit.click()

class KryshaKzSettingsPage:
    DROPDOWN_TRIGGER = (By.CSS_SELECTOR, "li.dropdown.header-dropdown.js-init-tutorial > a")
    SETTINGS_LINK = (By.LINK_TEXT, "Настройки")
    INPUT_ELEMENT = (By.ID, "name")
    BUTTON_ELEMENT = (By.CSS_SELECTOR, "button.kr-btn.kr-btn--large.kr-btn--blue-gradient")

    def __init__(self, driver):
        self.driver = driver

    def open_settings(self):
        dropdown_trigger = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DROPDOWN_TRIGGER))
        dropdown_trigger.click()

        settings_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SETTINGS_LINK))
        settings_link.click()

    def enter_name(self, name):
        input_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.INPUT_ELEMENT))
        input_element.send_keys(name)

    def save_changes(self):
        button_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BUTTON_ELEMENT))
        button_element.click()



