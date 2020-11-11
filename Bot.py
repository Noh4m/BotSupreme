from selenium import webdriver
from config import config
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

# will cookies improve load time?
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=www.supremenewyork.com')







@timeme
def order():
    # add to cart
    add_to_cart = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
    add_to_cart.click()

    # attendre le chargement de la page
    time.sleep(.5)
    checkout_element = driver.find_element_by_xpath('//*[@id="cart"]/a[2]')
    checkout_element.click()

    # infos

    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(config['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(config['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(config['phone'])
    driver.find_element_by_xpath('//*[@id="bo"]').get_property(config['adresse'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(config['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(config['zipCode'])
# Select Contry
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[14]').click()
# Select month of the card
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[6]').click()

# Select years of the card
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[3]').click()
# CVV & CardNumber
    driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(config['cardNumber'])
    driver.find_element_by_xpath('//*[@id="vval"]').send_keys(config['cardCvv'])

# checkout
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
        # load chrome
    driver = webdriver.Chrome('./chromedriver')
    # get product url
    driver.get(config['product_url'])
    order()


