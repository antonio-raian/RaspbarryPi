#########################################################
#
# Projeto: Minicuros - Utilizando a GPIO da Raspberry Pi
# Autor: Antonio Raian Mendes <raymendesjr2013@gmail.com>
# Atividade: 4 - Contador Binário
#
#########################################################

import RPi_emu.GPIO as GPIO
import time
import os
from threading import Thread

PAUSE = 0
PLAY = 1

#função pra limpar o console
clear = lambda: os.system('clear')

#Função q transforma decimal para binário
def binario(num):
	resultado = []
	for i in range(8):
		resultado.append(num & 1) #AND binário
		num >>= 1 #Shift direita
	return resultado

def setPins(pins, bits):
	for led, bit in zip(pins, bits):
		# print('LED BIT', led, bit)
		GPIO.output(led, bit)

#Classe para armazenar a contagem
class Counter:
	def __init__ (self, num):
		Thread.__init__(self)
		self.count = num
		self.state = PAUSE
	#Adiciona um ao contador
	def add(self):
		if self.state == PLAY:
			self.count += 1
	#Seta o contador para 0
	def clean(self):
		self.count = 0

#Classe da Thread q faz a contagem
class Th(Thread):
	def __init__ (self, counter, leds):
		Thread.__init__(self)
		self.counter = counter
		self.leds = leds
	def run(self):
		while(1):
			if (self.counter.state == PLAY):
				clear()
				print('Valor atual = ',self.counter.count)
				#Percorre os pinos do led colocando os valores referentes a cada um
				setPins(self.leds, binario(self.counter.count))
				#Soma mais um ao contador
				self.counter.add()
				#Espera um segundo
				time.sleep(1)

#Função pra setar o valor binário nos	LEDS
			
def play_pause(counter):
	if counter.state == PAUSE:
		print("PLAY", counter.count)
		counter.state = PLAY
	else:
		print("PAUSE")
		counter.state = PAUSE

def cleanUp(leds, counter):
	print('Zerou')
	counter.clean()
	setPins(leds, binario(0))

if __name__ == '__main__':
	#define uma variavel com o valor dos pinos usado
	LEDS = [17, 27, 22, 10, 9, 11, 5, 6]
	BTN_START = 23
	BTN_CLEAR = 24

	clear()

	#Setando o modo de operação
	GPIO.setmode(GPIO.BCM)

	#inicializando todos os pinos dos leds
	for i in LEDS:
		GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

	#Inicializando Botões
	GPIO.setup(BTN_START, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(BTN_CLEAR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

	#Cria a instancia de um contador iniciando em 0
	counter = Counter(0)

	#Cria os detectores de eventos para os pinos de entrada
	GPIO.add_event_detect(BTN_START, GPIO.BOTH, callback= lambda x: play_pause(counter), bouncetime=100)
	GPIO.add_event_detect(BTN_CLEAR, GPIO.RISING, callback=lambda x: cleanUp(LEDS, counter), bouncetime=100)
	
	#cria uma thread responsavel por contar
	thread = Th(counter, LEDS)
	thread.start() #Inicia a thread

	try:
		time.sleep(0.5)
	except KeyboardInterrupt:
  		GPIO.clean