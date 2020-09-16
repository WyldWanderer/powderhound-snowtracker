import scraper_components
import sending_components

# Sets static URL's for sending specific data to user via text or email and calls functions from scraper_components.py
scraper_components.url ='https://opensnow.com/location/copper'
temps = scraper_components.get_temp()
snowfall = scraper_components.get_snow()
sending_components.is_snow_coming()

# Resets browser variable in scraper_components.py so that a new URL is opened and is targeted by the called functions
scraper_components.browser = ''

# Commented out while working on sending_components.py, once functions working will test with additional URLs
#scraper_components.url = 'https://opensnow.com/location/winterpark'
#scraper_components.get_temp()
#scraper_components.get_snow()

