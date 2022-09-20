import webbrowser, sys, bs4, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time

op = webdriver.ChromeOptions()
op.add_argument('headless')
chromedriver_path = "//Users//Srivastr14//Documents//chromedriver"
browser = webdriver.Chrome(executable_path=chromedriver_path, options=op)


sys.argv #['weather.py', 'knoxville,', 'TN']

def getWeather(productUrl):
    res = requests.get(productUrl, timeout = 5) #make the scraper look like a computer
    res.raise_for_status() # this is in case the website wont load
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#current_conditions-summary > p.myforecast-current-lrg')
    # This code above is used with the CSS selector
    # print(elems[0].text.strip())
    return elems[0].text.strip()

def getToWebsite(city_state):
    current_url_ = 'https://forecast.weather.gov/MapClick.php?lat=35.960680000000025&lon=-83.92102999999997#.YBpXi3dKi34'
    browser.get(current_url_)
    city = browser.find_element_by_css_selector('#inputstring')
    city.click()
    city.send_keys(city_state)
    city.send_keys(Keys.ENTER)
    city.click()
    time.sleep(1)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnSearch"]')))
    go_page = browser.find_element_by_css_selector('#btnSearch')
    go_page.click()
    go_page.send_keys(Keys.ENTER)
    time.sleep(1)
    # print(browser.current_url)
    cityURL = browser.current_url
    browser.quit()
    return cityURL


city_state = ' '.join(sys.argv[1:])

weather = getToWebsite(city_state)
print('\nHere we go!\n')
Temp = getWeather(str(weather))

print('The temperature in ' + city_state + ' is ' + Temp + '\n')
browser.quit()
