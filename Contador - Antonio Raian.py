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
#função pra limpar o console
clear = lambda: os.system('clear')

#Setando o modo de operação
GPIO.setmode(GPIO.BCM)

#inicializando todos os pinos dos leds
for i in LEDS:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

#Inicializando Botões
GPIO.setup(BTN_START, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BTN_CLEAR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Função q transforma decimal para binário
def binario(num):
	resultado = []
	for i in range(8):
		resultado.append(num & 1) #AND binário
		num >>= 1 #Shift direita
	return resultado

#Função pra setar o valor binário nos	LEDS
def setPins(valor):
	for led in LEDS:
		for bit in binario(valor):
			GPIO.output(led, bit)

count = 0

# def contador(pino):
while 1:
	clear()
	print('Valor atual = ', count)

	if GPIO.input(BTN_START) == GPIO.HIGH:
		setPins(count)
		time.sleep(0.8)

		count += 1
		if count == 256:
			count = 0

	if GPIO.input(BTN_CLEAR) == GPIO.HIGH:
		setPins(count)
		count = 0

def cleanUp(pino):
	count = 0

# GPIO.add_event_detect(BTN_START, GPIO.BOTH, callback=contador, bouncetime=100)
# GPIO.add_event_detect(BTN_CLEAR, GPIO.BOTH, callback=cleanUp, bouncetime=100)

try:
	time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.clean

