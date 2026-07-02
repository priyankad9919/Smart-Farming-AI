import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ===================================================
# LOAD DATASET
# ===================================================

df = pd.read_csv("Crop_recommendation.csv")


# ===================================================
# FEATURES AND TARGET
# ===================================================

X = df[['N', 'P', 'K', 'temperature',
        'humidity', 'ph', 'rainfall']]

y = df['label']


# ===================================================
# SPLIT DATA
# ===================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ===================================================
# TRAIN MODEL
# ===================================================

print("Training model...\n")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# ===================================================
# TEST MODEL
# ===================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("Model Accuracy : {:.2f}%".format(accuracy * 100))
print("=" * 50)

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))


# ===================================================
# SAVE MODEL
# ===================================================

joblib.dump(model, "model.pkl")

print("\nModel saved successfully as model.pkl")