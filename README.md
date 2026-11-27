# Embedded Edge AI Portfolio

Self-directed portfolio focused on the full stack of Embedded AI engineering:
- Reliable low-level firmware
- On-device machine learning
- Hardware + sensor integration
- Real-world constraints (latency, memory, power, reliability)

Target platforms and themes relevant to edge devices, wearables, robotics, and industrial systems.

## Projects

### 1. TinyML Wearable Activity Recognition (In Progress)
**Platform:** Arduino Nano 33 BLE Sense Rev2

Build a wearable that classifies activities (walking, running, sitting, etc.) directly on the microcontroller.

- Collect and label IMU datasets
- Train models in Python (PyTorch / TensorFlow)
- Quantize to INT8 and deploy
- Real-time C++ inference pipeline
- BLE transmission of results
- Measure RAM, Flash, inference latency, power, and accuracy

### 2. Intelligent Predictive Maintenance System (Planned – target end of 2026)
**Platform:** Arduino Nano 33 BLE Sense → UNO Q path

Monitor a motor using vibration and temperature sensors, detect abnormal behavior, and generate early warnings.

- Deterministic sensor sampling
- Digital filtering + feature extraction (RMS, variance, frequency-domain)
- Anomaly detection (threshold-based vs ML)
- On-device inference and event handling
- Alerts via dashboard / hardware indicators
- Evaluate detection accuracy, false-alarm rate, latency, and power

### Future Projects (planned)
Additional projects will continue to cover firmware reliability, sensor fusion, optimization, and system-level integration under real constraints.

## Structure
