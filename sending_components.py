import main
fresh_powder = False

def is_snow_coming ():
    for snow in main.snowfall:
        if snow != '0"':
            fresh_powder = True
    print(fresh_powder)

    