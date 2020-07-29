#include <stdio.h>
#include <wiringPi.h>

#define LED 0 //BCM_GPIO pin 17

int main (void){
  printf ("Raspberry Pi blink\n");

  if (wiringPiSetup () == -1)
    return 1;

  pinMode (LED, OUTPUT);

  while(true){
    digitalWrite (LED, 1);
    delay (1500);
    digitalWrite (LED, 0);
    delay (500);
  }

  return 0;
}