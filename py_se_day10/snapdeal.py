from selenium import webdriver
import time

# A - Arrange (Setup/Prerequsite)
# A - Action
# A = Assert  (Validate)



def verify_search_functionality(search_text):

    # ARRANGE

    driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
    driver.get("https://www.snapdeal.com/offers/essential?")
    driver.maximize_window()
    time.sleep(4)

#//button[@class='_2AkmmA _29YdH8']

## ACTION
    search_box = driver.find_element_by_name("keyword")   # Find the location of search box
    #search_box.send_keys("Macbook pro")   # to enter text we have to use send_keys()
    search_box.send_keys(search_text)

# Finding xpath using contains(attribute, textwithinattributevalue)
    search_icon = driver.find_element_by_xpath("//button[contains(@class, 'searchformButton')]")
    search_icon.click()

    search_box = driver.find_element_by_name("keyword")   # Find the location of search box
    #search_box.send_keys("Macbook pro")   # to enter text we have to use send_keys()
    search_box.send_keys(search_text)

    search_icon = driver.find_element_by_xpath("//button[contains(@class, 'searchformButton')]")
    search_icon.click()
    time.sleep(5)

## ASSERT
    search_product_info_element = driver.find_element_by_xpath("(//span[@class='nnn'])[1]")
    search_product_info =  search_product_info_element.text

    if(search_product_info == "We've got 10000+ results for 'samsung mobile phone'"):
        print("We have successfully searched the product " + search_text)
    else:
        print("The search product is not listed here")





    driver.close()
    driver.quit()


# verify_search_functionality("Macbook pro back cover")

verify_search_functionality("samsung mobile phone")