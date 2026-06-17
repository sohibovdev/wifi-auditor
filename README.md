# Wi-Fi Password Strength Auditor & Simulator 📡

This project is a lightweight educational CLI tool written in Python, designed to simulate dictionary and brute-force attacks against WPA2 network configurations. 

It helps cybersecurity students and developers understand how weak network credentials can be easily matched against popular password leak databases without requiring any low-level hardware or root access.

> ⚠️ **IMPORTANT:** This tool is strictly for **educational and defensive training purposes**. It does not perform active wireless packet injection or target unauthorized third-party networks. It runs 100% locally and safely.

## ✨ Features
- 🚫 **No Root Required:** Safely tests password robustness without superuser or kernel-level permissions.
- ⏳ **Realistic Delay Emulation:** Simulates real network response verification speeds to demonstrate the time requirements of standard dictionary lookups.
- 🎨 **Clean Terminal UI:** Displays process tracking and vulnerability alerts using structured color-coded layouts.
- 🛡️ **Legal & Compliant:** Perfectly aligned with open educational frameworks and safety guidelines.

## 🛠️ Installation & Setup

The script requires Python 3 and the `colorama` library for ANSI terminal color support.

### 1. Install Required System Packages:
* **Linux (Ubuntu/Kali):**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip git -y
  ```
* **Termux:**
  ```bash
  pkg update
  pkg install python git -y
  ```

### 2. Clone the Repository & Configure Environment:
```bash
git clone https://github.com
cd wifi-auditor
pip install colorama
```

## 🚀 How to Run
Execute the interactive auditor script with standard user privileges:
```bash
python3 wifi_auditor.py
```

## 📝 Usage Parameters
Once the interface launches, follow the prompt:
1. Enter the target wireless network identifier (**SSID**).
2. Input the candidate password string to audit (Must be at least 8 characters to meet standard WPA2 length validation).
3. Analyze the vulnerability report outputted by the local dictionary checker simulator engine.
4. 
