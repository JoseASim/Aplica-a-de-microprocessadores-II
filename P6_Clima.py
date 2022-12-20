from requests import get
import json
from pprint import pprint
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

closet_stn = '966583'

weather = weather + str(closet_stn)

my_weather = get(weather).json()['items']
pprint(my_weather)