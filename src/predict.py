from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_FILE = PROJECT_ROOT / "models" / "xgboost.pkl"

if __name__ == "__main__":
    predict()