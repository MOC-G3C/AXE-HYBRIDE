#!/bin/bash

# Get the path to the project directory
PROJECT_DIR=~/Desktop/"L'AXE HYBRIDE"

# 1. Launch the Neural Bridge in a new window
osascript -e "tell application \"Terminal\" to do script \"cd '$PROJECT_DIR' && python3 01_SOFTWARE/Kybernetes-Governance/neural_bridge.py\""

# 2. Launch the Dashboard in another new window
osascript -e "tell application \"Terminal\" to do script \"cd '$PROJECT_DIR' && python3 01_SOFTWARE/Kybernetes-Governance/dashboard.py\""

# 3. Notification of activation
osascript -e "display notification \"Neural Bridge & Dashboard Active\" with title \"AXE HYBRIDE\""