import scraper_components
import sending_components

# Sets static URL's for sending specific data to user via text or email and calls functions from scraper_components.py and sending_componenets.py
ski_resort = ''

def get_copper(): 
    global ski_resort 
    ski_resort = 'Copper'
    scraper_components.url ='https://opensnow.com/location/copper'
    scraper_components.get_snow()
    sending_components.is_snow_coming()
    sending_components.send_email()
    # Resets browser variable in scraper_components.py so that a new URL is opened and is targeted by the called functions
    scraper_components.browser = ''

# Commented out while working on sending_components.py, once functions working will test with additional URLs
#scraper_components.url = 'https://opensnow.com/location/winterpark'
#scraper_components.get_temp()
#scraper_components.get_snow()

get_copper()