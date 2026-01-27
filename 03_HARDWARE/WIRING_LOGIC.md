# Wiring Diagram Logic


### Pin Mapping:
- **Pulse Sensor Signal:** Analog Pin **A0**
- **LED Ring Data:** Digital Pin **6**
- **Pulse Sensor Power:** 3.3V (for better stability)
- **LED Ring Power:** 5V

### Communication Flow:
1. **Heartbeat** -> Pulse Sensor -> Arduino.
2. **Arduino** -> Serial Bridge (USB) -> `neural_bridge.py`.
3. **neural_bridge.py** -> Commands -> LED Ring (via Arduino).