# Smart Skincare Assistant (drbot)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[cite_start]An IoT-based Smart Skincare Assistant that provides personalized skincare recommendations by analyzing your skin and real-time environmental conditions[cite: 10, 11].

[cite_start]This system integrates capacitive moisture sensing, spectral skin tone/oil analysis, and environmental monitoring (UV, temperature, humidity)[cite: 11, 12]. [cite_start]A Feedforward Neural Network (FNN) processes this data to classify skin conditions into one of 81 unique classes, delivering customized advice and product suggestions via a user-friendly web application[cite: 13, 24, 25].

---

## 🌟 Key Features

* [cite_start]**Personalized Skin Analysis:** Measures skin moisture and oil levels directly[cite: 71].
* [cite_start]**Environmental Monitoring:** Actively tracks ambient UV index, temperature, and humidity to provide contextual advice[cite: 11, 12].
* [cite_start]**AI-Powered Recommendations:** A Feedforward Neural Network (FNN) classifies skin into one of 81 conditions to provide tailored routines[cite: 13, 172].
* [cite_start]**Dynamic Tips:** Offers real-time alerts, such as "Extreme UV risk: Apply SPF 50+ sunscreen"[cite: 331].
* [cite_start]**Web Interface:** A clean, browser-based UI to display sensor readings and recommendations[cite: 24, 25, 26].

---

## 📸 Screenshots

Here is a look at the web application interface.

| Environmental Tips | Skin Analysis |
| :---: | :---: |
|  |  |
| [cite_start]The app displays real-time UV, humidity, and temperature data[cite: 186]. | [cite_start]Users get a clear reading of their moisture and oil levels[cite: 210]. |

| Recommended Routine |
| :---: |
|  |
| [cite_start]The FNN output is mapped to a JSON file to provide a full morning and night routine[cite: 21, 213, 321]. |

---

## 🛠️ Tech Stack & Hardware

### Hardware Components
* [cite_start]**Microcontroller:** ESP32-WROOM-32 (for processing and Wi-Fi) [cite: 12, 79]
* [cite_start]**Moisture Sensor:** Capacitive Moisture Sensor [cite: 12, 81]
* [cite_start]**Color/Oil Sensor:** TCS3200 Color Sensor (calibrated to measure oil levels across 6 skin tones) [cite: 12, 83, 164, 166]
* **Environment Sensors:**
    * [cite_start]DHT11 (Temperature & Humidity) [cite: 12, 85]
    * [cite_start]GUVA-S12SD (UV Index) [cite: 12, 87]

### Software & Frameworks
* [cite_start]**Firmware:** Arduino IDE [cite: 150]
* [cite_start]**AI/ML Model:** TensorFlow / Keras [cite: 98]
* [cite_start]**Frontend:** React with Tailwind CSS [cite: 218]
* [cite_start]**Backend:** Node.js [cite: 219]
* [cite_start]**Build Tool:** Vite [cite: 219]

---

## 🏗️ System Architecture

### Hardware Architecture
[cite_start]The system is centered around the ESP32[cite: 80].
* [cite_start]The Capacitive Moisture Sensor connects to an ADC pin[cite: 91].
* [cite_start]The TCS3200, DHT11, and UV sensors connect to digital GPIO pins[cite: 92, 93].
* [cite_start]The ESP32 acquires data from all sensors and transmits it via Wi-Fi to the server for processing[cite: 13, 156].

[cite_start]*(For the complete circuit diagram, please see Fig. 1 in the project report[cite: 148].)*

### Model Architecture
[cite_start]We use a Feedforward Neural Network (FNN) built with TensorFlow/Keras[cite: 98]. The architecture is as follows:

| Layer Type | Output Shape | Activation | Additional Notes |
| :--- | :--- | :--- | :--- |
| Input | (3) | - | 3 input features |
| Dense | 64 | ReLU | [cite_start]First hidden layer [cite: 117, 118, 119, 130] |
| BatchNormalization | 64 | - | [cite_start]Normalizes activations [cite: 120, 121, 131] |
| Dropout | 64 | - | [cite_start]Dropout rate 0.2 [cite: 122, 123, 132] |
| Dense | 32 | ReLU | [cite_start]Second hidden layer [cite: 124, 127, 128, 133] |
| BatchNormalization | 32 | - | [cite_start]Normalizes activations [cite: 125, 129, 134] |
| **Dense (Output)** | **num\_classes (81)** | **Softmax** | [cite_start]**Multi-class output** [cite: 126, 135, 136, 137] |

[cite_start]*(Based on Fig. 2 in the project report [cite: 151])*

---

## 📈 Model Performance

[cite_start]The FNN model was trained to classify 81 unique skin conditions based on sensor inputs[cite: 13, 172]. [cite_start]The model performs strongly with a **Test Accuracy of 94%**[cite: 224].

| Model Accuracy | Model Loss |
| :---: | :---: |
|  |  |
| [cite_start]Accuracy vs. Epochs [cite: 238] | [cite_start]Loss vs. Epochs [cite: 315] |

---

## 🚀 Getting Started

### 1. Hardware Setup
[cite_start]Assemble the circuit as shown in the `Analog Report.pdf` (Fig. 1)[cite: 148].
1.  [cite_start]Connect the Capacitive Moisture Sensor, TCS3200, DHT11, and GUVA-S12SD sensor to the specified GPIO pins on the ESP32 [cite: 90-93].
2.  Power the ESP32 via its VIN pin.

### 2. Firmware
1.  [cite_start]Open the firmware code (located in the `/firmware` directory) using the Arduino IDE[cite: 150].
2.  Install the required libraries for the ESP32, DHT11, and TCS3200.
3.  Add your Wi-Fi credentials to the code.
4.  Flash the firmware to the ESP32 board.

### 3. Software (Backend & Frontend)
[cite_start]This project uses a Node.js backend and a React/Vite frontend[cite: 218, 219].

1.  **Install Backend Dependencies:**
    ```bash
    # From the root directory
    npm install
    ```
2.  **Install Frontend Dependencies:**
    ```bash
    cd src # or your frontend folder
    npm install
    ```
3.  **Run the Development Servers:**
    ```bash
    # Run the backend (from root)
    npm start # or 'node server.js'
    
    # Run the frontend (from 'src' folder)
    npm run dev
    ```
4.  Open your browser and navigate to the local address provided by Vite (e.g., `http://localhost:5173`).

### 4. Usage
1.  Power on the ESP32 hardware.
2.  [cite_start]Open the web application in your browser[cite: 24, 25].
3.  [cite_start]Select your base skin tone from the options[cite: 166, 196].
4.  [cite_start]Place the sensor device on your skin for approximately 5 seconds[cite: 154].
5.  [cite_start]View your real-time skin analysis (Moisture & Oil) and the personalized routine generated by the AI[cite: 24, 211].

---

## 👥 Authors

* [cite_start]**MR Bharath** [cite: 2]
* [cite_start]**Machavarapu Sriram** [cite: 5]
* [cite_start]**M Shreeram** [cite: 6]
* [cite_start]**Mahadev M** [cite: 8]

---

## 🙏 Acknowledgments

[cite_start]We would like to express our gratitude to Amrita Vishwa Vidyapeetham for providing the resources and support necessary to complete this project[cite: 367].

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
