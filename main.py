import asyncio
from bleak import BleakScanner

# Constants
TARGET_SERVICE_UUID = "c8e5b2f0-3a9c-11ee-be56-0242ac120002"
TARGET_DEVICE_MAC = "48:74:12:31:E3:AA"  # BLE Device Address (optional filtering)

# Store previous accelerometer values
prev_x, prev_y, prev_z = None, None, None  

async def scan_for_service_data():
    """ Scans for BLE devices and extracts accelerometer data from advertisements. """
    print("🔍 Scanning for BLE Service Data...")

    def detection_callback(device, advertisement_data):
        global prev_x, prev_y, prev_z  # Use previous values for comparison

        if TARGET_SERVICE_UUID in advertisement_data.service_data:
            raw_data = advertisement_data.service_data[TARGET_SERVICE_UUID]
            x, y, z = raw_data[0], raw_data[1], raw_data[2]  # Extract X, Y, Z accelerometer values
            
            # Detect movement
            status = detect_movement(x, y, z)
            print(f"📊 jhghj{device}")

            print(f"✅ Found BLE Device: - {device.address}")
            print(f"📊 Accelerometer Data -> X: {x}, Y: {y}, Z: {z} | Status: {status}")

    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(10)  # Scan for 10 seconds
    await scanner.stop()

def detect_movement(x, y, z):
    """ Determines if the sensor is moving or stationary based on change in values. """
    global prev_x, prev_y, prev_z

    # If first reading, store values and return "Waiting..."
    if prev_x is None:
        prev_x, prev_y, prev_z = x, y, z
        return "⏳ Waiting for movement data..."

    movement_threshold = 3  # Adjust sensitivity threshold

    # Calculate differences between current and previous values
    delta_x = abs(x - prev_x)
    delta_y = abs(y - prev_y)
    delta_z = abs(z - prev_z)

    # Update previous values
    prev_x, prev_y, prev_z = x, y, z

    # Determine if movement is detected
    if delta_x > movement_threshold or delta_y > movement_threshold or delta_z > movement_threshold:
        return "🚀 Moving"
    else:
        return "⏸️ Stationary"

if __name__ == "__main__":
    asyncio.run(scan_for_service_data())
