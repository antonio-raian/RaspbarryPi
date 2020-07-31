#########################################################
#
# Projeto: Minicuros - Utilizando a GPIO da Raspberry Pi
# Autor: Antonio Raian Mendes <raymendesjr2013@gmail.com>
# Atividade: 2 - Acender LED
#
#########################################################

import RPi_emu.GPIO as GPIO
import time

#define uma variavel com o valor do pino usado
LED = 17

#Seta o GPIO para o modo BCM, poderia ser o modo BOARD
GPIO.setmode(GPIO.BCM)
#Identifico o meu pino e digo q ele é de saída
GPIO.setup(LED, GPIO.OUT)

print("Raspberry Pi blink\n")
while 1:
  GPIO.output(LED, GPIO.HIGH) #Aciona o pino 
  time.sleep(1.5) #Espera um segundo e meio
  GPIO.output(LED, GPIO.LOW) #Desliga o pino
  time.sleep(0.5) #espera meio segundo

