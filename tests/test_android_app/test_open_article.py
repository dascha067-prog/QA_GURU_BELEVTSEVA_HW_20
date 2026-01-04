import allure
from selene import browser


@allure.title("Open article from search results")
def test_open_article_from_search():
    with allure.step("Open search"):
        browser.element('//*[@text="Search Wikipedia"]').click()

    with allure.step("Enter search query"):
        browser.element('//*[@resource-id="org.wikipedia.alpha:id/search_src_text"]').type("Python")

    with allure.step("Click on first search result"):
        browser.element('//*[@resource-id="org.wikipedia.alpha:id/page_list_item_container"]').click()
