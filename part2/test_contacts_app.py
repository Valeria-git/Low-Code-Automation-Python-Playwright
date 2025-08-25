from playwright.sync_api import Page, expect, Route
from http.cookies import SimpleCookie


def test_api_examples_br(page: Page) -> None:
    created_contact = {}
    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    login_email = "test_random@mail.org"
    login_pwd = "2345678"
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"
    phone_number = "123456789"
    country = "USA"

    patch_first_name = "Anna"

    # Task-Part-3.1: Add country data to the request payload in the Add Contact request interception
    def handle_contacts(route: Route):
        # intercept Add Contact request
        if route.request.method == "POST":
            response = route.fetch()
            nonlocal created_contact
            created_contact = response.json()
            route.fulfill(response=response)
        # intercept Get Contact List request   
        elif route.request.method == "GET":
            response = route.fetch()
            json = response.json()
            json.append({"_id": "001", "firstName": "Fake", "lastName": "Contact", "email": "fake@mail.com",
                        "phone": "12345", "owner": "6894ad53a0504000151c0ba5", "country": "USA",  "__v": 0})
            route.fulfill(response=response, json=json)        
        else:
            route.continue_()

    page.route("**/contacts", handle_contacts)

    # login via API
    response = page.request.post(url=base_url + "/users/login",
                      data={"email": login_email, "password": login_pwd})
    assert response.ok, "Login response status should be OK"
    assert "set-cookie" in response.headers, "Login response should contain set-cookie header"
    # retrieve auth token from the response set-cookie header
    # set_cookie = response.headers.get("set-cookie", "")
    # cookie = SimpleCookie()
    # cookie.load(set_cookie)
    # token = cookie["token"].value
    cookies = page.context.cookies()
    token = next((cookie["value"] for cookie in cookies if cookie["name"] == "token"), None)
    assert token is not None, "Auth token should be present in browser context cookies"
    # Task-Part-2: Replace logic from the block above - retrieve auth token from the browser context (hint: use page.context.cookies())

    # UI test part - add new contact
    page.goto(base_url + "/contactList")
    page.get_by_role("button", name="Add a New Contact").click()
    page.locator("#firstName").fill(first_name)
    page.locator("#lastName").fill(last_name)
    page.locator("#email").fill(email)
    page.locator("#phone").fill(phone_number)
    page.locator("#country").fill(country)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#myTable")).to_be_visible()

    # verify created entity
    assert created_contact["firstName"] == first_name, "Created contact first name should equal to that entered"
    assert created_contact["lastName"] == last_name, "Created contact last name should equal to that entered"
    assert created_contact["email"] == email, "Created contact email should equal to that entered"
    assert created_contact["phone"] == phone_number, "Created contact phone should equal to that entered"
    assert created_contact["country"] == country, "Created contact country should equal to 'USA'"
    # Task-Part-3.2: Add an assertion for country field

    # Task-Part-4: Update the contact's firstName using PATCH API request, assert the response status and the updated field value
    response = page.request.patch(url=base_url + "/contacts/" + created_contact["_id"], data={"firstName": patch_first_name},
                     headers={"Authorization": "Bearer " + token})

    # clean server state
    response = page.request.delete(url=base_url + "/contacts/" + created_contact["_id"], 
                     headers={"Authorization": "Bearer " + token})
    assert response.ok, "Delete Contact response status should be OK"
