# Wiring Logic and Pin Mapping

## 1. Bio-Sensing Components
| Component | Arduino Pin | Wire Color (Typical) | Notes |
| :--- | :--- | :--- | :--- |
| **Pulse Sensor** | A0 (Analog) | Purple (Signal) | Connect Red to 5V, Black to GND. |
| **LDR (Light)** | A1 (Analog) | - | Use a 10k Ohm pull-down resistor. |
| **DHT11 (Temp)** | D2 (Digital) | - | Requires a 10k Ohm pull-up on Data. |

## 2. Feedback Components
| Component | Arduino Pin | Type | Function |
| :--- | :--- | :--- | :--- |
| **NeoPixel Ring** | D6 (PWM) | Digital | Signal/Visual Feedback. |
| **Piezo Buzzer** | D3 (PWM) | Digital | Frequency Resonance (3-6-9). |
| **Status LED** | D13 (Built-in) | Digital | System heartbeat. |

## 3. Power Rail
- **VCC:** 5V (from USB or external regulated source).
- **GND:** Common Ground for all components and the MCU.

## 4. Connection Checklist
1. Verify no short circuits between 5V and GND.
2. Ensure the Pulse Sensor is connected to the Analog rail (A0).
3. Check Serial Baud Rate (9600) matches `pulse_serial_test.py`.