import re
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import pytest



def test_software_testing(page: Page) -> None:
    quantity_value = "10"
    page.goto("https://practicesoftwaretesting.com/")

    page.locator("#search-query").fill("hammer")
    page.locator("button[type='submit']").click()
    
    page.locator("select[data-test='sort']").select_option("price,desc")
    page.locator("h5[data-test='product-name']").nth(0).click()

    product_name = page.locator("h1[data-test='product-name']").inner_text()

    product_price = page.locator("[data-test=\"unit-price\"]").inner_text()


    page.locator("[data-test=\"quantity\"]").fill(quantity_value)
    page.locator("[data-test=\"add-to-cart\"]").click()


    page.locator("[data-test=\"nav-cart\"]").click()
    
    expect(page.locator("[data-test=\"product-title\"]")).to_have_text(product_name)
    expect(page.locator("[data-test=\"product-quantity\"]")).to_have_value(quantity_value)
    expect(page.locator("[data-test=\"product-price\"]")).to_contain_text(product_price)
