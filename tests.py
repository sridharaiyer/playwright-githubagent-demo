import json
import time
from playwright.sync_api import sync_playwright
import pytest


def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_add_to_cart(username, password):
    config = load_config()
    browser_args = config.get("browser_args", [])

    with sync_playwright() as p:
        # Add slowMo option for slower execution
        browser = p.chromium.launch(headless=False, args=browser_args, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the login page
        page.goto("https://www.saucedemo.com/")

        # Perform login
        page.fill("#user-name", username)
        page.fill("#password", password)
        page.click("#login-button")

        # Fix the XPath to ensure the 'Add to cart' button belongs to the correct product
        product_selector = "text=Test.allTheThings() T-Shirt (Red)"
        add_to_cart_button = f"{product_selector} >> xpath=ancestor::div[contains(@class, 'inventory_item')]//button[text()='Add to cart']"
        page.wait_for_selector(add_to_cart_button, timeout=60000)  # Wait up to 60 seconds

        # Add the product to the cart
        page.click(add_to_cart_button)

        # Fix the XPath for the 'Remove' button to ensure it belongs to the correct product
        remove_button = f"{product_selector} >> xpath=ancestor::div[contains(@class, 'inventory_item')]//button[text()='Remove']"

        # Verify the 'Remove' button is visible
        assert page.is_visible(remove_button), "Remove button not found for the product."

        # Close the browser
        browser.close()


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_verify_product_in_cart(username, password):
    config = load_config()
    browser_args = config.get("browser_args", [])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=browser_args, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the login page
        page.goto("https://www.saucedemo.com/")

        # Perform login
        page.fill("#user-name", username)
        page.fill("#password", password)
        page.click("#login-button")

        # Add the product to the cart
        product_selector = "text=Test.allTheThings() T-Shirt (Red)"
        add_to_cart_button = f"{product_selector} >> xpath=ancestor::div[contains(@class, 'inventory_item')]//button[text()='Add to cart']"
        page.wait_for_selector(add_to_cart_button, timeout=60000)
        page.click(add_to_cart_button)

        # Navigate to the cart
        cart_icon_selector = "#shopping_cart_container"
        page.click(cart_icon_selector)

        # Verify the selected product is listed in the cart
        cart_item_selector = f"{product_selector} >> xpath=ancestor::div[contains(@class, 'cart_item')]"
        assert page.is_visible(cart_item_selector), "Selected product is not listed in the cart."

        # Close the browser
        browser.close()
