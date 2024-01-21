//bron Elske
#include <IRremote.h>
#include <string.h>

const int IrPin = 3;
const int RaspPins[] = {9, 10, 11, 12};

// Definieer de hexadecimale waarden die overeenkomen met de infraroodsignalen
unsigned long hexVal[] = { 0xF30CFF00, 0xE718FF00, 0xA15EFF00, 0xF708FF00 };

unsigned long newHexVal = 0;

// Array om de laatste millis-waarden op te slaan voor controle
unsigned long lastMillis[] = { 0, 0 };

int count = 0;
int lastLed;

// Maak een instantie van de IR-ontvanger
IRrecv irrecv(IrPin);
decode_results results;

void setup() {
    // Schakel de IR-ontvanger in
    irrecv.enableIRIn();

    // Stel de pin-modi in voor de LEDs
    for (int i = 0; i < 4; i++) {
        pinMode(RaspPins[i], OUTPUT);
    }
}

void loop() {
    // Controleer op ingedrukte knoppen
    findButtons();

    // Schakel LEDs uit als er slechts één knop is ingedrukt en er 2 seconden zijn verstreken
    if (count == 1 && millis() - lastMillis[0] >= 2000)
    {
        turnOffAllPins();
        count = 0;
    }
}

// Functie om alle LEDs uit te schakelen
void turnOffAllPins() {
    for (int i = 0; i < 4; i++) {
        digitalWrite(RaspPins[i], LOW);
    }
}

// Functie om te bepalen welke knop is ingedrukt
void findButtons() {
    if (irrecv.decode())
    {
        // Ontvang de hexadecimale waarde van het ontvangen IR-signaal
        newHexVal = (irrecv.decodedIRData.decodedRawData);
        Serial.println(newHexVal);

        // Controleer de hexadecimale waarde van elke knop
        for (int i = 0; i < 4; i++)
        {
            if (newHexVal == hexVal[i])
            {
                // Registreer het tijdstip van de knopdruk
                lastMillis[0] = millis();

                // Schakel alle LEDs uit en zet de overeenkomstige LED aan
                turnOffAllPins();
                digitalWrite(RaspPins[i], HIGH);
                lastLed = i;
            }
        }

        // Hervat ontvangst van IR-signalen
        irrecv.resume();
    }
}