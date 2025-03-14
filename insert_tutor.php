<?php
include('db.php'); // Fichier de connexion à la base de données

// Fonction pour insérer un tuteur
function insert_tutor($conn, $family_name, $first_name, $mail, $password, $image = 'image/blank_profile.jpeg') {
    // Hasher le mot de passe avant l'insertion
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Préparer la requête d'insertion
    $sql = "INSERT INTO tutor (family_name, first_name, mail, password, image) 
            VALUES (?, ?, ?, ?, ?)";
    
    // Préparer une requête sécurisée
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "sssss", $family_name, $first_name, $mail, $hashed_password, $image);

    // Exécuter la requête
    if (mysqli_stmt_execute($stmt)) {
        echo "Tutor inserted successfully: $mail<br>";
    } else {
        echo "Error inserting tutor: " . mysqli_error($conn) . "<br>";
    }

    mysqli_stmt_close($stmt);
}

// Insérer deux tuteurs
insert_tutor($conn, "Doe", "John", "john.doe@example.com", "password123");
insert_tutor($conn, "Smith", "Jane", "jane.smith@example.com", "securepass456");

// Fermer la connexion à la base de données
mysqli_close($conn);
?>
