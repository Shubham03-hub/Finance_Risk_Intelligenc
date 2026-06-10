import os
import pandas as pd

def load_data():

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

    data_path = os.path.join(
        base_dir,
        "data",
        "processed",
        "final_features.csv"
    )

    return pd.read_csv(data_path)

from streamlit_app.utils.load_data import load_data

df = load_data()