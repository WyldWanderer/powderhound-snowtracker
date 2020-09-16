from selenium import webdriver
import components

# Sets static URL's for sending specific data to user via text or email
components.url ='https://opensnow.com/location/copper'
components.get_temp()
components.get_snow()

components.url = 'https://opensnow.com/location/winterpark'
components.get_temp()
components.get_snow()

