import pytest
from playwright.sync_api import sync_playwright, Page, expect
from pages.base_page import *
from config.conftest import *


@pytest.mark.smoke
def test_flow(page, pw_template_1, pw_template_2, pw_template_3, pw_template_4):
    pw_template_1()
    pw_template_2()
    pw_template_3()
    pw_template_4()