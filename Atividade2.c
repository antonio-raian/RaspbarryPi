#include <stdio.h>
#include <wiringPi.h>
#include<time.h> 

#define BTN 3 //BCM_GPIO pin 22

int btnState;
int lastState = 0;
clock_t time;

int main (void){
  printf ("Raspberry Pi Button\n");

  if (wiringPiSetup () == -1)
    return 1;

  pinMode (BTN, INTPUT);

  while(true){
    int buttonValue = digitalRead(BTN);
    //Inicia o deboucing
    if(buttonValue != lastState)
        time = clock();
    if(((float)clock() - time/1000000.0F)>50){
        if(buttonValue != btnState){
            btnState = buttonValue;
        }
        if(buttonValue == 1){
            printf("Botão ativo")
        }else{
            printf("Botão solto")
        }
    }
  }

  return 0;
}