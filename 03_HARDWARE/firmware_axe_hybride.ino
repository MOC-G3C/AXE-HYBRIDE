int myThreshold = 550; // Remplace par la valeur trouvée via le Traceur
bool pulseDetected = false;

void loop() {
  int signal = analogRead(PULSE_PIN);

  // Détection du pic réel
  if (signal > myThreshold && pulseDetected == false) {
    pulseDetected = true;
    // Ici, on envoie le signal de battement
    Serial.println("BPM:DETECTED"); 
  }
  
  if (signal < myThreshold) {
    pulseDetected = false;
  }
  
  delay(20);
}