"""
ml_model.py
Machine Learning component of the AI-Generated Workout Routine system.
"""

import random
import pickle
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from exercise_db import EXERCISES, INJURY_ZONES, SEVERITY_LEVELS

IMPACT_MAP = {"low": 0, "medium": 1, "high": 2}
SEVERITY_MAP = {"mild": 1, "moderate": 2, "severe": 3}

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "safety_model.pkl")


def featurize(exercise, injury_zone, severity):
    tag = f"{injury_zone}_{severity}" if injury_zone != "none" else "none"
    is_contra = 1 if tag in exercise["contraindicated_for"] else 0
    is_rehab = 1 if tag in exercise["rehab_for"] else 0
    severity_score = SEVERITY_MAP.get(severity, 0)
    impact_score = IMPACT_MAP.get(exercise["impact_level"], 1)
    difficulty = exercise["difficulty"]

    return [
        impact_score,
        difficulty,
        severity_score,
        is_contra,
        is_rehab,
        impact_score * severity_score,
    ]


def rule_based_label(exercise, injury_zone, severity):
    tag = f"{injury_zone}_{severity}" if injury_zone != "none" else "none"
    if tag in exercise["contraindicated_for"]:
        return 0
    return 1


def build_training_data(n_synthetic_noise=40, seed=42):
    random.seed(seed)
    X, y = [], []

    for ex in EXERCISES:
        for zone in INJURY_ZONES:
            if zone == "none":
                X.append(featurize(ex, "none", "mild"))
                y.append(1)
                continue
            for sev in SEVERITY_LEVELS:
                X.append(featurize(ex, zone, sev))
                y.append(rule_based_label(ex, zone, sev))

    for _ in range(n_synthetic_noise):
        ex = random.choice(EXERCISES)
        zone = random.choice(INJURY_ZONES[:-1])
        sev = random.choice(SEVERITY_LEVELS)
        feats = featurize(ex, zone, sev)
        label = rule_based_label(ex, zone, sev)
        if random.random() < 0.15:
            label = 1 - label
        X.append(feats)
        y.append(label)

    return np.array(X), np.array(y)


def train_and_save_model():
    X, y = build_training_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=200, max_depth=6, random_state=42, class_weight="balanced"
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=["unsafe", "safe"])

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(clf, f)

    return clf, acc, report


def load_model():
    if not os.path.exists(MODEL_PATH):
        clf, _, _ = train_and_save_model()
        return clf
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def predict_safety_score(clf, exercise, injury_zone, severity):
    feats = np.array([featurize(exercise, injury_zone, severity)])
    proba = clf.predict_proba(feats)[0]
    classes = list(clf.classes_)
    safe_idx = classes.index(1)
    return proba[safe_idx]


if __name__ == "__main__":
    clf, acc, report = train_and_save_model()
    print(f"Model trained. Test accuracy: {acc:.3f}\n")
    print(report)
