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
