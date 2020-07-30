#########################################################
#
# Projeto: Minicuros - Utilizando a GPIO da Raspberry Pi
# Autor: Antonio Raian Mendes <raymendesjr2013@gmail.com>
# Atividade: 3 - Debouncing digital
#
#########################################################

import RPi_emu.GPIO as GPIO
import time

#define uma variavel com o valor do pino usado
LED = 17
BTN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BTN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def myReturn(pin):
  print("Evento %s = %s" % (pin, GPIO.input(pin)))
  btnValue = GPIO.input(BTN)
  GPIO.output(LED, btnValue)

print("Raspberry Pi Button\n")
GPIO.add_event_detect(BTN, GPIO.BOTH, callback=myReturn, bouncetime=100)

try:
  time.sleep(500)
except KeyboardInterrupt:
  GPIO.cleanup()
