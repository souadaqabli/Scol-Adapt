<?php
session_start();
include('db.php'); // Inclure le fichier de connexion à la base de données

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Éviter l'injection SQL
    $email = mysqli_real_escape_string($conn, $email);

    // Récupérer les détails de le docteur dans la base de données
    $sql = "SELECT * FROM doctor WHERE mail = '$email'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        $doctor = mysqli_fetch_assoc($result);

        // Vérifier le mot de passe
        if (password_verify($password, $doctor['password'])) {
            // Définir les variables de session
            $_SESSION['doctor'] = $doctor['mail'];
            header('Location: doctor_space.php');
            exit();
        } else {
            $error = "Email or password incorrect !";
        }
    } else {
        $error = "Email or password incorrect !";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutor Login</title>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" />
    <link rel="stylesheet" href="doctor_login.css">
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <section id="header">
        <a href="#"><img src="image/logo_removed bg.png" class="logo" alt="Logo"></a>
        <div>
            <ul id="navbar">
                <li><a href="index.html">Home</a></li>
                <li><a href="login_admin.php">Admin</a></li>
                <li><a href="About.html">About</a></li>
                <li><a href="Contact.html">Contact</a></li>
            </ul>
        </div>
    </section>

    <div class="main-container">

        <!-- Image section -->
        <div class="image-container">
            <img src="image/Doctor_Login.jpg" alt="Tutor Login Illustration">
        </div>

        <!-- Login form section -->
        <div class="login-container">
            <h2>Doctor Space</h2>
            <?php if (isset($error)): ?>
                <p class="error"><?= $error ?></p>
            <?php endif; ?>
            <form action="doctor_login.php" method="POST">
                <div class="input-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="input-group">
                    <label for="password">Password:</label>
                    <div class="password-container">
                        <input type="password" id="password" name="password" required>
                        <i class="far fa-eye" id="togglePassword"></i>
                    </div>
                </div>
                <div class="input-group">
                    <a href="forgot_password.php">Forgot Password?</a>
                </div>
                <button type="submit">Login</button>
                <div class="input-group">
                    <h>You do not have an account ? <a href="doctor_sign_up.php">sign up →</a></h>
                </div>
            </form>
        </div>
    </div>  

        <!-- Informative text section -->
        <div class="info-text">
        <p>
            Are you a child psychiatrist passionate about helping young learners overcome challenges and thrive academically?
            
            Join our platform to access innovative tools and resources tailored to support children’s mental well-being and foster a positive learning environment for every student.  
        </p>
    </div>  

    <script>
        const togglePassword = document.querySelector('#togglePassword');
        const password = document.querySelector('#password');

        togglePassword.addEventListener('click', function (e) {
            // Toggle the type attribute
            const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
            password.setAttribute('type', type);
            // Toggle the eye slash icon
            this.classList.toggle('fa-eye-slash');
        });
    </script>
</body>
</html>
