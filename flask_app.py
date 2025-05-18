from flask import Flask, request, jsonify
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

class DropoutPredictor:
    def __init__(self, model_path, scaler_path, encoders_path, feature_order_path):
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
        self.encoders = joblib.load(encoders_path)
        self.feature_order = joblib.load(feature_order_path)

    def preprocess(self, data):
        df = pd.DataFrame([data])

        # Encode categorical columns using saved encoders
        for col, le in self.encoders.items():
            if col in df.columns:
                df[col] = le.transform(df[col])

        # Ensure correct column order and presence
        df = df[self.feature_order]

        # Scale features
        X_scaled = self.scaler.transform(df)
        return X_scaled

    def predict(self, data):
        X = self.preprocess(data)
        prob = self.model.predict(X)[0][0]
        prediction = int(prob > 0.5)
        return prob, prediction

# Initialize Flask app and predictor
app = Flask(__name__)
predictor = DropoutPredictor(
    model_path='models/edupulse_model.h5',
    scaler_path='models/scaler.save',
    encoders_path='models/encoders.save',
    feature_order_path='models/feature_order.save'
)

@app.route('/predict_dropout', methods=['POST'])
def predict_dropout():
    try:
        data = request.get_json()
        print("📥 Received data:", data)  # Debug input

        # Sanity check keys
        required_keys = ['Age', 'Gender', 'Education_Level', 'Time_Spent_on_Videos',
                         'Quiz_Attempts', 'Quiz_Scores', 'Assignment_Completion_Rate', 'Engagement_Level']

        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing key in input: {key}")

        prob, pred = predictor.predict(data)

        print(f"✅ Prediction complete: {pred}, Probability: {prob}")
        return jsonify({
            'dropout_probability': float(prob),
            'dropout_prediction': int(pred)
        })

    except Exception as e:
        print("❌ Error during prediction:", str(e))
        return jsonify({'error': str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)