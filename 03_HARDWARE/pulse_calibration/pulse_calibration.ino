/*
 * Pulse Sensor Calibration - Hybrid Axis (Hardware Layer)
 * Reads analog pulse signal and transmits BPM to Python Serial Bridge.
 */

const int pulsePin = A0;    // Pulse Sensor purple wire connected to Analog Pin 0
const int blinkPin = 13;    // Pin to blink led at each beat
const int threshold = 550;  // Determine which signal to "count" as a beat

void setup() {
  pinMode(blinkPin, OUTPUT);
  Serial.begin(9600);       // Match baud rate with pulse_serial_test.py
}

void loop() {
  int signalValue = analogRead(pulsePin);

  if (signalValue > threshold) {
    digitalWrite(blinkPin, HIGH);
    // Simplified BPM calculation or raw signal transmission
    // For this bridge, we send the raw value to be processed by Python
    Serial.println(signalValue); 
  } else {
    digitalWrite(blinkPin, LOW);
  }
  
  delay(20); // Stability delay
}