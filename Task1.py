from selenium import webdriver

browser = webdriver.Chrome()
# WebDriver будет искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

a = browser.find_element_by_id("button")
print(a.text)

browser.close()

# Проверка отправки изменений на репозит