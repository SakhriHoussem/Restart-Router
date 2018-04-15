"""
restart Router TP-link TD-W8968 programmatically
"""
from time import sleep

try:
    from selenium import webdriver
except:
    import pip.main as install
    install(['install', 'selenium'])

class Restart:

    def __init__(self,
                 link='http://192.168.1.1/',
                 username="admin",
                 password="admin",
                 driver='chrome',
                 driver_path=''):
        """
        :param str link: link to acces to router login page
        :param str username: username to acces to router
        :param str password: password to acces to router
        :param str driver: browser name
        :param str driver_path: browser driver path
        :return:
        """
        self.link = link
        self.username = username

        self.password = password

        self.driver = driver

        self.driver_path = driver_path

        self.drivers = {'chrome':webdriver.Chrome,
                        'firefox':webdriver.Firefox,
                        'opera':webdriver.Opera,
                        'safari':webdriver.Safari,
                        'edge':webdriver.Edge,
                        'ie':webdriver.Ie
                        }

        browser = self.drivers[self.driver](self.driver_path)

        browser.implicitly_wait(10)

        browser.get(self.link)

        sleep(2)

        browser.find_element_by_id("userName").send_keys(self.username)

        browser.find_element_by_id("pcPassword").send_keys(self.password)

        browser.find_element_by_tag_name("button").click()

        sleep(2)

        browser.switch_to.frame('menufrm')

        browser.find_element_by_id("74").click()

        browser.find_element_by_id("87").click()

        browser.switch_to.default_content()

        sleep(2)

        browser.switch_to.frame('basefrm')

        browser.find_element_by_tag_name("input").click()

        browser.switch_to.alert.accept()

        sleep(2)

        browser.close()

if __name__ == '__main__':

    Restart(driver='chrome',driver_path='chromedriver.exe')