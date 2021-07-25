# importing required modules/packages
import time,requests,json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def check_weather():
    # getting inputs
    json_input = input("Please Enter your Data in JSON format and hit ENTER:").replace('“','"').replace('”','"')
    data_dict = json.loads(json_input)
    city_list = data_dict["City"]
    allowed_variance = data_dict["Variance"]

    # Phase 1: gettig temperature values from weather.com UI
    # initializing instance of webdriver

    driver = webdriver.Chrome(executable_path="Drivers//chromedriver.exe",options=options)
    driver.maximize_window()
    driver.get("https://weather.com/")
    for city in city_list:
        #will wait till location search input is clickable
        try:
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"LocationSearch_input")))
            search_box = driver.find_element_by_id("LocationSearch_input")
        #if location search input is not interactable or missing from DOM then reloading the page
        except  selenium.common.exceptions.StaleElementReferenceException:
            driver.refresh()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "LocationSearch_input")))
            search_box = driver.find_element_by_id("LocationSearch_input")
        search_box.click()
        #entering city name in location search input
        search_box.clear()
        # capitalizing city name because we weather.com lists city names in capitalize manner
        city.capitalize()
        search_box.send_keys(city)
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f'(//div[@id="LocationSearch_listbox"]/button[contains(text(),"{city}")])[1]')))
            driver.find_element_by_xpath(f'(//div[@id="LocationSearch_listbox"]/button[contains(text(),"{city}")])[1]').click()
        except Exception as e:
            print(f"No Result found for city name {city}")
            continue
        # # getting value of temperature from UI
        UI_temperature = int(str(driver.find_element_by_xpath('//span[@class="CurrentConditions--tempValue--1RYJJ"]').text).replace("°",""))
        # Phase 2 : Getting temperature from API
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4cbdf2b2851ed8893a53e8cf7af9ce9f&units=metric")
        api_data = req.json()
        if api_data["cod"]==200:
            api_temperature = api_data["main"]["temp"]
        else:
            print(api_data["message"],f" with name {city}")
            continue
        # Phase 3 : comparing both temperatures and returning response
        # calculating variance % wrt UI Values (as not specified in assignment question)
        temperature_difference = abs(UI_temperature - api_temperature) * 100 / UI_temperature
        if temperature_difference <= allowed_variance:
            print(
                f"Success: UI temperature {UI_temperature} and api temparature {api_temperature} of {city} have variance {temperature_difference} in required range")
        else:
            print(
                f"Matcher Exception: variance for {city} temperatures {UI_temperature} and {api_temperature} is {temperature_difference}, which is above allowed variance")
    driver.quit()

if __name__=="__main__":
   check_weather()
