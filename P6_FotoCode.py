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
