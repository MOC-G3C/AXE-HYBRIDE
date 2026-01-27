#include <Adafruit_NeoPixel.h> // On utilise le "dictionnaire"

#define PIN        6   // Fil de données sur la broche 6
#define NUMPIXELS 12   // Nombre de LEDs sur ton anneau
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin(); // Initialisation des LEDs
  Serial.begin(115200);
  
  // SÉQUENCE DE BIENVENUE (Respiration Cyan)
  for(int b=0; b<150; b++) { 
    for(int i=0; i<NUMPIXELS; i++) pixels.setPixelColor(i, pixels.Color(0, b, b));
    pixels.show();
    delay(5);
  }
}

void loop() {
  // Le système attend ici ton pouls...
}