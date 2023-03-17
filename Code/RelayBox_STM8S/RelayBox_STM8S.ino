// Relay Box 4 channel
// @THT5HC
byte pinout[] = {6,7,8,9};
uint8_t i = 0, cmd =0;
char line[15];
char *command[] = {"VSET1OUTon", "VSET1OUToff", "VSET2OUTon", "VSET2OUToff", "VSET3OUTon","VSET3OUToff", "VSET4OUTon","VSET4OUToff", "VSETAOUTon","VSETAOUToff"};
// Func read serial, return length of string
int read_line(char* buffer, int bufsize)
{
  for (int index = 0; index < bufsize; index++) {
    while (Serial_available() == 0);
    char ch = Serial_read(); // read next character
    if (ch == '\n') {
      buffer[index] = 0; // end of line reached: null terminate string
      return index; // success: return length of string (zero if string is empty)
    }
    buffer[index] = ch; // Append character to buffer
  }
  char ch;
  do {
    while (Serial_available() == 0);
    ch = Serial_read(); // read next character (and discard it)
//    Serial_print_s(ch); // echo it back
  } while (ch != '\n');
  buffer[0] = 0; // set buffer to empty string even though it should not be used
  return -1; // error: return negative one to indicate the input was too long
}

void setup() {
  Serial_begin(9600);
  for (i=0;i<5;i++){
    pinMode(pinout[i], OUTPUT);
    digitalWrite(6, LOW); 
  }
  delay(100);
//  Serial_println_s("RELAY BOX 4 CHANNEL");
}
void loop() {
  cmd = 99;
  if (read_line(line, sizeof(line)) < 0) {
    Serial_println_s("Error: Command too long");
    return; // skip command processing and try again on next iteration of loop
  }
  for(i=0; i<sizeof(command); i++){
    if (strcmp(line, command[i])==0){
      cmd = i;
      break;
    }
   }
  switch (cmd){
    case 0: digitalWrite(pinout[0], HIGH); break;
    case 1: digitalWrite(pinout[0], LOW); break;
    case 2: digitalWrite(pinout[1], HIGH); break;
    case 3: digitalWrite(pinout[1], LOW); break;
    case 4: digitalWrite(pinout[2], HIGH); break;
    case 5: digitalWrite(pinout[2], LOW); break;
    case 6: digitalWrite(pinout[3], HIGH); break;
    case 7: digitalWrite(pinout[3], LOW); break;
    case 8: for(i=0; i<4;i++) digitalWrite(pinout[i], HIGH); break;
    case 9: for(i=0; i<4;i++) digitalWrite(pinout[i], LOW); break;    
  }
}
