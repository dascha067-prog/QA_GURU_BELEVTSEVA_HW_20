import allure
import pytest
import allure_commons

from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser, support

from selene_in_action import utils, settings


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',
        'app': 'bs://sample.app',

        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # 🔐 данные берутся из settings, как у преподавателя
            'userName': settings.bstack_userName,
            'accessKey': settings.bstack_accessKey,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'https://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.timeout = settings.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.allure.attach_bstack_video(session_id)

