import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1_sign_in(self):
        # 1. Вход под парой логин/пароль
        driver = self.driver
        driver.set_window_size(1920, 960)
        driver.get("http:/127.0.0.1:8000")
        self.assertIn('Отдел аренды', driver.title)

        elem = driver.find_element_by_id('id_username')
        elem.send_keys('admin')
        elem = driver.find_element_by_id('id_password')
        elem.send_keys('admin')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_2_sign_out(self):
        self.test_1_sign_in()
        # 2. Выход из под пользователя
        driver = self.driver
        elem = driver.find_element_by_css_selector(".btn-outline-primary")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_3(self):
        self.test_1_sign_in()
        # 3. Переход во вкладку клиенты и выбор одного из клиентов
        driver = self.driver
        elem = driver.find_element_by_xpath("//a[contains(.,'Клиенты')]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("//div[1]")
        elem.click()
        time.sleep(2)

    def test_4(self):
        self.test_1_sign_in()
        # 4. Изменение и сохранения одного из клиентов
        driver = self.driver
        elem = driver.find_element_by_xpath("//a[contains(.,'Клиенты')]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        elem = driver.find_element_by_xpath("//div[1]")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id('id_customer_name')
        elem.clear()
        elem.send_keys('Игнатенко Петр Владимирович')
        time.sleep(0.25)
        elem = driver.find_element_by_id('id_customer_phone')
        elem.clear()
        elem.send_keys('89132001010')
        time.sleep(0.25)
        elem = driver.find_element_by_id('id_customer_pasport')
        elem.clear()
        elem.send_keys('1234 567890')
        time.sleep(1)
        elem = driver.find_element_by_name('save-client')
        elem.click()
        time.sleep(2)

    def test_5(self):
        self.test_1_sign_in()
        # 5. Добавление нового клиента
        driver = self.driver
        elem = driver.find_element_by_xpath("//a[contains(.,'Клиенты')]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("//div/a")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_id('id_customer_name')
        elem.clear()
        elem.send_keys('Савченко Илья Андреевич')
        time.sleep(0.25)
        elem = driver.find_element_by_id('id_customer_phone')
        elem.clear()
        elem.send_keys('89132001010')
        time.sleep(0.25)
        elem = driver.find_element_by_id('id_customer_pasport')
        elem.clear()
        elem.send_keys('1234 567890')
        time.sleep(0.25)
        elem = driver.find_element_by_name('save-client')
        elem.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
