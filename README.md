# README - BLE Movement Detector

## BLE Movement Detector

This project detects movement using a BLE-based accelerometer tag. It scans for advertisement packets, extracts X, Y, Z accelerometer values, and determines whether the device is moving or stationary.

## Features

- BLE Scanning for advertisements
- Extracts accelerometer data from service data
- Movement vs. stationary detection
- Works on Linux & Mac


## Prerequisites

- Python 3.7+
- Bluetooth Adapter (Laptop must support BLE)
- Linux/MacOS (Windows BLE support is limited)
- nRF Connect App (For mobile BLE broadcasting)

## Setting Up Your Phone (nRF Connect)

1. Install nRF Connect from the Play Store or App Store.
2. Open the app and navigate to Advertiser.
3. Create a new advertisement profile:
   - Service UUID: `c8e5b2f0-3a9c-11ee-be56-0242ac120002`
   - Service Data: Choose a custom data field for X, Y, Z values.
4. Start broadcasting from the phone.
5. Verify that your laptop detects the phone’s BLE advertisement.

## Installation & Setup

### Install Dependencies (Manual Method)
```bash
pip install -r requirements.txt
```

### Run the BLE Scanner
```bash
python main.py
```


## Expected Output
```
Scanning for BLE Service Data...
Found BLE Device: 48:74:12:31:E3:AA
Accelerometer Data -> X: 9, Y: 8, Z: 7 | Status: Stationary
Accelerometer Data -> X: 15, Y: 20, Z: 12 | Status: Moving
```


## Repository Link

**GitHub Repository:** [ble-movement-detector](https://github.com/shubham-bawane/ble-movement-detector)

## Author

- **Shubham (Your Name)**
- **Email:** shubhambawane410@gmail.com
- **GitHub:** (https://github.com/shubham-bawane)

