import pytest
import time
from selenium import webdriver
from pages import KryshaKzHomePage, KryshaKzLoginPage, KryshaKzFavoritesPage, KryshaKzMessagePage, KryshaKzNotesPage, \
    KryshaKzSettingsPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize('phone_number, password', [("87084053169", "Ibrahim2004")])
def test_login(driver, phone_number, password):
    driver.get("http://krysha.kz/")
    home_page = KryshaKzHomePage(driver)
    login_page = KryshaKzLoginPage(driver)

    home_page.click_login_button()
    time.sleep(3)
    login_page.login(phone_number, password)
    time.sleep(5)
    home_page.click_logo()
    time.sleep(3)


def test_favorites(driver):
    home_page = KryshaKzHomePage(driver)
    favorites_page = KryshaKzFavoritesPage(driver)

    favorites_page.click_first_link()
    time.sleep(3)
    favorites_page.add_to_favorites()
    time.sleep(3)
    favorites_page.click_favorites_link()
    time.sleep(3)
    favorites_page.delete_from_favorites()
    time.sleep(3)
    favorites_page.click_favorites_link()
    time.sleep(3)
    home_page.click_logo()
    time.sleep(3)


def test_messages(driver):
    home_page = KryshaKzHomePage(driver)
    messages_page = KryshaKzMessagePage(driver)

    messages_page.click_first_link()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(3)
    messages_page.click_message_link()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 300);")
    messages_page.enter_message("Здравствуйте")
    time.sleep(3)
    messages_page.submit()
    time.sleep(3)
    home_page.click_logo()
    time.sleep(3)


def test_notes(driver):
    home_page = KryshaKzHomePage(driver)
    notes_page = KryshaKzNotesPage(driver)

    driver.execute_script("window.scrollTo(400, 0);")
    notes_page.click_first_link()
    time.sleep(3)
    notes_page.click_notes_link()
    time.sleep(3)
    notes_page.enter_note("I like it")
    time.sleep(3)
    notes_page.delete_note()
    time.sleep(3)
    notes_page.confirm_delete()
    time.sleep(5)
    home_page.click_logo()
    time.sleep(3)


def test_edit_profile(driver):
    settings_page = KryshaKzSettingsPage(driver)
    settings_page.open_settings()
    time.sleep(3)
    settings_page.enter_name("Ibrakhim040101")
    time.sleep(3)
    settings_page.save_changes()
    time.sleep(3)
