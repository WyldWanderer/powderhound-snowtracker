import ezgmail
import scraper_components

fresh_powder = False

def is_snow_coming ():
    global fresh_powder
    for forecasts in scraper_components.snowForecast:
        if forecasts != '0"':
            fresh_powder = True

def send_email ():
    if fresh_powder == True:
        ezgmail.send('living2snowboard@gmail.com', 'Powderhound Alert!', 'Hey Tyler, check out the snow report for ' + ski_resort + '\n \n' 
                     'Upcoming snowfall \n'  + scraper_components.snowForecast[0] + ' ' + scraper_components.snowForecast[1] + ' ' + scraper_components.snowForecast[2] + ' ' + scraper_components.snowForecast[3] + ' ' + scraper_components.snowForecast[4] + ' ' + scraper_components.snowForecast[5] + ' ' + scraper_components.snowForecast[6])
        print('process finished, email sent')
    else:
        print('process finished, no email sent')
   