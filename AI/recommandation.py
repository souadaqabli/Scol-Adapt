import numpy as np

recommandations = {
    "MDD": {
        "nom_complet": "Major Depressive Disorder - Dépression majeure",
        "description": "La dépression majeure est un trouble de l'humeur qui affecte environ 7% de la population mondiale. Elle se manifeste par une tristesse intense et persistante durant au moins deux semaines, accompagnée de symptômes comme des troubles du sommeil, une perte d'appétit, une fatigue constante, des difficultés de concentration et parfois des pensées suicidaires. Cette condition altère significativement la qualité de vie et nécessite une consultation rapide auprès d'un psychiatre ou psychologue pour un diagnostic et une prise en charge adaptée."
    },
    "ASD": {
        "nom_complet": "Autism Spectrum Disorder - Trouble du spectre autistique",
        "description": "L'autisme est un trouble neurodéveloppemental qui se manifeste dès la petite enfance. Les personnes atteintes peuvent présenter des difficultés dans la communication sociale, des comportements répétitifs, une sensibilité particulière aux stimuli sensoriels (bruits, lumières, textures) et des intérêts très spécifiques. La sévérité des symptômes varie considérablement d'une personne à l'autre. Un diagnostic précoce par une équipe pluridisciplinaire spécialisée (pédopsychiatre, psychologue, orthophoniste) est essentiel pour une meilleure prise en charge et un accompagnement adapté."
    },
    "Loneliness": {
        "nom_complet": "Solitude",
        "description": "La solitude chronique est un état psychologique qui va au-delà du simple fait d'être seul. Elle se caractérise par un sentiment profond d'isolement social et émotionnel, même en présence d'autres personnes. Des études scientifiques ont démontré que la solitude prolongée peut avoir des impacts négatifs sur la santé physique et mentale, augmentant les risques de dépression, d'anxiété et de maladies cardiovasculaires. Si ce sentiment persiste et affecte votre bien-être quotidien, consulter un psychologue peut vous aider à développer des stratégies pour créer des connexions sociales significatives."
    },
    "Bipolar_Disorder": {
        "nom_complet": "Trouble bipolaire",
        "description": "Le trouble bipolaire est une maladie chronique qui touche environ 2,4% de la population mondiale. Il se caractérise par l'alternance d'épisodes maniaques (euphorie intense, impulsivité, réduction du besoin de sommeil) et dépressifs (tristesse profonde, perte d'énergie). Les épisodes peuvent durer de quelques semaines à plusieurs mois. Cette condition peut avoir des répercussions graves sur la vie professionnelle, sociale et familiale. Une consultation psychiatrique est indispensable pour un diagnostic précis et la mise en place d'un traitement approprié, généralement une combinaison de médicaments et de psychothérapie."
    },
    "Anxiety": {
        "nom_complet": "Anxiété",
        "description": "L'anxiété pathologique se distingue de l'anxiété normale par son intensité et sa persistance. Elle se manifeste par des inquiétudes excessives et incontrôlables, accompagnées de symptômes physiques comme des palpitations, des tremblements, des sueurs et une tension musculaire. L'anxiété peut aussi provoquer des troubles du sommeil et des difficultés de concentration. Lorsque ces symptômes persistent plus de 6 mois et perturbent la vie quotidienne, il est important de consulter un professionnel de santé mentale (psychologue ou psychiatre) pour une évaluation et un traitement adapté."
    },
    "PTSD": {
        "nom_complet": "Post-Traumatic Stress Disorder - Trouble de stress post-traumatique",
        "description": "Le TSPT est une réponse psychologique qui se développe suite à l'exposition à un événement traumatique (accident grave, agression, catastrophe naturelle). Les personnes atteintes peuvent souffrir de flashbacks vivides, de cauchemars récurrents, d'hypervigilance et d'évitement des situations rappelant le trauma. Le trouble peut également s'accompagner de modifications neurobiologiques affectant la réponse au stress. Une prise en charge spécialisée par un psychiatre ou un psychologue traumatologue est essentielle, car des thérapies spécifiques comme l'EMDR ont prouvé leur efficacité."
    },
    "sleep disorder": {
        "nom_complet": "Trouble du sommeil",
        "description": "Les troubles du sommeil englobent diverses conditions affectant la qualité, la durée ou le rythme du sommeil. Ils peuvent se manifester par des difficultés d'endormissement, des réveils nocturnes fréquents, une somnolence diurne excessive ou des parasomnies (somnambulisme, terreurs nocturnes). Ces troubles peuvent avoir des causes physiques, psychologiques ou environnementales. Si les problèmes de sommeil persistent plus de trois mois et affectent votre fonctionnement quotidien, consultez un médecin ou un spécialiste du sommeil pour une évaluation approfondie."
    },
    "psychotic deprission": {
        "nom_complet": "Dépression psychotique",
        "description": "La dépression psychotique est une forme sévère de dépression caractérisée par la présence de symptômes psychotiques (hallucinations, délires) en plus des symptômes dépressifs classiques. Les personnes atteintes peuvent avoir des croyances irrationnelles de culpabilité, de ruine ou de maladie, et parfois entendre des voix négatives. Cette condition nécessite une prise en charge psychiatrique urgente, généralement en milieu hospitalier, car elle présente un risque élevé de suicide. Un traitement combinant antipsychotiques et antidépresseurs est souvent nécessaire."
    },
    "eating disorder": {
        "nom_complet": "Trouble de l'alimentation",
        "description": "Les troubles alimentaires sont des maladies mentales graves affectant le comportement alimentaire et l'image corporelle. Ils incluent l'anorexie (restriction alimentaire sévère), la boulimie (cycles de crises de suralimentation suivies de comportements compensatoires) et l'hyperphagie. Ces troubles peuvent entraîner des complications médicales sérieuses et ont le taux de mortalité le plus élevé parmi les maladies mentales. Une prise en charge multidisciplinaire (psychiatre, psychologue, nutritionniste) est essentielle pour un traitement efficace."
    },
    "ADHD": {
        "nom_complet": "Attention Deficit Hyperactivity Disorder - Trouble de l'attention avec ou sans hyperactivité",
        "description": "Le TDAH est un trouble neurodéveloppemental qui touche environ 5% des enfants et peut persister à l'âge adulte. Il se caractérise par des difficultés d'attention, une hyperactivité motrice et/ou une impulsivité qui dépassent le niveau attendu pour l'âge. Ces symptômes peuvent affecter significativement les performances scolaires ou professionnelles et les relations sociales. Un diagnostic précis par un psychiatre ou neuropsychologue est nécessaire, car le TDAH est souvent associé à d'autres troubles (anxiété, troubles d'apprentissage). Un traitement multimodal incluant approches comportementales et parfois médicamenteuses est recommandé."
    },
    "PDD": {
        "nom_complet": "Persistent Depressive Disorder - Trouble dépressif persistant",
        "description": "Le trouble dépressif persistant, anciennement appelé dysthymie, est une forme chronique de dépression qui dure au moins deux ans chez l'adulte. Les symptômes sont moins intenses que dans la dépression majeure mais plus persistants, incluant une humeur dépressive chronique, une faible estime de soi, des troubles du sommeil et une fatigue constante. Cette condition peut significativement impacter la qualité de vie et les relations interpersonnelles. Une consultation auprès d'un psychiatre ou psychologue est nécessaire pour un diagnostic et un traitement approprié, combinant souvent psychothérapie et médication."
    },
    "OCD": {
        "nom_complet": "Obsessive-Compulsive Disorder - Trouble obsessionnel-compulsif",
        "description": "Le TOC est un trouble anxieux caractérisé par des pensées intrusives récurrentes (obsessions) et des comportements répétitifs (compulsions) que la personne se sent obligée d'effectuer pour réduire son anxiété. Ces rituels peuvent prendre plusieurs heures par jour et interférer significativement avec la vie quotidienne. Les recherches ont montré des anomalies dans les circuits cérébraux impliqués dans la régulation des émotions et du comportement. Une consultation auprès d'un psychiatre ou psychologue spécialisé est essentielle, car des traitements spécifiques comme la thérapie d'exposition et les médicaments sérotoninergiques peuvent grandement améliorer la qualité de vie."
    }
}

def generate_recommendations(prediction, probabilities):
    """
    Génère une description basée sur la prédiction et les probabilités associées.
    
    :param prediction: Classe prédite par le modèle (str)
    :param probabilities: Tableau des probabilités pour chaque classe (numpy.ndarray)
    :return: Texte contenant le trouble prédit et sa description
    """
    predicted_index = np.argmax(probabilities)
    predicted_probability = probabilities[predicted_index]

    if prediction in recommandations:
        recommendation_data = recommandations[prediction]
        recommendation_text = f"{recommendation_data['nom_complet']}\n{recommendation_data['description']}"
    else:
        recommendation_text = "Aucune description disponible pour ce trouble."
    
    return f"\n{recommendation_text}"