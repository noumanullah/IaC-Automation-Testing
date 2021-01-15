from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

def GetCurrentDateTime():
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    return (ts + '   --->   ')

# Open Browser
def OpenBrowser():
    print(GetCurrentDateTime() + 'Opening browser')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print(GetCurrentDateTime() + 'Browser opened.')
    return driver

# Login With Username & Password
def UserLogin(driver, username, password):
    print(GetCurrentDateTime() + 'Navigating to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(username)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_label = driver.find_element_by_css_selector("div[class='product_label']").text
    assert "Products" in product_label
    print(GetCurrentDateTime() + 'User has logged-in: Username [{:s}] and Password [{:s}]'.format(username, password))

def AddItemsToCart(driver, itemsCount):
    print(GetCurrentDateTime() + 'Starting adding {:d} items to cart.'.format(itemsCount))
    for i in range(itemsCount):
        element = "a[id='item_" + str(i) + "_title_link']" 
        driver.find_element_by_css_selector(element).click() 
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click() 
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text  
        print(GetCurrentDateTime() + product + " is added to shopping cart.") 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click() 
    cartCount = driver.find_element_by_css_selector("span[class='fa-layers-counter shopping_cart_badge']").text
    assert "6" in cartCount
    print(GetCurrentDateTime() + 'All {:d} items are added to shopping cart successfully.'.format(itemsCount))

def RemoveItemsFromCart(driver, itemsCount):
    print(GetCurrentDateTime() + 'Starting removing {:d} items to cart.'.format(itemsCount))
    for i in range(itemsCount):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(GetCurrentDateTime() + product + " is removed from shopping cart.") 
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    elementExists = driver.find_elements_by_xpath('//*[@id="shopping_cart_container"]/a/span')
    if not len(elementExists):
        print(GetCurrentDateTime() + 'All {:d} items are removed from shopping cart successfully.'.format(itemsCount))

if __name__ == "__main__":
    print(GetCurrentDateTime() + 'Script Running!')
    driver = OpenBrowser()
    UserLogin(driver, 'standard_user', 'secret_sauce')
    AddItemsToCart(driver, 6)
    RemoveItemsFromCart(driver, 6)
    print(GetCurrentDateTime() + 'Script Stopped!')
