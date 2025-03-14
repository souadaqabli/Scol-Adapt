import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Initialisation des variables globales
X_train, X_test, y_train, y_test, feature_names, le = None, None, None, None, None, None

def load_and_prepare_data():
    print("Préparation des données...")
    
    # Chargement des données
    df = pd.read_excel('Mental disorder symptoms.xlsx')  
    
    # Vérification et exclusion de colonnes inutiles
    if 'ag+1:629e' in df.columns:
        df = df.drop(columns=['ag+1:629e'])
        print("Colonne 'ag+1:629e' exclue des données.")
    
    # Séparation features et target
    X = df.drop('Disorder', axis=1)
    y = df['Disorder']
    
    # Encodage de la variable cible
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    # Liste des noms des caractéristiques
    feature_names = X.columns.tolist()
    
    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Dimensions de X_train :", X_train.shape)
    print("Dimensions de y_train :", y_train.shape)
    
    return X_train, X_test, y_train, y_test, feature_names, le

# Chargement des données dès l'import du module
X_train, X_test, y_train, y_test, feature_names, le = load_and_prepare_data()

__all__ = ['X_train', 'y_train', 'X_test', 'y_test', 'feature_names', 'le']
