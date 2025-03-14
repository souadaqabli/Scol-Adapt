<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire de Santé Mentale</title>
    <link rel="stylesheet" href="form.css">
</head>
<body>
    <div class="container">
        <h1>Formulaire de Santé Mentale</h1>

        <form action="tutor_space.php" method="POST">
            <!-- Section 1 -->
            <div class="section">
                <h2>Section 1: Informations générales</h2>
                
                <div class="form-group">
                    <label for="feeling_nervous">État nerveux :</label>
                    <select id="feeling_nervous" name="feeling_nervous" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="panic">Crises de panique :</label>
                    <select id="panic" name="panic" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="breathing_rapidly">Respiration rapide :</label>
                    <select id="breathing_rapidly" name="breathing_rapidly" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="sweating">Transpiration excessive :</label>
                    <select id="sweating" name="sweating" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="trouble_in_concentration">Difficultés de concentration :</label>
                    <select id="trouble_in_concentration" name="trouble_in_concentration" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="having_trouble_in_sleeping">Troubles du sommeil :</label>
                    <select id="having_trouble_in_sleeping" name="having_trouble_in_sleeping" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="having_trouble_with_work">Difficultés au travail :</label>
                    <select id="having_trouble_with_work" name="having_trouble_with_work" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="hopelessness">Sentiment de désespoir :</label>
                    <select id="hopelessness" name="hopelessness" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="anger">Colère :</label>
                    <select id="anger" name="anger" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="over_react">Réactions excessives :</label>
                    <select id="over_react" name="over_react" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="change_in_eating">Changements dans l'alimentation :</label>
                    <select id="change_in_eating" name="change_in_eating" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
            </div>

            <!-- Section 2 -->
            <div class="section">
                <h2>Section 2: Questions avancées</h2>

                <div class="form-group">
                    <label for="suicidal_thought">Pensées suicidaires :</label>
                    <select id="suicidal_thought" name="suicidal_thought" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="feeling_tired">Fatigue chronique :</label>
                    <select id="feeling_tired" name="feeling_tired" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="close_friend">Présence d'amis proches :</label>
                    <select id="close_friend" name="close_friend" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="social_media_addiction">Dépendance aux réseaux sociaux :</label>
                    <select id="social_media_addiction" name="social_media_addiction" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="weight_gain">Prise de poids :</label>
                    <select id="weight_gain" name="weight_gain" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="introvert">Introverti :</label>
                    <select id="introvert" name="introvert" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="popping_up_stressful_memory">Souvenirs stressants récurrents :</label>
                    <select id="popping_up_stressful_memory" name="popping_up_stressful_memory" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="having_nightmares">Cauchemars :</label>
                    <select id="having_nightmares" name="having_nightmares" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="avoids_people_or_activities">Évitement social :</label>
                    <select id="avoids_people_or_activities" name="avoids_people_or_activities" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="feeling_negative">Pensées négatives :</label>
                    <select id="feeling_negative" name="feeling_negative" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="trouble_concentrating">Difficultés de concentration :</label>
                    <select id="trouble_concentrating" name="trouble_concentrating" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="blamming_yourself">Auto-culpabilisation :</label>
                    <select id="blamming_yourself" name="blamming_yourself" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="hallucinations">Hallucinations :</label>
                    <select id="hallucinations" name="hallucinations" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="repetitive_behaviour">Comportements répétitifs :</label>
                    <select id="repetitive_behaviour" name="repetitive_behaviour" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="seasonally">Variations saisonnières :</label>
                    <select id="seasonally" name="seasonally" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="form-group">
                    <label for="increased_energy">Augmentation d'énergie :</label>
                    <select id="increased_energy" name="increased_energy" required>
                        <option value="" selected disabled>Choisissez une option</option>
                        <option value="Oui">Oui</option>
                        <option value="Non">Non</option>
                    </select>
                </div>
    
                <div class="submit-section">
                    <div class="submit-container">
                        <button type="submit">Envoyer le formulaire</button>
                </div>
            </div>

            <!-- Bouton d'envoi fixé en bas de page -->
            <div class="submit-section">
                <div class="submit-container">
                    <button type="submit">Envoyer le formulaire</button>
                </div>
            </div>
        </form>
    </div>
</body>
</html>