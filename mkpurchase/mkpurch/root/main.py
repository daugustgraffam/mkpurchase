from selenium import webdriver

class makePurchase():
    def buy(self):
        driver = webdriver.Firefox()
        driver.get("http://squaretesting.weebly.com/")
        button = driver.find_element_by_xpath(".//div[@id='wsite-content']//div[@class='wsite-product-button-wrap']/a")
        button.click()
        driver.implicitly_wait(20)
        email = driver.find_element_by_xpath(".//div[@id='wsite-content']//label[@class='wsite-checkout-form__field']//input[@class='js-customer-email wsite-checkout-form__input']")
        email.send_keys('derrick.g@weebly.com')
        fname = driver.find_element_by_name('name_first')
        fname.send_keys('QA')
        lname = driver.find_element_by_name('name_last')
        lname.send_keys('Squaretesting')
        address1 = driver.find_element_by_name('street')
        address1.send_keys('123 Weebly St')
        city = driver.find_element_by_name('city')
        city.send_keys('San Francisco')
        state = driver.find_element_by_name('region')
        state.send_keys('c')
        zipcode = driver.find_element_by_name('postal_code')
        zipcode.send_keys('94107')
        phone = driver.find_element_by_name('phone')
        phone.send_keys('5555555555')
        nextbutton = driver.find_element_by_class_name('js-next-btn.wsite-button.wsite-button-small.wsite-button-highlight.wsite-buy-button')
        nextbutton.click()

ecom = makePurchase()
ecom.buy()


# from webdriver_util import init
#
#
# def query_google(keywords):
#     print("Loading Firefox driver...")
#     driver, waiter, selector, datapath = init()
#
#     print("Fetching google front page...")
#     driver.get("http://google.com")
#
#     print("Taking a screenshot...")
#     waiter.shoot("frontpage")
#
#     print("Typing query string...")
#     selector.get_and_clear("input[type=text]").send_keys(keywords)
#
#     print("Hitting Enter...")
#     selector.get("input[type=submit]").click()
#
#     print("Waiting for results to come back...")
#     waiter.until_display("#ires")
#
#     print
#     print("The top search result is:")
#     print
#     print('    "{}"'.format(selector.get("#ires a").text))
#     print
#
#
# if __name__ == '__main__':
#     query_google('test')
