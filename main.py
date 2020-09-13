from selenium import webdriver
import components

webdriver.Firefox().get('https://opensnow.com/location/copper')
components.get_temp()
components.get_snow()

#webdriver.Firefox().get('https://opensnow.com/location/winterpark')
#components.get_temp()
#components.get_snow()