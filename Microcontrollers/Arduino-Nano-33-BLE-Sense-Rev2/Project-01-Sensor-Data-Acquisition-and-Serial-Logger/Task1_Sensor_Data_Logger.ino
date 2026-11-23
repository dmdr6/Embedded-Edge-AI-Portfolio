#include <Arduino_BMI270_BMM150.h>

// Target sampling frequency in Hz
const int SAMPLE_RATE_HZ = 50;

// Calculate interval in milliseconds (1000ms / 50 = 20ms)
const unsigned long INTERVAL_MS = 1000 / SAMPLE_RATE_HZ;

unsigned long previousMillis = 0;

void setup() {
  // Initialize Serial communication at 115200 baud
  Serial.begin(115200);

  // Wait for the Serial monitor to open
  while (!Serial) {
    delay(10);
  }

  Serial.println("Initializing BMI270 IMU...");

  // Task 1: Initialize the onboard IMU and handle errors
  if (!IMU.begin()) {
    Serial.println("ERROR: Failed to initialize IMU! Check hardware.");
    while (1) {
      // Halt execution permanently if initialization fails
      delay(1000);
    }
  }

  Serial.println("IMU initialized successfully!");
  Serial.println("Timestamp(ms), AccX(g), AccY(g), AccZ(g),GyroX(dps),GyroY(dps),GyroZ(dps)");
}

void loop() {
  unsigned long currentMillis = millis();

  // Enforce a fixed sampling interval (50 Hz -> every 20 ms)
  if (currentMillis - previousMillis >= INTERVAL_MS) {
    previousMillis = currentMillis;   // Save the last sample time

    float accX, accY, accZ;
    float gyroX, gyroY, gyroZ;

    // Check if new accelerometer and gyroscope data are available
    if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
      IMU.readAcceleration(accX, accY, accZ);
      IMU.readGyroscope(gyroX, gyroY, gyroZ);

      // Print timestamped CSV-formatted readings over Serial
      Serial.print(currentMillis); Serial.print(",");
      Serial.print(accX, 4); Serial.print(",");
      Serial.print(accY, 4); Serial.print(",");
      Serial.print(accZ, 4); Serial.print(",");
      Serial.print(gyroX, 4); Serial.print(",");
      Serial.print(gyroY, 4);
      Serial.println(gyroZ, 4);
    } else {
      Serial.println("WARNING: Sensor data not ready.");
    }
  }
}
