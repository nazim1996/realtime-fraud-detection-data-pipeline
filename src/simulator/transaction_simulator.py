import pandas as pd;
import time;

df = pd.read_csv('')

def transaction_stream():
    for _, row in df.iterrows():
        transaction = row.drop("Class").to_dict()
        yield transaction
        time.sleep(1)