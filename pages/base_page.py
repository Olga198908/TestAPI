import pytest
from playwright.sync_api import sync_playwright, Page, expect
from config.conftest import *

from data.module1_data import *
from locators.module1_locators import *

@pytest.fixture
def pw_template_1(page: Page):
    def pw_template_1_fync():
        page.goto(URL_CAT_BUTTON)
        page.click(LOCATOR_BASIC)
        expect(page.locator(LOCATOR_TABLE1)).to_contain_text(DATA_TEXT)
        page.wait_for_timeout(1000)
        page.go_back()

    return pw_template_1_fync()

@pytest.fixture
def pw_template_2(page: Page):
    def pw_template_2_fync():
        page.click(LOCATOR_ELEMENT)
        page.mouse.wheel(0, 1000)
        page.keyboard.press(LOCATOR_BUTTON)
        page.click(LOCATOR_BUTTON_TABLE)
        expect(page.locator(LOCATOR_BUTTON_TABLE)).to_be_visible()
        page.go_back()

    return pw_template_2_fync()

@pytest.fixture
def pw_template_3(page: Page):
    def pw_template_3_fync():
        page.click(LOCATOR_FIND)
        expect(page.locator(LOCATOR_TABLE2)).to_be_visible()
        page.mouse.wheel(0, 1000)
        page.keyboard.press(LOCATOR_BUTTON)
        page.click(LOCATOR_BUTTON_JUMP1)
        expect(page.locator(LOCATOR_TABLE3)).to_be_visible()
        page.go_back()
        page.go_back()

    return pw_template_3_fync()

@pytest.fixture
def pw_template_4(page: Page):
    def pw_template_4_fync():
        page.click(LOCATOR_WEBDRIVER)
        expect(page.locator(LOCATOR_NUM)).to_be_visible()
        page.wait_for_timeout(1000)
        page.fill(LOCATOR_NUM, DATA_FILL)
        expect(page.locator(LOCATOR_NUM)).to_have_value(DATA_FILL)
        page.click(LOCATOR_PROCESS)
        page.go_back()

    return pw_template_4_fync()