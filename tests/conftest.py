import os
import pytest
import allure

from dotenv import load_dotenv
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support
import allure_commons

# 1. Загружаю базовый .env
load_dotenv()

# 2. Беру context
context = os.getenv("context")
if not context:
    raise RuntimeError("context is not set")

# 3. Загружаю env по context
load_dotenv(f".env.{context}")


@pytest.fixture(scope="function", autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": os.getenv("platformName"),
        "automationName": "UiAutomator2",
        "deviceName": os.getenv("deviceName"),
        "appWaitActivity": "org.wikipedia.*",
        "app": os.getenv("app"),
    })

    with allure.step("Init app session"):
        browser.config.driver = webdriver.Remote(
            command_executor=os.getenv("command_executor"),
            options=options,
        )

    browser.config.timeout = float(os.getenv("timeout", 10.0))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name="page source",
        attachment_type=allure.attachment_type.XML,
    )

    browser.quit()
