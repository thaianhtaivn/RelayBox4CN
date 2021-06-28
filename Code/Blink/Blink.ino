/*
  Blink
  http://www.arduino.cc/en/Tutorial/Blink
*/
#include <EEPROM.h>
char pinout[] = {6,7,8,9};
int i = 0;
int addr = 0;
byte value;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  for (i=0;i<5;i++){
    pinMode(pinout[i], OUTPUT);
    digitalWrite(6, LOW);
    delay(100); 
  }
//  Serial_begin(38400);
}

// the loop function runs over and over again forever
void loop() {
  for (i=0;i<4;i++){
    digitalWrite(pinout[i], HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);
  }
  for (i=0;i<4;i++){
    digitalWrite(pinout[i], LOW);   // turn the LED on (HIGH is the voltage level)
    delay(500);
  }
  
                         // wait for a second
//  if (i==1){
//    Serial_println_s("Read from EEPROM:");
//    value = EEPROM_read(addr);
//    Serial_println_ub(value, DEC);
//    EEPROM_write(addr, 1);
//    digitalWrite(3, HIGH);
//  }
//  
//  if (i==11){
//    Serial_println_s("Read from EEPROM:");
//    value = EEPROM_read(addr);
//    Serial_println_ub(value, DEC);
//    EEPROM_write(addr, 0);
//    digitalWrite(3, LOW);
//    Serial_println_s("LOW");
//  }
//  
//  if (i==20)
//  i = 0;
//  digitalWrite(4, LOW);    // turn the LED off by making the voltage LOW
//  delay(500);
  
}
