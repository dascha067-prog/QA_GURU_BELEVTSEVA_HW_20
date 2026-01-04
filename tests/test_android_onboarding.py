import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title("Wikipedia onboarding: прохождение 4 экранов")
def test_wikipedia_onboarding():
    with step("Проверить первый onboarding экран"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("The Free Encyclopedia"))

        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Проверить второй onboarding экран"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("New ways to explore"))

        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Проверить третий onboarding экран"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("Reading lists"))

        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Проверить четвертый onboarding экран"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("Data & Privacy"))

        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()
