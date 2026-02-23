# LoMar – Web-based Malicious Content Detection System

LoMar is a **Django-based Machine Learning web application** used to detect and analyze **poisoning attacks in datasets**.  
The system allows users to train ML models, predict attack status, and visualize results through a web dashboard.

---

## Live Deployment

🔗 **Deployed Application:**  
https://lomar-production.up.railway.app

🔗 **GitHub Repository:**  
https://github.com/athaulrehman0304/lomar

---

## Project Overview

Poisoning attacks occur when malicious or incorrect data is injected into training datasets, leading to inaccurate model predictions.

LoMar helps in:
- Detecting poisoning attack patterns
- Predicting attack status using Machine Learning
- Visualizing results using charts
- Managing users with role-based access

---

## Key Features

- User authentication and role-based access
- Machine learning model training
- Poisoning attack status prediction
- Data visualization using charts and graphs
- Downloadable prediction results
- Web-based interface built with Django

---

## Tech Stack

- **Backend:** Python, Django
- **Machine Learning:** NumPy, Matplotlib
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Server:** Gunicorn
- **Deployment:** Railway

---


## How to Run Locally

```bash
git clone https://github.com/athaulrehman0304/lomar.git
cd lomar
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
6.  **Access the App**:
    Open your browser and go to `http://127.0.0.1:8000/`
```

## Usage
1.  **Register a User**: Create a new account to test the detection features.
2.  **Login as Admin**: Access the Service Provider dashboard (credentials required) to train the model on the `Datasets.csv` file.
3.  **Predict**: Input text data to see if the system classifies it as a poisoning attack.

## Disclaimer
This project is a prototype for educational purposes. It implements a centralized simulation of poisoning attack detection.
