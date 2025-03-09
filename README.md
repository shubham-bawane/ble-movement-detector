# BLE Movement Detector

This project detects movement using a BLE-based accelerometer tag. It scans for advertisement packets, extracts X, Y, Z accelerometer values, and determines whether the device is **moving** or **stationary**.

## 📌 Features
✅ BLE Scanning for advertisements  
✅ Extracts accelerometer data from service data  
✅ Movement vs. stationary detection  
✅ Works on Linux & Mac  
✅ Dockerized for easy deployment  

---

## 📌 Prerequisites
- **Python 3.7+**
- **Bluetooth Adapter** (Laptop must support BLE)
- **Linux/MacOS** (Windows BLE support is limited)
- **Docker & Docker Compose**

---

## 📌 Installation & Setup

### **1️⃣ Install Dependencies (Manual Method)**
```bash
pip install -r requirements.txt
