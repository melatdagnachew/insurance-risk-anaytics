import numpy as np

from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluate_regression(
    y_true,
    y_pred
):
    """
    Evaluate regression models using RMSE and R².
    """

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "RMSE": rmse,
        "R2": r2
    }


def evaluate_classification(
    y_true,
    y_pred
):
    """
    Evaluate classification models.
    """

    return {
        "Accuracy": accuracy_score(
            y_true,
            y_pred
        ),

        "Precision": precision_score(
            y_true,
            y_pred
        ),

        "Recall": recall_score(
            y_true,
            y_pred
        ),

        "F1": f1_score(
            y_true,
            y_pred
        )
    }
