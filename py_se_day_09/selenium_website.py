from selenium import webdriver
from time import sleep


def test_documentation_link():
    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://www.selenium.dev/")
    driver.maximize_window();
    sleep(4)

    # driver.find_element_by_link_text("Downloads").click()

    # Find Downloads using Absolute xpath
    # xpath = //html/body/header/nav/a[1]

    # Absolute xpath for Downloads
    # driver.find_element_by_xpath("//html/body/header/nav/a[1]").click()

    # Relative xpath for Downloads
    driver.find_element_by_xpath("(//a[@href='/downloads'])[1]").click()

    sleep(4)
    # documentation = driver.find_element_by_link_text("documentation")

    # Absolute xpath for Downloads
    # documentation = driver.find_element_by_xpath("//html/body/header/nav/a[3]")

    # Relative xpath for Downloads
    documentation = driver.find_element_by_xpath("(//a[@href='/documentation'])[1]")

    documentation.click()

    #//header[@id='header']//a[@href='/about']

    sleep(8)

    driver.close()
    driver.quit()
