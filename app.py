import streamlit as st
import random

# Configuration
st.set_page_config(
    page_title="Quiz Code de la Route",
    page_icon="🚗",
    layout="wide"
)

# ============================================================
# THÈMES AVEC LEURS QUESTIONS (CORRIGÉES)
# ============================================================

themes = {
    "🏎️ Vitesse": {
        "icon": "🏎️",
        "questions": [
            {
                "question": "Quelle est la vitesse maximale autorisée en agglomération ?",
                "options": ["30 km/h", "40 km/h", "50 km/h", "60 km/h"],
                "correct": 2,
                "explication": "La vitesse maximale en ville est de 50 km/h (sauf zones 30)."
            },
            {
                "question": "Quelle est la vitesse maximale autorisée en rase campagne (hors agglomération) ?",
                "options": ["70 km/h", "80 km/h", "90 km/h", "100 km/h"],
                "correct": 1,
                "explication": "La limite générale hors agglomération est de 80 km/h."
            },
            {
                "question": "Qu'est-ce qui compose la distance d'arrêt ?",
                "options": ["Freinage × 2", "Réaction + Freinage", "Réaction × Freinage", "Arrêt - Réaction"],
                "correct": 1,
                "explication": "La distance d'arrêt est la somme des distances de réaction et de freinage."
            },
            {
                "question": "Qu'est-ce qui augmente la distance de réaction ? (plusieurs réponses)",
                "options": ["Alcool", "Fatigue", "Bonne visibilité", "Distraction"],
                "correct": [0, 1, 3],
                "explication": "L'alcool, la fatigue et la distraction allongent le temps de réaction."
            },
            {
                "question": "Quelle est la vitesse maximale sur une route 2x1 voie (2 voies d'un côté, 1 de l'autre) ?",
                "options": ["70 km/h", "80 km/h", "90 km/h", "110 km/h"],
                "correct": 2,
                "explication": "Sur route à chaussées séparées (2x1), la vitesse est de 90 km/h."
            },
            {
                "question": "En temps de pluie, quelles distances sont augmentées ? (plusieurs réponses)",
                "options": ["Distance de réaction", "Distance de freinage", "Distance d'arrêt", "Distance de visibilité"],
                "correct": [1, 2],
                "explication": "La pluie augmente la distance de freinage et donc la distance d'arrêt."
            },
            {
                "question": "Quelle est la vitesse maximale sur autoroute en temps de pluie ?",
                "options": ["80 km/h", "100 km/h", "110 km/h", "130 km/h"],
                "correct": 2,
                "explication": "Sur autoroute sous la pluie, la vitesse est limitée à 110 km/h."
            },
            {
                "question": "Quelle est la vitesse maximale en temps de verglas ?",
                "options": ["30 km/h", "40 km/h", "50 km/h", "70 km/h"],
                "correct": 2,
                "explication": "En cas de verglas, la vitesse maximale est de 50 km/h."
            }
        ]
    },
    "🚦 Priorité": {
        "icon": "🚦",
        "questions": [
            {
                "question": "Le conducteur A est sur la voie principale, le conducteur B est sur la voie verte. Qui a la priorité ?",
                "options": ["Conducteur A", "Conducteur B", "Le plus rapide", "Celui qui arrive en premier"],
                "correct": 0,
                "explication": "Le conducteur A sur la voie principale est prioritaire. La voie verte n'est pas prioritaire, c'est celui qui en sort qui doit céder le passage."
            },
            {
                "question": "Qui est prioritaire face à un obstacle sur la route ?",
                "options": ["Celui qui arrive en premier", "Le plus lent", "Le conducteur sans obstacle", "Celui qui klaxonne"],
                "correct": 2,
                "explication": "Celui qui rencontre un obstacle doit céder le passage."
            },
            {
                "question": "Comment fonctionnent les priorités dans un giratoire ?",
                "options": ["Priorité à droite", "Priorité aux véhicules déjà engagés", "Priorité à celui qui entre", "Priorité au plus rapide"],
                "correct": 1,
                "explication": "Dans un giratoire, la priorité est aux véhicules déjà engagés (priorité à gauche)."
            },
            {
                "question": "Comment fonctionnent les priorités dans un rond-point (sans signalisation) ?",
                "options": ["Priorité à droite", "Priorité à gauche", "Priorité aux véhicules déjà engagés", "Priorité à celui qui entre"],
                "correct": 0,
                "explication": "Dans un rond-point, la règle par défaut est la priorité à droite."
            },
            {
                "question": "Dans le cas d'un carrefour à feux classique, je veux tourner à gauche. Qui a la priorité ?",
                "options": ["Les véhicules venant de droite", "Les véhicules venant d'en face", "Les piétons", "Personne, je suis prioritaire"],
                "correct": 1,
                "explication": "Au feu vert, si tu tournes, tu laisses passer les usagers venant en face."
            },
            {
                "question": "Dans le cas d'un carrefour avec des feux à flèche, je veux tourner à gauche et le feu flèche gauche est vert. Ai-je la priorité ?",
                "options": ["Non", "Oui", "Seulement si j'ai mon clignotant", "Seulement la nuit"],
                "correct": 1,
                "explication": "La flèche verte indique que tu es prioritaire pour tourner à gauche."
            }
        ]
    },
    "💡 Feux & Éclairage": {
        "icon": "💡",
        "questions": [
            {
                "question": "Dans des virages serrés, quels feux puis-je activer en complément ?",
                "options": ["Feux de route", "Feux de détresse", "Feux de brouillard avant", "Feux de position"],
                "correct": 2,
                "explication": "Les feux de brouillard avant éclairent plus large dans les virages serrés."
            },
            {
                "question": "Dans quelles situations peut-on allumer les feux de brouillard arrière ? (plusieurs réponses)",
                "options": ["Fortes pluies", "Brouillard épais", "Nuit claire", "En ville éclairée"],
                "correct": [0, 1],
                "explication": "Les feux de brouillard arrière sont réservés aux conditions de visibilité très réduite."
            },
            {
                "question": "En agglomération éclairée, quels feux doivent être activés ?",
                "options": ["Feux de route", "Feux de croisement", "Feux de détresse", "Feux de brouillard"],
                "correct": 1,
                "explication": "En ville éclairée, on utilise les feux de croisement (pas les feux de route)."
            },
            {
                "question": "Quand puis-je activer les feux de route ?",
                "options": ["Quand il y a du brouillard", "Quand je roule en ville", "Quand aucun autre véhicule n'est devant moi ni n'arrive en face", "Quand je suis en agglomération"],
                "correct": 2,
                "explication": "Les feux de route s'utilisent quand il n'y a personne devant moi (ni dans le même sens, ni en face)."
            },
            {
                "question": "Quel est l'usage des feux de position ?",
                "options": ["Éclairer la route", "Signaler un danger", "Signaler ma présence", "Indiquer un virage"],
                "correct": 2,
                "explication": "Les feux de position rendent le véhicule visible aux autres usagers."
            },
            {
                "question": "Dans un giratoire, comment gérer les clignotants pour aller tout droit et le placement ?",
                "options": ["Je reste au centre et je mets le clignotant gauche", "Extérieur du rond-point + clignotant droit avant de sortir", "Je mets le clignotant gauche tout le temps", "Je ne mets pas de clignotant"],
                "correct": 1,
                "explication": "Pour aller tout droit, on reste à l'extérieur et on met le clignotant droit avant de sortir."
            },
            {
                "question": "Quand activer les feux de détresse ?",
                "options": ["Quand je roule vite", "Ralentissement important ou véhicule immobilisé", "Quand je change de direction", "Quand je suis en tort"],
                "correct": 1,
                "explication": "Les feux de détresse signalent un danger inhabituel ou un ralentissement brutal."
            }
        ]
    },
    "🅿️ Stationnement": {
        "icon": "🅿️",
        "questions": [
            {
                "question": "Que signifie une ligne jaune continue ?",
                "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Rien de particulier"],
                "correct": 1,
                "explication": "La ligne jaune continue interdit l'arrêt ET le stationnement."
            },
            {
                "question": "Que signifie une ligne jaune discontinue ?",
                "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Stationnement gratuit"],
                "correct": 0,
                "explication": "La ligne jaune discontinue interdit le stationnement mais autorise l'arrêt."
            },
            {
                "question": "Puis-je consulter mon téléphone lorsque mon véhicule est arrêté et que le moteur est allumé ?",
                "options": ["Oui", "Non", "Oui, seulement si je suis sur le parking", "Oui, seulement si j'ai le Bluetooth"],
                "correct": 1,
                "explication": "Le téléphone en main est interdit sauf si le véhicule est correctement stationné (moteur coupé)."
            },
            {
                "question": "Dans une voie à sens unique, de quel côté puis-je me stationner ?",
                "options": ["Uniquement à droite", "Uniquement à gauche", "Gauche et droite", "Seulement sur le trottoir"],
                "correct": 2,
                "explication": "En sens unique, le stationnement est autorisé des deux côtés."
            }
        ]
    },
    "🛠️ Divers": {
        "icon": "🛠️",
        "questions": [
            {
                "question": "Quand je rencontre un panneau d'obligation de chaînes à neige, j'ai l'obligation que mon véhicule en soit équipé sur :",
                "options": ["Les 4 roues", "Les roues motrices seulement", "Les roues avant", "Les roues arrière"],
                "correct": 1,
                "explication": "Les chaînes se montent sur les roues motrices du véhicule."
            },
            {
                "question": "À quelle distance éclairent les feux de croisement ?",
                "options": ["10 mètres", "30 mètres environ", "50 mètres", "100 mètres"],
                "correct": 1,
                "explication": "Les feux de croisement éclairent à environ 30 mètres."
            },
            {
                "question": "À quelle distance éclairent les feux de route ?",
                "options": ["30 mètres", "50 mètres", "80 mètres", "100 mètres environ"],
                "correct": 3,
                "explication": "Les feux de route éclairent à environ 100 mètres."
            },
            {
                "question": "Quand un véhicule me dépasse, je dois : (plusieurs réponses)",
                "options": ["Maintenir mon allure", "Me serrer à droite", "Accélérer", "Ne jamais accélérer"],
                "correct": [0, 1, 3],
                "explication": "Je maintiens mon allure, je me serre à droite et je n'accélère jamais."
            },
            {
                "question": "En tant que piéton, puis-je traverser la route en présence d'un bus à proximité ?",
                "options": ["Oui", "Non", "Oui, si le bus est à l'arrêt", "Oui, si je cours"],
                "correct": 1,
                "explication": "Il est interdit de traverser devant ou derrière un bus ; il faut attendre son départ."
            },
            {
                "question": "En tant que conducteur, un bus s'arrête devant moi à un arrêt. Que dois-je faire ?",
                "options": ["Le dépasser par la droite", "Attendre qu'il redémarre sans dépasser", "Klaxonner pour qu'il avance", "Le dépasser si c'est sûr"],
                "correct": 1,
                "explication": "Il faut attendre que le bus redémarre, car des piétons peuvent traverser."
            },
            {
                "question": "Pour un véhicule électrique, de quoi dépend le temps de conduite ? (plusieurs réponses)",
                "options": ["De la température extérieure", "De la façon de conduire", "De la charge de la batterie", "Du nombre de passagers"],
                "correct": [1, 2],
                "explication": "L'autonomie dépend du style de conduite et du niveau de charge de la batterie."
            },
            {
                "question": "Quel niveau contrôle la tige moteur ?",
                "options": ["Niveau de liquide de refroidissement", "Niveau d'huile", "Niveau de liquide de frein", "Niveau de lave-glace"],
                "correct": 1,
                "explication": "La jauge d'huile mesure le niveau d'huile moteur."
            },
            {
                "question": "Que signifie le voyant pression ?",
                "options": ["Pression d'huile trop basse", "Pneus sous-gonflés", "Pression des freins", "Pression de la batterie"],
                "correct": 1,
                "explication": "Le voyant de pression indique que les pneus sont sous-gonflés."
            },
            {
                "question": "Un niveau de pollution non conforme déclenche une défaillance de quel type au contrôle technique ?",
                "options": ["Mineure", "Majeure", "Critique", "Aucune"],
                "correct": 1,
                "explication": "Une pollution non conforme est une défaillance majeure au contrôle technique."
            },
            {
                "question": "Un chargement sur le toit peut dépasser de combien ?",
                "options": ["1 mètre à l'avant, 0 à l'arrière", "2 mètres à l'arrière, 0 à l'avant", "3 mètres à l'arrière, 0 à l'avant", "1 mètre partout"],
                "correct": 2,
                "explication": "Le chargement peut dépasser à l'arrière (jusqu'à 3 m) mais jamais à l'avant."
            },
            {
                "question": "Quelle est la limite d'alcool pour un jeune conducteur ?",
                "options": ["0,50 g/L", "0,20 g/L", "0,10 g/L", "0,80 g/L"],
                "correct": 1,
                "explication": "La limite est de 0,20 g/L pour les jeunes conducteurs (contre 0,50 g/L pour les confirmés)."
            },
            {
                "question": "Qu'est-ce qui est inclus dans l'abonnement d'autopartage ? (plusieurs réponses)",
                "options": ["Énergie (carburant/électricité)", "Assurance", "Entretien", "Péages"],
                "correct": [0, 1, 2],
                "explication": "L'autopartage inclut l'énergie, l'assurance et l'entretien. Les péages sont à la charge de l'utilisateur."
            },
            {
                "question": "Quel côté du constat amiable peut être complété après la signature ?",
                "options": ["Le recto", "Le verso", "Les deux côtés", "Aucun côté"],
                "correct": 1,
                "explication": "Le verso du constat amiable peut être complété après la signature."
            }
        ]
    }
}

