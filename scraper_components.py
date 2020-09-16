# Contains the functions for web scraping upcoming temperature and snow forecast
from selenium import webdriver

# Set starting global variables
url = 'EMPTY URL'
browser = ''

# Prompts for user to enter which resort the client wants information on, this function is for later if deploying to a more interactive platform
# Currently, the url variable is being set in main.py 
def get_url ():
    input_name = input("Where are you interested in skiing?: ")
    location_name = input_name.lower().replace(" ", "")
    global url 
    url = 'https://opensnow.com/location/' + location_name

# Get's available temperature data from provided url, url MUST BE https://opensnow.com/location/ + location name in order to work 
# as the find elements by class name method is page specific
def get_temp ():
    global browser
    if browser == '':
        browser = webdriver.Firefox()
        browser.get(url)

    elems = browser.find_elements_by_class_name('high')

    hiTemp = []

    for element in elems:
        try: 
            tag = element.text
            hiTemp.append(tag)
        except:
            print("Something went wrong getting temperatures")

    print(hiTemp)

# Get's available snow forecast data from provided url, url MUST BE https://opensnow.com/location/ + location name in order to work 
# as the find elements by class name method is page specific
def get_snow ():
    global browser
    if browser == '':
        browser = webdriver.Firefox()
        browser.get(url)

    snow = browser.find_elements_by_class_name('us')
    
    snowForecast = []

    for forecast in snow:
        try:
            snowfall = forecast.text
            snowForecast.append(snowfall)
        except: 
            print('Something went wrong getting snowfall')

    while('' in snowForecast):
        snowForecast.remove('')

    print(snowForecast)

