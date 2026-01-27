#include <Adafruit_NeoPixel.h>

#define PIN        6   // Le fil "Data" est sur la broche 6
#define NUMPIXELS 12   // Nombre de LEDs sur ton anneau

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin(); // Initialisation
}

void loop() {
  pixels.clear(); // Éteindre tout

  for(int i=0; i<NUMPIXELS; i++) {
    // On fait défiler un spectre Cyan/Bleu (Couleur de base du Nexus)
    pixels.setPixelColor(i, pixels.Color(0, 255, 255)); 
    pixels.show();
    delay(100);
  }
  
  delay(500);
  
  // Flash Rouge (Test du seuil Critique 130 BPM)
  for(int i=0; i<NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(255, 0, 0));
  }
  pixels.show();
  delay(1000);
}