from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

MODEL_PATH = os.environ.get("MODEL_PATH", "phishguard_pipeline.joblib")

app = Flask(__name__)
CORS(app)

# Lazy load model
_model = None
def get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please run train.py first.")
        _model = joblib.load(MODEL_PATH)
    return _model

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True) or {}
    text = data.get("text", "")
    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Missing 'text' field or empty string."}), 400

    model = get_model()
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba([text])[0]
        pred = model.classes_[proba.argmax()]
        confidence = float(proba.max())
    else:
        pred = model.predict([text])[0]
        confidence = None

    return jsonify({
        "prediction": str(pred),
        "confidence": confidence,
    }), 200

if __name__ == "__main__":
    # Run on 0.0.0.0 for container/cloud friendliness
    app.run(host="0.0.0.0", port=5000, debug=True)
