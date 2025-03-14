from flask import Flask, request, jsonify
import pickle
import numpy as np
from recommandation import generate_recommendations

app = Flask(__name__)

# Charger le modèle et le LabelEncoder
try:
    with open('mental_health_model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('label_encoder.pkl', 'rb') as f:
        le = pickle.load(f)

    print("Modèle et LabelEncoder chargés avec succès.")
except FileNotFoundError as e:
    print(f"Erreur lors du chargement des fichiers : {e}")
    model = None
    le = None

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue dans l'API de prédiction de santé mentale."})

@app.route('/predict', methods=['POST'])
def predict():
    # Vérification si les fichiers nécessaires sont chargés
    if model is None or le is None:
        return jsonify({"error": "Modèle ou LabelEncoder introuvable", "success": False}), 500

    # Vérification des données reçues
    data = request.get_json()
    if not data or 'inputs' not in data:
        return jsonify({"error": "Les données d'entrée 'inputs' sont manquantes", "success": False}), 400

    try:
        # Préparation des données pour le modèle
        inputs = np.array(data['inputs']).reshape(1, -1)

        # Prédiction
        prediction = model.predict(inputs)
        decoded_prediction = le.inverse_transform(prediction)[0]  # Obtenir le label prédictible

        # Probabilités des classes (si disponible)
        probabilities = None
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(inputs)[0]  # Probabilités pour chaque classe

        # Convertir les probabilités en liste Python pour éviter l'erreur JSON
        if probabilities is not None:
            probabilities = probabilities.tolist()  # Convertir ndarray en liste

        # Génération des recommandations
        recommendations = generate_recommendations(decoded_prediction, probabilities)

        # Réponse
        return jsonify({
            "success": True,
            "prediction": decoded_prediction,
            "probabilité": probabilities,
            "recommendations": recommendations,
            "message": "Prédiction et recommandations générées avec succès"
        })
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
