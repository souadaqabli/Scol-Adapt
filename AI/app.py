from flask import Flask, request, jsonify
from train import train_model
from predict import create_prediction_interface
from recommandation import generate_recommendation
from data import load_and_prepare_data

app = Flask(__name__)

# Route pour entraîner le modèle
@app.route('/train', methods=['POST'])
def train():
    # Chargez les données et entraînez le modèle
    X, y, _, _ = load_and_prepare_data('Mental disorder symptoms.xlsx')  # Utilisez le chemin approprié
    model = train_model(X, y)  # Utilisez votre fonction d'entraînement du modèle
    return jsonify({"message": "Modèle entraîné avec succès."}), 200

# Route pour faire une prédiction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = data.get('input_data')

    if input_data is None:
        return jsonify({"error": "Aucune donnée d'entrée fournie."}), 400

    prediction = make_prediction(input_data)  # Fonction de prédiction

    if prediction is not None:
        return jsonify({"predicted_class": prediction}), 200
    else:
        return jsonify({"error": "Erreur dans la prédiction."}), 500

# Route pour obtenir des recommandations
@app.route('/recommendation', methods=['POST'])
def recommendation():
    data = request.get_json()
    user_data = data.get('user_data')

    if user_data is None:
        return jsonify({"error": "Aucune donnée utilisateur fournie."}), 400

    recommendation = generate_recommendation(user_data)  # Fonction de recommandations

    if recommendation:
        return jsonify({"recommendation": recommendation}), 200
    else:
        return jsonify({"error": "Erreur dans les recommandations."}), 500

if __name__ == '__main__':
    app.run(debug=True)