# ============================================================
# SIDEBAR - SÉLECTION DU THÈME
# ============================================================

st.sidebar.title("🚗 Quiz Code")
st.sidebar.markdown("---")

# Créer les boutons dans la sidebar
selected_theme = None
for theme_name in themes.keys():
    if st.sidebar.button(f"{themes[theme_name]['icon']} {theme_name}", use_container_width=True):
        selected_theme = theme_name

# Réinitialiser le quiz si le thème change
if selected_theme:
    st.session_state['selected_theme'] = selected_theme
    # Réinitialiser l'état du quiz
    for key in list(st.session_state.keys()):
        if key.startswith("quiz_"):
            del st.session_state[key]

# Si aucun thème sélectionné, prendre le dernier ou le premier
if 'selected_theme' not in st.session_state:
    st.session_state['selected_theme'] = list(themes.keys())[0]

theme_name = st.session_state['selected_theme']

# ============================================================
# AFFICHAGE DU QUIZ
# ============================================================

st.title(f"{themes[theme_name]['icon']} Quiz {theme_name}")

theme_data = themes[theme_name]
questions = theme_data["questions"]

# Mélanger les questions (mais de manière fixe pour la session)
if f"shuffled_{theme_name}" not in st.session_state:
    shuffled = questions.copy()
    random.shuffle(shuffled)
    st.session_state[f"shuffled_{theme_name}"] = shuffled

