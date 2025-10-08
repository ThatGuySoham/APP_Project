
# 🚦 AATOS – Artificially Augmented Traffic Observation System

## 📌 Overview
AATOS is a **smart traffic management system** that uses **YOLOv11 for car detection** and provides **dynamic traffic signal control** at a 4-way junction.

- 🚗 Vehicle detection using **YOLOv11**
- ⏱️ Variable green light timing based on traffic density
- 🤖 Optional **LLM-powered decision making** for adaptive policies
- 🔧 Future-ready for **hardware integration (Raspberry Pi/Arduino + LEDs)**

---


## ⚡ Installation
```
git clone https://github.com/yourusername/AATOS.git
cd AATOS
pip install -r requirements.txt
```

## ▶️ Usage
# Run rule-based system:
```
python main.py
```

# Run with LLM decisions (requires OpenAI API key):
```
python main.py --llm
```


## 🚀 Example Output
```
North: 🚗 12 cars → Green 35s
North: 🟡 Yellow 2s
North: 🔴 Red

East: 🚗 3 cars → Green 10s
...
=======
```
<img width="1902" height="579" alt="image" src="https://github.com/user-attachments/assets/4bd9ed94-e766-423f-a46e-60b2b50db23e" />

<img width="1900" height="844" alt="image" src="https://github.com/user-attachments/assets/b05d89e4-9848-43a2-87c0-ca9131d38ba9" />


