from flask import Blueprint, request, jsonify

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    return jsonify({
        "disease": "Test Disease",
        "confidence": 0.90,
        "advice": "Test advice"
    })