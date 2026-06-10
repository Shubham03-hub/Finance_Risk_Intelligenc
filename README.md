# Finance Risk Intelligence

A machine learning platform for financial risk analysis — from raw data all the way to an interactive dashboard you can actually use.

---

## What This Project Does

Finance Risk Intelligence takes messy financial data and turns it into something useful. It walks through the full data science pipeline: cleaning your data, engineering the right features, training a model, and surfacing the results in a Streamlit dashboard where you can explore risk predictions and dig into what's driving them.

If you've ever wanted a project that ties together the whole ML workflow — not just model training in isolation — this is a good one to study or build on.

### What's Included

- Data cleaning and preprocessing
- A feature engineering pipeline
- Model training with multiple algorithm options
- An interactive Streamlit dashboard
- Risk predictions with probability scoring
- SHAP-based explainability so you can see *why* the model made a call
- Charts and visualizations throughout

---

## Project Layout

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

**Language:** Python 3.11+

**Data work:** Pandas, NumPy

**Modeling:** Scikit-Learn, XGBoost, CatBoost, SHAP

**Visualization:** Matplotlib, Seaborn, Plotly

**Dashboard:** Streamlit

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/Finance_Risk_Intelligence.git
cd Finance_Risk_Intelligence
```

### 2. Set up a virtual environment

**Windows:**
```powershell
python -m venv test_env
test_env\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv test_env
source test_env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

The project runs in four steps. Run them in order the first time.

### Step 1 — Clean the data

```bash
python src/data_cleaning.py
```

You should see:
```text
Data cleaning complete
```

### Step 2 — Engineer features

```bash
python src/feature_engineering.py
```

### Step 3 — Train the model

```bash
python src/train_model.py
```

This produces trained model files and evaluation output under `models/`.

### Step 4 — Launch the dashboard

```bash
python -m streamlit run streamlit_app/Home.py
```

Then open `http://localhost:8501` in your browser.

---

## How the Workflow Fits Together

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
Dashboard
```

Each step feeds into the next. If you want to swap in your own data, start at Step 1.

---

## Models You Can Use

- Logistic Regression
- Random Forest
- XGBoost
- CatBoost

The setup makes it straightforward to add other models if you want to experiment.

---

## What's in the Dashboard

**Home** — A summary of the dataset and overall risk picture.

**Analytics** — Feature distributions, correlation heatmaps, and risk segmentation breakdowns.

**Predictions** — Run predictions on individual records or upload a batch. Outputs include probability scores.

**Explainability** — SHAP value plots and feature importance charts so you can understand what the model is actually doing, not just what it outputs.

---

## Quick Reference

```powershell
# Activate environment (Windows)
test_env\Scripts\activate

# Run the full pipeline
python src\data_cleaning.py
python src\feature_engineering.py
python src\train_model.py

# Start the dashboard
python -m streamlit run streamlit_app/Home.py
```

---

## Common Issues

**`ModuleNotFoundError`**

Usually means dependencies aren't installed in the active environment:
```bash
pip install -r requirements.txt
```

Quick check:
```bash
python -c "import pandas, sklearn, streamlit; print('OK')"
```

---

**Streamlit not found**

```bash
pip install streamlit
python -m streamlit --version
```

---

**Something else seems off**

These commands help narrow things down:
```bash
python --version
python -m pip list
python -m pip check
```

---

## What's Next

A few directions this project could grow:

- Real-time risk scoring via an API (FastAPI would be a natural fit)
- Cloud deployment
- Scheduled model retraining as new data comes in
- User authentication for the dashboard
- More advanced explainability tooling

---

## About

Built by **Shubham Panchal** — working at the intersection of data analytics, machine learning, and finance.

[LinkedIn](https://linkedin.com/in/shubham-panchal-a100282a8)

---

## License

MIT — use it, modify it, learn from it. Attribution appreciated but not required.