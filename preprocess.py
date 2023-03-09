import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocessor(df, tort):
    train_df, test_df = train_test_split(df, test_size=0.30, random_state=123)
    train_df['target'] = np.where(train_df['quality'] > 5, 1, 0)
    test_df['target'] = np.where(test_df['quality'] > 5, 1, 0)

    if tort == 0:
        return train_df
    elif tort == 1:
        return test_df