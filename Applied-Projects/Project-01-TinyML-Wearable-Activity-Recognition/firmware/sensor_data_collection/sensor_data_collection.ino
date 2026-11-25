#include <Arduino_BMI270_BMM150.h>

// Define the target sampling interval in milliseconds
// 20ms = 50 Hz sampling frequency (1000 ms / 50 = 20ms)
const unsigned long SAMPLING_INTERVAL_MS = 20;
unsigned long lastSampleTime = 0;

void setup() {
  // Initialize serial communication at 9600 baud for debugging
  Serial.begin(9600);

  // Wait for the serial monitor to open
  while(!Serial);

  Serial.println("Initializing BMI270 IMU...");

  // Initialize the IMU sensor
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while(1);   // Halt execution if sensor fails
  }

  Serial.println("IMU initialized successfully.");
  // Serial.println("Timestamp(ms),AccX(g),AccY(g),AccZ(g),GyroX(dps),GyroY(dps),GyroZ(dps)"); in python's file now
}

void loop() {
  unsigned long currentTime = millis();

  // Enforce a strict fixed sampling frequency
  if (currentTime - lastSampleTime >= SAMPLING_INTERVAL_MS) {
    lastSampleTime = currentTime;

    float ax, ay, az;
    float gx, gy, gz;

    // Check if both accelerometer and gyroscope data are available to read
    if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {

      // Read accelerometer data (in g-forces)
      IMU.readAcceleration(ax, ay, az);

      // Read gyroscope data (in degrees/second)
      IMU.readGyroscope(gx, gy, gz);

      // Print timestamp and sensor values in CSV format
      Serial.print(currentTime);
      Serial.print(",");
      Serial.print(ax); Serial.print(",");
      Serial.print(ay); Serial.print(",");
      Serial.print(az); Serial.print(",");
      Serial.print(gx); Serial.print(",");
      Serial.print(gy); Serial.print(",");
      Serial.println(gz);
    }
  }
}
