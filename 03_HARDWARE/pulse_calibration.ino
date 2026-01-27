void setup() {
  Serial.begin(115200);
}

void loop() {
  int signal = analogRead(A0); // Lecture brute du capteur
  
  // On envoie la valeur au traceur série
  Serial.println(signal); 
  
  delay(10); // Lecture rapide pour voir la courbe
}