# 🛰️ ISS Overhead Notifier (Python)

This Python script checks if the International Space Station (ISS) is currently flying over your location **during nighttime**, and sends you an email alert if it is. Built using real-time APIs and basic automation techniques.

---

## 🚀 Features

- Tracks ISS real-time position using Open Notify API
- Detects local sunrise and sunset using Sunrise-Sunset API
- Sends automated email alert when ISS is overhead at night
- Runs in a loop, checking every 20 seconds

---


---

## 🛠️ Requirements

- Python 3.x
- Modules:
  - `requests`
  - `datetime`
  - `smtplib`
  - `time`

Install required modules using:

```bash
pip install requests

