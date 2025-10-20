import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

def main():
    df = pd.read_csv("sample_data.csv")
    X = df["text"].astype(str)
    y = df["label"].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

    # Pipeline: TF-IDF + Logistic Regression
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
        ("clf", LogisticRegression(max_iter=200, n_jobs=None, class_weight="balanced"))
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy:", acc)
    print(classification_report(y_test, y_pred))

    # Persist the entire pipeline (vectorizer + model)
    joblib.dump(pipe, "phishguard_pipeline.joblib")
    print("Saved model to phishguard_pipeline.joblib")

if __name__ == "__main__":
    main()
