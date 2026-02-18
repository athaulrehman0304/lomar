# LoMar: Malicious Content Detection System

## Overview
LoMar is a Django-based web application designed to detect and classify malicious content (poisoning attacks) in text data. It leverages machine learning algorithms to analyze user inputs and determine if they exhibit characteristics of known attack patterns.

## Features
*   **User Role Management**: Separate portals for Remote Users (Clients) and Service Providers (Admins).
*   **Machine Learning Integration**: Utilizes Scikit-learn to train and deploy models.
*   **Ensemble Learning**: Implements a Voting Classifier combining:
    *   Naive Bayes
    *   Support Vector Machine (SVM)
    *   Logistic Regression
    *   Decision Tree/Extra Tree
*   **Data Visualization**: Displays detection accuracy and ratios.

## Tech Stack
*   **Backend**: Python, Django
*   **Frontend**: HTML, CSS
*   **Machine Learning**: Scikit-Learn, Pandas, NumPy
*   **Database**: SQLite

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/lomar.git
    cd lomar
    ```

2.  **Create a Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install django pandas scikit-learn numpy xlwt
    ```

4.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```

6.  **Access the App**:
    Open your browser and go to `http://127.0.0.1:8000/`

## Usage
1.  **Register a User**: Create a new account to test the detection features.
2.  **Login as Admin**: Access the Service Provider dashboard (credentials required) to train the model on the `Datasets.csv` file.
3.  **Predict**: Input text data to see if the system classifies it as a poisoning attack.

## Disclaimer
This project is a prototype for educational purposes. It implements a centralized simulation of poisoning attack detection.
