import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt
from time import sleep
import numpy as np
from sklearn.preprocessing import label_binarize

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("games.csv")
        return df
    except FileNotFoundError:
        st.error("Please ensure 'games.csv' is in the same directory.")
        st.stop()

# Preprocess data
@st.cache_data
def preprocess_data(df):
    df['rating_diff'] = df['white_rating'] - df['black_rating']
    df['game_duration'] = (((df['last_move_at'] - df['created_at']) / 60) / 60) / 24  # Convert to days

    def handle_outliers_iqr(df, column):
        Q1, Q3 = df[column].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)
        return df

    numerical_cols = ['white_rating', 'black_rating', 'turns', 'opening_ply', 'rating_diff', 'game_duration']
    for col in numerical_cols:
        df = handle_outliers_iqr(df, col)

    le = LabelEncoder()
    df['winner'] = le.fit_transform(df['winner'])  # 0: Draw, 1: Black, 2: White

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df, le, scaler

# Train and save model
def train_and_save_optimized_model(X_train, y_train, model_path='optimized_chess_model.pkl'):
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
    }
    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

    # Training progress bar
    progress_bar = st.progress(0)
    st.write("Training model with GridSearchCV... Please wait.")
    for percent_complete in range(0, 101, 10):
        sleep(0.5)
        progress_bar.progress(percent_complete)

    grid_search.fit(X_train, y_train)

    # Save best model
    with open(model_path, 'wb') as f:
        pickle.dump(grid_search.best_estimator_, f)

    st.success(f"Optimized model saved to '{model_path}'!")
    st.write(f"Best Parameters: {grid_search.best_params_}")

# Load model
def load_model(model_path='optimized_chess_model.pkl'):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        st.success("Pre-trained model loaded successfully!")
        return model
    except FileNotFoundError:
        st.error(f"No model found at {model_path}. Please train and save the model first.")
        st.stop()

# Visualization Functions
def plot_confusion_matrix(y_test, y_pred, class_names):
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)

def plot_feature_importance(model, feature_names):
    importance = model.feature_importances_
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
    ax.set_title("Feature Importance")
    st.pyplot(fig)

def plot_roc_curve(y_test, y_pred_prob, classes):
    y_test_bin = label_binarize(y_test, classes=[0, 1, 2])  # Multiclass binarization

    fig, ax = plt.subplots(figsize=(8, 6))
    for i in range(len(classes)):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_prob[:, i])
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, lw=2, label=f'Class {classes[i]} ROC curve (area = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('ROC Curve - Multiclass')
    ax.legend(loc='lower right')
    st.pyplot(fig)

# Display model evaluation
def display_model_evaluation(accuracy, classification_report_dict):
    st.subheader("Model Evaluation")
    st.metric(label="Accuracy", value=accuracy)

    st.subheader("Classification Report")
    df = pd.DataFrame(classification_report_dict).transpose().astype(float)
    st.dataframe(df.style.background_gradient(axis=0), width=800)

    st.subheader("Averages")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Macro Avg:**")
        st.dataframe(df.loc[['macro avg']].style.background_gradient(axis=1), width=400)
    with col2:
        st.write("**Weighted Avg:**")
        st.dataframe(df.loc[['weighted avg']].style.background_gradient(axis=1), width=400)

# Perform ML modeling and predictions
def perform_ml_modeling():
    st.title("Machine Learning Model - Chess Outcome Prediction (Optimized)")

    # Load and preprocess data
    df = load_data()
    df, le, scaler = preprocess_data(df)

    # Prepare training and testing sets
    X = df.drop(['rated', 'opening_name', 'opening_eco', 'increment_code', 'winner', 'id', 'white_id', 'black_id', 'moves', 'created_at', 'last_move_at', 'victory_status'], axis=1)
    y = df['winner']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model_path = 'optimized_chess_model.pkl'

    if "model" not in st.session_state:
        st.session_state.model = None

    if "is_trained" not in st.session_state:
        st.session_state.is_trained = False

    if "is_loaded" not in st.session_state:
        st.session_state.is_loaded = False

    # Training and loading buttons
    if st.button("Train and Save Optimized Model"):
        train_and_save_optimized_model(X_train, y_train, model_path)
        st.session_state.is_trained = True
        st.session_state.is_loaded = False

    if st.button("Load Pre-Trained Model"):
        model = load_model(model_path)
        st.session_state.model = model
        st.session_state.is_loaded = True
        st.session_state.is_trained = False

    # Ensure model is loaded or trained before proceeding with predictions
    if st.session_state.is_loaded or st.session_state.is_trained:
        model = st.session_state.model

        if st.session_state.is_trained or st.session_state.is_loaded:
            y_pred = model.predict(X_test)
            y_pred_prob = model.predict_proba(X_test)

            # Model evaluation and visualization
            display_model_evaluation(accuracy_score(y_test, y_pred), classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True))

            st.write("### Visualizations")

            # Show visualizations after model is loaded
            if st.button("Show Confusion Matrix"):
                plot_confusion_matrix(y_test, y_pred, class_names=le.classes_)

            if st.button("Show Feature Importance"):
                plot_feature_importance(model, X.columns)

            if st.button("Show ROC Curve"):
                plot_roc_curve(y_test, y_pred_prob, classes=le.classes_)

if __name__ == "__main__":
    perform_ml_modeling()
