const int raspPinnen[] = {10, 11};
unsigned long vorigeTijd = 0;
bool ledStatus = false;

void setup() {
  pinMode(raspPinnen[0], INPUT); 
  pinMode(raspPinnen[1], OUTPUT); 
  digitalWrite(raspPinnen[1], LOW);
}

//functie voor het regelen van de pinnen
void loop() {
  unsigned long huidigeTijd = millis();
  if (digitalRead(raspPinnen[0]) == LOW) {
    if (huidigeTijd - vorigeTijd >= 1000){
      vorigeTijd = huidigeTijd;
      if(ledStatus){
        digitalWrite(raspPinnen[1], HIGH);
        ledStatus = false;
      } else {
        digitalWrite(raspPinnen[1], LOW);
        ledStatus = true;
      }
    }
  }
}