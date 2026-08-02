import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, recall_score
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

print("--- Part 2: Model Training Pipeline ---")

# 1. Dataset Load કરવો
try:
    df = pd.read_csv(gtu_student_data_v3.csv')
    
    # Features (X) અને Target (y)
    X = df[['SPI_trend', 'prev_SPI_avg', 'Mid%']]
    y = df['AT_risk']

    # 2. Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Class Imbalance (SMOTE)
    smote = SMOTE(k_neighbors=1, random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)

    # 5. XGBoost Model Training
    xgb = XGBClassifier(random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1]
    }

    grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, scoring='recall', cv=3)
    grid_search.fit(X_train_res, y_train_res)
    best_model = grid_search.best_estimator_

    # 6. Evaluation
    y_pred = best_model.predict(X_test_scaled)
    print("\n=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print(f"Recall Score: {recall_score(y_test, y_pred):.2f}")

    # 7. Model and Scaler Save કરવો
    joblib.dump(best_model, 'at_risk_model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    print("\n✅ Success: 'at_risk_model.joblib' અને 'scaler.joblib' સેવ થઈ ગયા છે!")

except FileNotFoundError:
    print("⚠️ અત્યારે ડેટાસેટ ફાઈલ (gtu_student_data.csv) મળી નથી.")




