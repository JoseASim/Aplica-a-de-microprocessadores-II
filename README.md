# Aplicação-de-microprocessadores-II

Primeiramente foi realizado um código que por meio do I2C tire uma foto. O código é apresentado a seguir.

  from picamera import PiCamera                           #importa as blibiotecas que serão utilizadas
  from time import sleep                               

  camera = PiCamera()                                     #configura uma variável para realizar as instruções

  camera.resolution = (2592, 1944)                        #define a resolução
  camera.framerate = 15

  camera.start_preview()                                  #inicia a visualização câmera

  camera.annotate_text = "11930742"                       #texto que deve ficar na foto
  sleep(2)                                                #espera 2 segundo
  camera.capture('/home/sel/SEL0337/11930742/image.jpg')  #tira a foto e salva no local informado

  camera.stop_preview()                                   #desliga a visualização da câmera

Então, com um código parecido é possível gravar um vídeo.

  from picamera import PiCamera                                   #importa as blibiotecas que serão utilizadas
  from time import sleep

  camera = PiCamera()                                             #configura uma variável para realizar as instruções

  camera.start_preview()                                          #inicia a visualização câmera
.
  camera.annotate_text = "11930742"                               #texto que deve ficar no vídeo
  camera.start_recording('/home/sel/SEL0337/11930742/video.h264') #começa a gravar e salva no loal indicado
  sleep(5)                                                        #tempo de espera/duração do vídeo
  camera.stop_recording()                                         #para a gravação

  camera.stop_preview()                                           #desliga a visualização da câmera
  
Então, foi realizada a obtenção de dados climáticos da base localizada na UFSC por meio do código.

  from requests import get                                                                        #importa as blibiotecas que serão utilizadas
  import json
  from pprint import pprint
  
  weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'  #associa a variavel ao diretório de IDs

  closet_stn = '966583'                                                                           #ID da base da UFSC

  weather = weather + str(closet_stn)                                                             #obtém os dados do ID

  my_weather = get(weather).json()['items']                                                       #obtém os dados do clima
  pprint(my_weather)                                                                              #mostra os dados obtidos

