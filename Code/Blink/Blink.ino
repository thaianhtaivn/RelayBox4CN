//#include <EEPROM.h>
//#include <String.h>
byte pinout[] = {6,7,8,9};
int i = 0, mode =0;
int addr = 0;
char value;
char txtMsg;
//byte DATA[30]={};
int LINE_BUFFER_SIZE = 10; // max line length is one less than this
char line[15];

int read_line(char* buffer, int bufsize)
{
  for (int index = 0; index < bufsize; index++) {
    while (Serial_available() == 0) {
    }
    char ch = Serial_read(); // read next character
//    Serial.print(ch); // echo it back: useful with the serial monitor (optional)
    if (ch == '\n') {
      buffer[index] = 0; // end of line reached: null terminate string
      return index; // success: return length of string (zero if string is empty)
    }
    buffer[index] = ch; // Append character to buffer
  }
  char ch;
  do {
    while (Serial_available() == 0) {
      
    }
    ch = Serial_read(); // read next character (and discard it)
    Serial_print_s(ch); // echo it back
  } while (ch != '\n');
  buffer[0] = 0; // set buffer to empty string even though it should not be used
  return -1; // error: return negative one to indicate the input was too long
}

void setup() {
  Serial_begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  for (i=0;i<5;i++){
    pinMode(pinout[i], OUTPUT);
    digitalWrite(6, LOW); 
  }
  delay(100); i=0;
  Serial_println_s("RELAY BOX 4 CHANNEL");
}



// the loop function runs over and over again forever
void loop() {
  mode = 0;

//  char line[LINE_BUFFER_SIZE]="";
////  char line;
  if (read_line(line, sizeof(line)) < 0) {
    Serial_println_s("Error: line too long");
    return; // skip command processing and try again on next iteration of loop
  }

  if (strcmp(line, "VSET1") == 0) {
    mode = 1;
  } else if (strcmp(line, "VSET2") == 0) {
    mode = 2;
    Serial_println_s("MODE 2");
  } else if (strcmp(line, "VSET3") == 0) {
    mode = 3;
  } else if (strcmp(line, "VSET4") == 0) {
    mode = 4;
  } else if (strcmp(line, "VSETA") == 0) {
    mode = 5;
  } else if (strcmp(line, "VOFF") == 0) {
    mode = 10;  
  } else {
    Serial_println_s("UNKNOW COMMAND");
    Serial_println_s(line);    
  }
  switch (mode){
    case 1:
      digitalWrite(pinout[0], HIGH);
      break;
    case 2:
      digitalWrite(pinout[1], HIGH);
      break;
    case 3:
      digitalWrite(pinout[2], HIGH);
      break;
    case 4:
      digitalWrite(pinout[3], HIGH);
      break;
    case 5:
      for(i=0; i<4;i++)
        digitalWrite(pinout[i], HIGH);
      break;
    case 10:
      for(i=0; i<4;i++)
        digitalWrite(pinout[i], LOW);
      break;
  }

}
