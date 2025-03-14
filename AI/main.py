from data import load_and_prepare_data
from train import train_model, analyze_feature_importance, check_overfitting, save_model
from predict import create_prediction_interface
from recommandation import generate_recommendations

if __name__ == "__main__":
    # Chargement et préparation des données
    X_train, X_test, y_train, y_test, feature_names, le = load_and_prepare_data()
    
    # Entraînement du modèle
    model = train_model(X_train, y_train)
    
    # Analyse des caractéristiques importantes
    analyze_feature_importance(model, X_train, feature_names)
    
    # Vérification du surapprentissage
    check_overfitting(model, X_train, y_train)
    
    # Sauvegarde du modèle
    save_model(model, le)
    
    # Interface de prédiction
    while True:
        response = input("\nVoulez-vous faire une prédiction? (oui/non): ")
        if response.lower() != 'oui':
            break
        
        # Créer l'interface de prédiction et récupérer la prédiction et les probabilités
        predicted_disorder, probabilities = create_prediction_interface(model, feature_names, le )

        # Vérifiez que predicted_disorder et probabilities existent avant de passer à la recommandation
        if predicted_disorder is not None and probabilities is not None:
            recommendation = generate_recommendations(predicted_disorder, probabilities)
            print(f"Recommandation: {recommendation}")
        else:
            print("Aucune prédiction ou probabilité disponible.")
