<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultat de l'Évaluation</title>
    <link rel="stylesheet" href="tutor_space.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Résultat de l'Évaluation</h1>
        </div>
        <div class="content">
            <?php
            include('db.php');

            session_start();
            if (!isset($_SESSION['tutor'])) {
                header('Location: tutor_login.php');
                exit();
            }

            $fields = [
                'feeling_nervous', 'panic', 'breathing_rapidly', 'sweating',
                'trouble_in_concentration', 'having_trouble_in_sleeping', 'having_trouble_with_work',
                'hopelessness', 'anger', 'over_react', 'change_in_eating',
                'suicidal_thought', 'feeling_tired', 'close_friend', 'social_media_addiction',
                'weight_gain', 'introvert', 'popping_up_stressful_memory', 'having_nightmares',
                'avoids_people_or_activities', 'feeling_negative', 'trouble_concentrating',
                'blamming_yourself', 'hallucinations', 'repetitive_behaviour', 'seasonally',
                'increased_energy'
            ];

            $missing_fields = array_diff($fields, array_keys($_POST));
            if (!empty($missing_fields)) {
                echo '<div class="error-message">Les champs suivants sont manquants : ' . 
                     implode(', ', $missing_fields) . '</div>';
                exit;
            }

            $data = [];
            foreach ($fields as $field) {
                $value = trim($_POST[$field]);
                if (!in_array($value, ['Oui', 'Non'], true)) {
                    echo '<div class="error-message">Valeur invalide pour le champ ' . 
                         htmlspecialchars($field) . '.</div>';
                    exit;
                }
                $data[$field] = $value === 'Oui' ? 1 : 0;
            }

            $json_data = json_encode(['inputs' => array_values($data)]);
            $ch = curl_init('http://127.0.0.1:5000/predict');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $json_data);
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                'Content-Type: application/json',
                'Content-Length: ' . strlen($json_data)
            ]);

            $response = curl_exec($ch);

            if ($response === false) {
                echo '<div class="error-message">Erreur cURL : ' . curl_error($ch) . '</div>';
            } else {
                $decoded_response = json_decode($response, true);

                if (isset($decoded_response['prediction']) && 
                    isset($decoded_response['message']) && 
                    isset($decoded_response['recommendations'])) {
                    
                    echo '<div class="result-card">
                            <div class="result-title">
                                <span class="result-icon">🔍</span>
                                <strong>Trouble identifié :</strong> ' . 
                                htmlspecialchars($decoded_response['prediction']) . 
                            '</div>';
                    
                    // Déterminer la sévérité basée sur la prédiction
                    $severity_class = 'severity-medium';
                    if (strpos(strtolower($decoded_response['prediction']), 'severe') !== false) {
                        $severity_class = 'severity-high';
                    }
                    
                    echo '<div class="severity-indicator ' . $severity_class . '">
                            Consultation recommandée
                          </div>';

                    echo '<div class="description">' . 
                         htmlspecialchars($decoded_response['recommendations']) . 
                         '</div>';
                    
                    echo '</div>';
                } else {
                    echo '<div class="error-message">
                            Erreur lors de la récupération de la réponse. Données reçues :
                            <pre>' . htmlspecialchars($response) . '</pre>
                          </div>';
                }
            }

            curl_close($ch);
            ?>

            <div class="buttons">
                <a href="form.php" class="button button-secondary">
                    ← Retour au questionnaire
                </a>
                <?php if (isset($decoded_response['prediction'])): ?>
                    <a href="generate_program.php?diagnosis=<?php echo urlencode($decoded_response['prediction']); ?>&subjects=General+Subjects&availability=2-3+hours" class="button button-primary">
                        Générer un programme personnalisé →
                    </a>
                <?php endif; ?>
            </div>
        </div>
    </div>
</body>
</html>