questions = st.session_state[f"shuffled_{theme_name}"]

# Initialisation du quiz
session_key = f"quiz_{theme_name}"
if session_key not in st.session_state:
    st.session_state[session_key] = {
        "current": 0,
        "score": 0,
        "answers": [],
        "finished": False
    }

quiz = st.session_state[session_key]
total = len(questions)
current = quiz["current"]

# Barre de progression
st.progress(current / total if total > 0 else 0)
st.markdown(f"**Question {current + 1} / {total}**")

# ============================================================
# AFFICHAGE DES QUESTIONS
# ============================================================

if not quiz["finished"] and current < total:
    q = questions[current]
    
    # Mélanger les options (mais de manière fixe pour la question)
    q_key = f"shuffled_options_{theme_name}_{current}"
    if q_key not in st.session_state:
        # Créer un tuple (option, index_original)
        options_with_index = list(enumerate(q["options"]))
        random.shuffle(options_with_index)
        st.session_state[q_key] = options_with_index
    
    options_with_index = st.session_state[q_key]
    shuffled_options = [opt[1] for opt in options_with_index]
    
    st.subheader(q["question"])
    
    # Vérifier si c'est une question à choix multiples
    is_multiple = isinstance(q["correct"], list)
    
    if is_multiple:
        selected = st.multiselect(
            "Choisis toutes les bonnes réponses :",
            shuffled_options,
            key=f"{session_key}_{current}"
        )
    else:
        selected = st.radio(
            "Choisis ta réponse :",
            shuffled_options,
            key=f"{session_key}_{current}",
            index=None
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Valider", key=f"valider_{session_key}_{current}", use_container_width=True):
            if is_multiple:
                if selected:
                    # Trouver les indices originaux des options sélectionnées
                    correct_indices = q["correct"]
                    correct_options = [q["options"][i] for i in correct_indices]
                    is_correct = set(selected) == set(correct_options)
                    
                    quiz["answers"].append({
                        "question": q["question"],
                        "selected": ", ".join(selected),
                        "correct": ", ".join(correct_options),
                        "is_correct": is_correct,
                        "explication": q["explication"]
                    })
                    
                    if is_correct:
                        quiz["score"] += 1
                    quiz["current"] += 1
                    st.rerun()
                else:
                    st.warning("Sélectionne au moins une réponse !")
            else:
                if selected is not None:
                    # Trouver l'index original de l'option sélectionnée
                    selected_original_index = q["options"].index(selected)
                    is_correct = (selected_original_index == q["correct"])
                    
                    quiz["answers"].append({
                        "question": q["question"],
                        "selected": selected,
                        "correct": q["options"][q["correct"]],
                        "is_correct": is_correct,
                        "explication": q["explication"]
                    })
                    
                    if is_correct:
                        quiz["score"] += 1
                    quiz["current"] += 1
                    st.rerun()
                else:
                    st.warning("Sélectionne une réponse avant de valider !")
    
    with col2:
        if st.button("🔄 Recommencer ce quiz", key=f"reset_{session_key}", use_container_width=True):
            st.session_state[session_key] = {"current": 0, "score": 0, "answers": [], "finished": False}
            # Supprimer les mélanges pour régénérer
            for key in list(st.session_state.keys()):
                if key.startswith(f"shuffled_{theme_name}") or key.startswith(f"shuffled_options_{theme_name}"):
                    del st.session_state[key]
            st.rerun()

# ============================================================
# RÉSULTATS
# ============================================================

elif quiz["finished"] or current >= total:
    st.balloons()
    st.success("🎉 Quiz terminé !")
    
    score = quiz["score"]
    pourcentage = round((score / total) * 100) if total > 0 else 0
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;">
            <h1>{score} / {total}</h1>
            <h2>{pourcentage}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    if pourcentage >= 90:
        st.success("🌟 Excellent ! Tu maîtrises ce thème !")
    elif pourcentage >= 70:
        st.info("📚 Bien joué ! Revois quelques points pour être parfait.")
    elif pourcentage >= 50:
        st.warning("🤔 Pas mal, mais il faut réviser certaines parties.")
    else:
        st.error("📖 Il faut sérieusement réviser ce thème !")
    
    with st.expander("📋 Voir le détail des réponses"):
        for i, ans in enumerate(quiz["answers"]):
            if ans["is_correct"]:
                st.success(f"✅ **{i+1}.** {ans['question']}")
            else:
                st.error(f"❌ **{i+1}.** {ans['question']}")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;Ta réponse : **{ans['selected']}**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;Bonne réponse : **{ans['correct']}**")
            st.info(f"💡 {ans['explication']}")
            st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Recommencer ce quiz", key=f"reset_final_{session_key}", use_container_width=True):
            st.session_state[session_key] = {"current": 0, "score": 0, "answers": [], "finished": False}
            for key in list(st.session_state.keys()):
                if key.startswith(f"shuffled_{theme_name}") or key.startswith(f"shuffled_options_{theme_name}"):
                    del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("🏠 Changer de thème", use_container_width=True):
            st.session_state[session_key] = {"current": 0, "score": 0, "answers": [], "finished": False}
            for key in list(st.session_state.keys()):
                if key.startswith(f"shuffled_{theme_name}") or key.startswith(f"shuffled_options_{theme_name}"):
                    del st.session_state[key]
            st.rerun()

# ============================================================
# PIED DE PAGE
# ============================================================

st.divider()
st.caption("🚗 Quiz Code de la Route – 5 thèmes | 39 questions")