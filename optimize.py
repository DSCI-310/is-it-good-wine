import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier
from IPython import display
from pipeline import pipe_build

def hp_optimizer(model, X_train, y_train):
    if model == 'lr':
        scores_dict = {
        "C": 10.0**np.arange(-4, 6, 1),
        "mean_train_scores": list(),
        "mean_cv_scores": list(),
        }
        for C in scores_dict["C"]:
            pipe = make_pipeline(StandardScaler(),
                                 LogisticRegression(C=C, random_state=1234))
            scores = cross_validate(pipe, X_train, y_train, return_train_score=True)
            scores_dict["mean_train_scores"].append(scores["train_score"].mean())
            scores_dict["mean_cv_scores"].append(scores["test_score"].mean())

        results_df = pd.DataFrame(scores_dict)
        return results_df

    elif model == 'svm':
        best_score = 0

        param_grid = {
        "C": [0.001, 0.01, 0.1, 1, 10, 100],
        "gamma": [0.001, 0.01, 0.1, 1, 10, 100],
        }

        for gamma in param_grid["gamma"]:
            for C in param_grid["C"]:
                pipe_svc = make_pipeline(
                    StandardScaler(),
                    SVC(gamma=gamma, C=C, class_weight='balanced', random_state=1234))
                scores = cross_val_score(pipe_svc, X_train, y_train, cv=5)
                mean_score = np.mean(scores)
                if (mean_score > best_score):
                    best_score = mean_score
                    best_parameters = {"C": C, "gamma": gamma}

        print(best_parameters, ", best_score:", best_score)

    elif model == 'dtc':
        best_score = 0

        param_grid = {"max_depth": np.arange(1, 20, 2)}

        results_dict = {"max_depth": [], "mean_cv_score": []}
        for depth in param_grid["max_depth"]:
            dtc = DecisionTreeClassifier(max_depth=depth, class_weight='balanced')
            scores = cross_val_score(dtc, X_train, y_train)
            mean_score = np.mean(scores)

            if (mean_score > best_score):
                best_score = mean_score
                best_params = {"max_depth": depth}
                
            results_dict["max_depth"].append(depth)
            results_dict["mean_cv_score"].append(mean_score)

        results_df = pd.DataFrame(results_dict)
        return results_df