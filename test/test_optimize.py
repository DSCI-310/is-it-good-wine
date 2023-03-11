import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from optimize import hp_optimizer




# dummy data
X_train, y_train = make_moons(n_samples = 100)


# test whether the function returns hyperparameter and validation score
def test_hp_optimizer():
    actual_lr = hp_optimizer("lr", X_train, y_train)
    assert list(actual_lr.columns) == ['C', 'mean_train_scores', 'mean_cv_scores']
    actual_dtc = hp_optimizer('dtc', X_train, y_train)
    assert list(actual_dtc.columns) == ['max_depth', 'mean_cv_score']
    actual_svm = hp_optimizer('svm', X_train, y_train)