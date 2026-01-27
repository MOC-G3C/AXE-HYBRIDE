#include <Adafruit_NeoPixel.h>

// --- CONFIGURATION ---
#define PULSE_PIN A0        // Pulse Sensor connected to Analog Pin 0
#define LED_PIN 6           // NeoPixel Ring connected to Digital Pin 6
#define NUM_LEDS 12         // Number of LEDs in your ring

Adafruit_NeoPixel ring(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Thresholds defined in Kybernetes-Governance
const int THRESHOLD_RESONANCE = 100;
const int THRESHOLD_CRITICAL = 130;

void setup() {
  Serial.begin(115200);     // High speed for real-time resonance
  ring.begin();
  ring.show();              // Initialize all pixels to 'off'
}

void loop() {
  int signal = analogRead(PULSE_PIN);
  
  // Simple BPM estimation logic (to be refined with hardware)
  // For now, we transmit the raw signal for the Neural Bridge to process
  float simulatedBPM = map(signal, 0, 1023, 60, 160); 

  // --- VISUAL CORE LOGIC ---
  if (simulatedBPM > THRESHOLD_CRITICAL) {
    setRingColor(255, 0, 0); // RED: Critical
  } else if (simulatedBPM > THRESHOLD_RESONANCE) {
    setRingColor(255, 255, 0); // YELLOW: Resonance
  } else {
    setRingColor(0, 255, 255); // CYAN: Pulse
  }

  // --- SERIAL BRIDGE ---
  // Format: BPM:[value]
  Serial.print("BPM:");
  Serial.println(simulatedBPM);

  delay(20); // Frequency alignment
}

void setRingColor(uint8_t r, uint8_t g, uint8_t b) {
  for(int i=0; i<NUM_LEDS; i++) {
    ring.setPixelColor(i, ring.Color(r, g, b));
  }
  ring.show();
}