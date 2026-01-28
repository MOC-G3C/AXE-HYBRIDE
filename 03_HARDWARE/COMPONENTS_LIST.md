# Hardware Components List (Hybrid Axis)

## 1. Bio-Sensing Layer (Bridge to 02_HUMAIN)
- **Pulse Sensor (Analog):** Required for `pulse_calibration.ino` to track real-time heart rate and update `BIO_CALIBRATION.md`.
- **LDR (Light Dependent Resistor):** Necessary for `visual_core.py` to calibrate ambient light against neural load.
- **DHT11/22 Sensor:** Optional for tracking ambient temperature/humidity for biological baseline data.

## 2. Processing and Logic
- **Microcontroller (MCU):** ESP32 or Arduino Nano (capable of serial communication with Python).
- **Logic Level Converter:** If using 3.3V sensors with 5V controllers.

## 3. Feedback and Output
- **NeoPixel Ring/Strip:** For visual frequency feedback (controlled by `visual_core.py`).
- **Piezo Buzzer:** For acoustic 3-6-9 resonance patterns in `tesla_resonance_369.py`.

## 4. Prototyping Essentials
- **Breadboard:** For circuit assembly.
- **Jumper Wires:** M-M and M-F sets.
- **10k Ohm Resistors:** For sensor voltage dividers.