from requests import get                                                                        #importa as blibiotecas que serão utilizadas
import json
from pprint import pprint

weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'  #associa a variavel ao diretório de IDs

closet_stn = '966583'                                                                           #ID da base da UFSC

weather = weather + str(closet_stn)                                                             #obtém os dados do ID

my_weather = get(weather).json()['items']                                                       #obtém os dados do clima
pprint(my_weather)                                                                              #mostra os dados obtidos