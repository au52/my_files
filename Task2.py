from selenium import webdriver
import time
import math

url = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(url)

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_link_text(a)
link.click()

try:

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Sidor")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Matrasych")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Bobruysk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarussia")
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:

    time.sleep(30)
    browser.quit()