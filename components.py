from selenium import webdriver
browser = webdriver.Firefox()

def get_temp ():
    elems = browser.find_elements_by_class_name('high')
    hiTemp = []

    for element in elems:
        try: 
            tag = element.text
            hiTemp.append(tag)
        except:
            print("Something went wrong getting temperatures")

    print(hiTemp)

def get_snow ():
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