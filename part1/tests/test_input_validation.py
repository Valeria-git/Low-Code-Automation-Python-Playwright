from playwright.sync_api import sync_playwright, Page, expect




def test_input_validation_main(page: Page) -> None:
    firstname_value = 'Ivan'
    surname_value = 'IvanovvvvIvanovvvv'
    age_value = '30'
    country_value = 'Belarus'
    notes_value = 'some notes'


    page.goto("https://testpages.eviltester.com/styled/validation/input-validation.html")

    page.locator("#firstname").fill(firstname_value)
    page.locator("#surname").fill(surname_value)
    page.locator("#age").fill(age_value)
    page.locator("#country").select_option(country_value)
    page.locator("#notes").fill(notes_value)
    page.locator("input[type='submit']").click()

    
    expect(page.locator("h1")).to_have_text("Input Validation Response")
    expect(page.locator("#firstname-value")).to_have_text(firstname_value)
    expect(page.locator("#surname-value")).to_have_text(surname_value)
    expect(page.locator("#age-value")).to_have_text(age_value)
    expect(page.locator("#country-value")).to_have_text(country_value)
    expect(page.locator("#notes-value")).to_have_text(notes_value)
