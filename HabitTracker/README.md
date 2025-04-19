# ⏱️ Coding Time Tracker with Pixela

This Python script helps you track your daily coding time by logging it to a [Pixela](https://pixe.la/) graph. It uses a simple GUI prompt to collect your coding hours and records them visually on your Pixela dashboard.

## 📌 Description

- Logs daily coding hours using the Pixela API.
- Uses a `tkinter` dialog for input.
- Sends data in Pixela's required format (`YYYYMMDD`).
- Shows your coding time as a pixel graph online.

## 🧰 Requirements

- Python 3.x
- `requests` library
- `tkinter` (usually pre-installed with Python)

## 💻 How to Run

1. Install `requests`:
   ```bash
   pip install requests
   ```

2. Set your Pixela credentials in the script:
   ```python
   USERNAME = "your_username"
   TOKEN = "your_token"
   graph_id = "your_graph_id"
   ```

3. Run the script:
   ```bash
   python your_script_name.py
   ```

4. Enter your coding time (in hours) in the popup window.
5. The data will be logged to your Pixela graph.

## 🔗 View Your Graph

Use this link format to view your graph online:

```
https://pixe.la/v1/users/<your_username>/graphs/<your_graph_id>.html
```

**Example (from this script):**
```
https://pixe.la/v1/users/khyathi/graphs/user1.html
```

## 🧪 Features

- 📅 Logs daily coding time
- 💬 GUI prompt using `tkinter`
- 📈 Visual dashboard using Pixela
- 🔐 Uses secure token headers

## 🛑 Limitations

> ⚠️ To access full features like graph customization, webhooks, integrations, and more storage, you need to purchase the **Pixela Premium Plan**.

## 🔄 Optional Pixela Setup (uncomment in script)

- **Create User**:
   ```python
   requests.post(url=user_endpoint, json=user_parameters)
   ```

- **Create Graph**:
   ```python
   requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
   ```

## 📅 Date Format Used

Pixela accepts only this format for the date:

```
YYYYMMDD
```

Generated in the script with:
```python
datetime.now().strftime("%Y%m%d")
```

## ✅ Example Output

On running, you’ll get a popup asking:
```
Enter today's coding time (In Hours):
```

Then the result will be posted to your graph and you’ll see a response like:
```json
{"message":"Success","isSuccess":true}
```
