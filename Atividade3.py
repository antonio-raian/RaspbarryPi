#########################################################
#
# Projeto: Minicuros - Utilizando a GPIO da Raspberry Pi
# Autor: Antonio Raian Mendes <raymendesjr2013@gmail.com>
# Atividade: 3 - Debouncing digital
#
#########################################################

import RPi_emu.GPIO as GPIO
import time
import os

#define uma variavel com o valor do pino usado
# Inicializar pines de salida.
LEDS = [17, 27, 22, 10, 9, 11, 5, 6]
BTN_START = 23
BTN_CLEAR = 24

GPIO.setmode(GPIO.BCM)


for i in LEDS:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(BTN_START, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BTN_CLEAR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

clear = lambda: os.system('clear')

def binario(n):
	resultado = []
	for i in range(8):
		resultado.append(n & 1) #AND binário
		n >>= 1 #Shift direita
	return resultado
def setPins(value):
	for pin, bit in zip(LEDS, binario(value)):
		GPIO.output(pin, bit)

valor = 0

# def contador(pino):
while 1:
	clear()
	print('Valor atual = ', valor)

	if GPIO.input(BTN_START) == GPIO.HIGH:
		setPins(valor)
		time.sleep(0.8)

		valor += 1
		if valor == 256:
			valor = 0

	if GPIO.input(BTN_CLEAR) == GPIO.HIGH:
		setPins(valor)
		valor = 0

def cleanUp(pino):
	valor = 0

# GPIO.add_event_detect(BTN_START, GPIO.BOTH, callback=contador, bouncetime=100)
# GPIO.add_event_detect(BTN_CLEAR, GPIO.BOTH, callback=cleanUp, bouncetime=100)

try:
	time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.clean

