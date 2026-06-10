# Finance Risk Intelligence

A machine learning-powered financial risk analysis platform that performs data preprocessing, feature engineering, model training, and interactive risk visualization through a Streamlit dashboard.

---

## Project Overview

Finance Risk Intelligence is an end-to-end data science project designed to identify and analyze financial risk using machine learning techniques. The platform automates the workflow from raw data processing to predictive modeling and dashboard visualization.

### Key Features

* Data cleaning and preprocessing
* Feature engineering pipeline
* Machine Learning model training
* Interactive Streamlit dashboard
* Risk prediction and analysis
* Data visualization and reporting
* Support for multiple ML algorithms

---

## Project Structure

```text
Finance_Risk_Intelligence/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── engineered/
│
├── models/
│   └── trained_model.pkl
│
├── notebooks/
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── train_model.py
│
├── streamlit_app/
│   ├── Home.py
│   └── pages/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

### Programming Language

* Python 3.11+

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* XGBoost
* CatBoost
* SHAP

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Dashboard

* Streamlit

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Finance_Risk_Intelligence.git

cd Finance_Risk_Intelligence
```

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv test_env

test_env\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv test_env

source test_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Data Cleaning

**File:**

```text
src/data_cleaning.py
```

Run:

```bash
python src/data_cleaning.py
```

Expected Output:

```text
Data cleaning complete
```

---

### Step 2: Feature Engineering

**File:**

```text
src/feature_engineering.py
```

Run:

```bash
python src/feature_engineering.py
```

---

### Step 3: Train Model

**File:**

```text
src/train_model.py
```

Run:

```bash
python src/train_model.py
```

This step generates trained models and evaluation results.

---

### Step 4: Launch Dashboard

**File:**

```text
streamlit_app/Home.py
```

Run:

```bash
python -m streamlit run streamlit_app/Home.py
```

Open:

```text
http://localhost:8501
```

---

## Machine Learning Workflow

```text
Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Model Training
    ↓
Risk Prediction
    ↓
Dashboard Visualization
```

---

## Models Supported

* Logistic Regression
* Random Forest
* XGBoost
* CatBoost

Model selection can be extended based on project requirements.

---

## Dashboard Features

### Home

* Project overview
* Dataset summary
* Risk insights

### Analytics

* Feature distributions
* Correlation analysis
* Risk segmentation

### Predictions

* Individual risk prediction
* Batch prediction
* Probability scoring

### Explainability

* SHAP value analysis
* Feature importance visualization

---

## Example Commands

```powershell
# Activate environment
test_env\Scripts\activate

# Run pipeline
python src\data_cleaning.py
python src\feature_engineering.py
python src\train_model.py

# Launch dashboard
python -m streamlit run streamlit_app/Home.py
```

---

## Troubleshooting

### ModuleNotFoundError

Install dependencies:

```bash
pip install -r requirements.txt
```

Verify:

```bash
python -c "import pandas, sklearn, streamlit; print('OK')"
```

Expected:

```text
OK
```

---

### Streamlit Not Found

Install Streamlit:

```bash
pip install streamlit
```

Verify:

```bash
python -m streamlit --version
```

---

### Check Environment

```bash
python --version
python -m pip list
python -m pip check
```

---

## Future Enhancements

* Real-time financial risk scoring
* API deployment with FastAPI
* Cloud deployment
* Automated model retraining
* User authentication
* Advanced explainable AI modules

---

## Author

**Shubham Panchal**

Data Analytics | Data Science | Machine Learning | Business Intelligence | Finance Risk Intelligence Project

LinkedIn:
https://linkedin.com/in/shubham-panchal-a100282a8 


---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational and research purposes.
