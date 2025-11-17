# Simple supervised learning workflow (classification) 
# Dataset: Breast cancer (diagnostic) from scikit-learn
# Task: Predict whether a tumor is malignant (0) or benign (1)
# To install dependencies (in your environment/terminal):
#   pip install scikit-learn xgboost

from collections import Counter
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from xgboost import XGBClassifier

# -------------------------------------------------
# 1. Load the healthcare dataset
# -------------------------------------------------

data = load_breast_cancer()

X = data.data           # features (measurements from the tumor)
y = data.target         # labels: 0 = malignant, 1 = benign
feature_names = data.feature_names
target_names = data.target_names

print("Step 1: Load data")
print("  Feature matrix shape:", X.shape)
print("  Target vector shape:", y.shape)
print("  Classes:", target_names)

n_total = len(y)
print("  Total number of samples:", n_total)

# -------------------------------------------------
# 2. Split into train / validation / test
# -------------------------------------------------
#
# GOAL: End up with approximately:
#   - 60% of data for TRAINING (model learns here)
#   - 20% for VALIDATION (model selection / hyperparameter tuning)
#   - 20% for TEST (held out until the very end)
#
# We do this in TWO STEPS:
#
#   STEP 2a: First split
#       - Take original data
#       - Set aside 20% as TEST (never touch until the end)
#       - Remaining 80% is TEMP data we will later split into TRAIN and VAL
#
#   STEP 2b: Second split
#       - Take that 80% TEMP (train+val) data
#       - Split it into:
#           75% TRAIN  (of TEMP)
#           25% VAL    (of TEMP)
#       - In terms of the ORIGINAL dataset:
#           TRAIN = 0.8 * 0.75 = 0.60  (60%)
#           VAL   = 0.8 * 0.25 = 0.20  (20%)
#           TEST  = 0.2                (20%)

print("\nStep 2: Split data into train / validation / test sets")

# ---------- STEP 2a: train+val vs test ----------
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X,
    y,
    test_size=0.2,       # 20% reserved as TEST
    stratify=y,
    random_state=42,
)

n_trainval = len(y_trainval)
n_test = len(y_test)

print("    Train+Val samples:", n_trainval, f"({n_trainval / n_total:.1%}) of total")
print("    Test samples:     ", n_test,      f"({n_test / n_total:.1%}) of total")

# ---------- STEP 2b: train vs validation ----------
# We now split the 80% (trainval) into train and val.
# test_size=0.25 here means:
#   - 25% of 80% = 20% of original -> Validation
#   - 75% of 80% = 60% of original -> Training

X_train, X_val, y_train, y_val = train_test_split(
    X_trainval,
    y_trainval,
    test_size=0.25,      # 25% of TRAIN+VAL becomes VALIDATION
    stratify=y_trainval,
    random_state=42,
)

n_train = len(y_train)
n_val = len(y_val)

print("    Train samples:    ", n_train, f"({n_train / n_total:.1%}) of total")
print("    Validation samples:", n_val,   f"({n_val / n_total:.1%}) of total")


# -------------------------------------------------
# 3. Baseline "non-ML" model: most common class
# -------------------------------------------------
#
# WHY?
#   - We want a very simple, "dumb" baseline that does *not* use any features.
#   - This shows how well we would do with almost no intelligence at all.
#
# WHAT IS THE MAJORITY-CLASS BASELINE?
#   - Look at the labels in the training set (y_train).
#   - Count how many examples of each class we have.
#   - Pick the class that appears most often (the majority class).
#   - Our "model" will always predict that one class, no matter what the input is.
#
# EXAMPLE:
#   - Suppose in y_train: 60% are benign, 40% malignant.
#   - Majority class = benign.
#   - Baseline model: for every patient, we predict "benign".
#   - That gives ~60% accuracy without using X at all.

# 3a. Look at class distribution in the training labels
class_counts = Counter(y_train)
print("  Class counts in y_train:", class_counts)
for class_id, count in class_counts.items():
    print(f"    Class {class_id} ({target_names[class_id]}): {count} examples")

# 3b. Find the most common (majority) class
most_common_class = class_counts.most_common(1)[0][0]
print("\n  Most common class in training data:",
      most_common_class,
      f"-> '{target_names[most_common_class]}'")

# 3c. Create baseline predictions by filling arrays with the majority class
baseline_val_pred = np.full(shape=(len(y_val),), fill_value=most_common_class)
baseline_test_pred = np.full(shape=(len(y_test),), fill_value=most_common_class)

# 3d. Evaluate baseline on validation set
print("\n=== Baseline (most common class) – Validation ===")
print("Accuracy:", round(accuracy_score(y_val, baseline_val_pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_val, baseline_val_pred))
print(
    "Classification report:\n",
    classification_report(
        y_val,
        baseline_val_pred,
        digits=3,
        target_names=target_names,
    ),
)

# 3e. Evaluate baseline on test set
print("\n=== Baseline (most common class) – Test ===")
print("Accuracy:", round(accuracy_score(y_test, baseline_test_pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_test, baseline_test_pred))
print(
    "Classification report:\n",
    classification_report(
        y_test,
        baseline_test_pred,
        digits=3,
        target_names=target_names,
    ),
)

# -------------------------------------------------
# 4. XGBoost classifier (ML model)
# -------------------------------------------------
#
# Now we build a *real* ML model that uses the features X to try
# to beat the baseline.
#
# In a more advanced setting, we would:
#   - Use the validation set to tune hyperparameters.
#   - Possibly try multiple models (logistic regression, random forest, etc.).
# Here we just choose some reasonable hyperparameters to keep it simple.

print("\nStep 4: Train an XGBoost model (a real ML model)")

xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42,
    n_jobs=-1,
)

print("  Fitting XGBoost model on the TRAIN data...")
xgb_model.fit(X_train, y_train)

# Predictions on validation set (for model selection / hyperparameter tuning)
xgb_val_pred = xgb_model.predict(X_val)

print("\n=== XGBoost – Validation ===")
print("Accuracy:", round(accuracy_score(y_val, xgb_val_pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_val, xgb_val_pred))
print(
    "Classification report:\n",
    classification_report(
        y_val,
        xgb_val_pred,
        digits=3,
        target_names=target_names,
    ),
)

# Final evaluation on the held-out test set
xgb_test_pred = xgb_model.predict(X_test)

print("\n=== XGBoost – Test (Final model performance) ===")
print("Accuracy:", round(accuracy_score(y_test, xgb_test_pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_test, xgb_test_pred))
print(
    "Classification report:\n",
    classification_report(
        y_test,
        xgb_test_pred,
        digits=3,
        target_names=target_names,
    ),
)
