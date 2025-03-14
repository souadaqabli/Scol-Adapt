import numpy as np

def create_prediction_interface(model, feature_names, le):
    print("\nInterface de prédiction:")
    
    # Exclure le critère 'ag+'
    if 'ag+1:629e' in feature_names:
        feature_names = [feature for feature in feature_names if feature != 'ag+1:629e']
        #print("Le critère 'ag+' a été exclu du questionnaire.")
    
    # Créer un dictionnaire pour stocker les entrées
    inputs = {}
    for feature in feature_names:
        while True:
            try:
                value = float(input(f"{feature}: "))
                if 0 <= value <= 1:
                    inputs[feature] = value
                    break
                else:
                    print("La valeur doit être entre 0 et 1")
            except ValueError:
                print("Veuillez entrer un nombre valide")
    
    # Faire la prédiction
    input_data = np.array(list(inputs.values())).reshape(1, -1)
    prediction = model.predict(input_data)
    predicted_disorder = le.inverse_transform(prediction)[0]
    
    print(f"\nTrouble mental prédit: {predicted_disorder}")
    
    # Afficher les probabilités pour chaque classe
    probabilities = model.predict_proba(input_data)
    print("\nProbabilités pour chaque trouble:")
    for disorder, prob in zip(le.classes_, probabilities[0]):
        print(f"{disorder}: {prob:.4f}")
    
    # Retourner la classe prédite et les probabilités
    return predicted_disorder, probabilities[0]
