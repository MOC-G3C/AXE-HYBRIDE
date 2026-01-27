# 03_HARDWARE : Physical Components List

To complete the bridge between biology and code, the following hardware is required for the "Axe Hybride" project.

## 1. The Core (Microcontroller)
* **Arduino Uno or Nano:** The brain that will interface with the sensors.
* **USB Cable:** To bridge the Arduino to the Mac.

## 2. The Bio-Sensor (Input)
* **Pulse Sensor (Optical):** To capture real-time BPM instead of relying on JSON logs.
* **Connection:** VCC (3V/5V), GND, and Analog Signal (A0).

## 3. The Visual Feedback (Output)
* **WS2812B LED Ring (NeoPixel):** To visualize the "Visual Core" logic (Cyan, Yellow, Red).
* **Connection:** DI (Digital Pin), VCC, GND.

## 4. The Bridge Logic
The Arduino will read the pulse, process it, and send a serial string to the Mac:
`BPM:[value],INTENSITY:[0-255]`