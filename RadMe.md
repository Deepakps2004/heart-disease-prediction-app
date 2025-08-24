# ❤️ Heart Disease Prediction Web App

A simple Machine Learning project that predicts the likelihood of a patient having heart disease based on their medical data. The project uses a Logistic Regression model trained on the UCI Heart Disease dataset and serves the prediction through a user-friendly web interface built with Flask and styled with Tailwind CSS.

---

## ✨ Features

-   **Accurate Predictions:** Uses a trained Scikit-learn model to predict heart disease.
-   **User-Friendly Interface:** A clean, modern, and responsive UI with lively animations.
-   **Lightweight Backend:** Built with Flask, a simple and powerful Python web framework.
-   **Easy to Set Up:** Get the project running locally in just a few simple steps.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have **Python** installed on your system. You can download it from [python.org](https://www.python.org/).

### 🛠️ Installation Guide

1.  **Clone the Repository**
    First, clone this project to your local machine.
    ```bash
    git clone [https://github.com/your-username/heart-disease-prediction.git](https://github.com/your-username/heart-disease-prediction.git)
    cd heart-disease-prediction
    ```
    *(Note: Replace `your-username` with your actual GitHub username if you've uploaded it there. Otherwise, just navigate into your project folder.)*

2.  **Create a Virtual Environment**
    It's a best practice to create a virtual environment to keep project dependencies isolated.
    ```bash
    # For Windows
    python -m venv venv
    
    # For macOS/Linux
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment**
    You must activate the environment before installing packages.
    ```bash
    # For Windows
    .\venv\Scripts\activate
    
    # For macOS/Linux
    source venv/bin/activate
    ```

4.  **Install Required Packages**
    This project uses a few Python libraries. You can install them all at once using the `requirements.txt` file.

    First, create a file named `requirements.txt` in your project folder and add the following lines to it:
    ```
    Flask
    scikit-learn
    pandas
    numpy
    ```

    Now, run this command in your terminal to install them:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run the Application

With all the dependencies installed, you are now ready to run the web app!

1.  Make sure you are in the main project directory and your virtual environment is activated.
2.  Run the following command in your terminal:
    ```bash
    python app.py
    ```
3.  You will see an output message like this:
    ```
     * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```
4.  Open your web browser and go to the URL **http://127.0.0.1:5000**. 🌐

You should now see the web application running! Fill in the form with patient data and click "Get Prediction" to see the model in action.