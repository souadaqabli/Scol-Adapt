import numpy as np
from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, learning_curve
import pickle
from data import X_train, y_train, X_test, y_test


def train_model(X_train, y_train):
    print("Entraînement du modèle...")
    model = RandomForestClassifier(n_estimators=100, max_depth=10, 
    min_samples_split=5, 
    min_samples_leaf=2,
    random_state=42)
    model.fit(X_train, y_train)
    
    # Validation croisée
    print("Entraînement du modèle avec validation croisée...")
    # Validation croisée pour vérifier les performances
    train_score = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    test_score = cross_val_score(model, X_test, y_test, cv=5, scoring='accuracy')

    print("Score d'entraînement moyen :", train_score.mean())
    print("Score de test moyen :", test_score.mean())
    
    return model

def analyze_feature_importance(model, X_train, feature_names):
    print("\nAnalyse des caractéristiques importantes:")
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title("Importance des caractéristiques")
    plt.bar(range(X_train.shape[1]), importances[indices])
    plt.xticks(range(X_train.shape[1]), [feature_names[i] for i in indices], rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    
    print("\nTop 10 des caractéristiques les plus importantes:")
    for f in range(10):
        print("%d. %s (%f)" % (f + 1, feature_names[indices[f]], importances[indices[f]]))

def check_overfitting(model, X_train, y_train):
    print("\nVérification du surapprentissage:")
    
    train_sizes, train_scores, test_scores = learning_curve(
        model, X_train, y_train, cv=5, n_jobs=-1, 
        train_sizes=np.linspace(0.1, 1.0, 10))
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, label='Score d\'entraînement')
    plt.plot(train_sizes, test_mean, label='Score de validation croisée')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1)
    plt.xlabel('Taille de l\'échantillon d\'entraînement')
    plt.ylabel('Score')
    plt.title('Courbe d\'apprentissage')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('learning_curve.png')

def save_model(model, le):
    # Sauvegarde du modèle
    with open('mental_health_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Sauvegarde du LabelEncoder
    with open('label_encoder.pkl', 'wb') as f:
        pickle.dump(le, f)