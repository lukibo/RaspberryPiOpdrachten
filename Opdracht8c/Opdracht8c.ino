const int knopPin = 13;

const int leds[] = {3, 4};
const int raspPinnen[] = {10, 11};
int inputWaarden[] = {LOW, LOW};

void setup() {
  pinMode(leds[0], OUTPUT);  
  pinMode(leds[1], OUTPUT);  
  pinMode(raspPinnen[0], INPUT); 
  pinMode(raspPinnen[1], OUTPUT); 
}

//functie voor het regelen van de leds
void loop() {
  digitalWrite(raspPinnen[1], digitalRead(knopPin));

  digitalWrite(leds[0], digitalRead(raspPinnen[0]));
  
  if (digitalRead(raspPinnen[0]) == HIGH) {
    digitalWrite(leds[0], HIGH);
    digitalWrite(leds[1], LOW);
  } else {
    digitalWrite(leds[1], HIGH);
    digitalWrite(leds[0], LOW);
  }
}