from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://opensnow.com/location/copper')

elems = browser.find_elements_by_class_name('high')
snow = browser.find_elements_by_class_name('us')
hiTemp = []
snowForecast = []

for element in elems:
    try: 
        tag = element.text
        hiTemp.append(tag)
    except:
       print("Something went wrong getting temperatures")

for forecast in snow:
    try:
        snowfall = forecast.text
        snowForecast.append(snowfall)
    except: 
       print('Something went wrong getting snowfall')

while('' in snowForecast):
    snowForecast.remove('')

print(hiTemp)
print(snowForecast)