import streamlit as st

# Configuration
st.set_page_config(
    page_title="Quiz Code de la Route",
    page_icon="🚗",
    layout="centered"
)

# ============================================================
# THÈMES AVEC LEURS QUESTIONS
# ============================================================

themes = {
    "💡 Éclairage & Visibilité": {
        "icon": "💡",
        "questions": [
            {
                "question": "À quel moment dois-tu utiliser tes feux de route la nuit hors agglomération ?",
                "options": ["Tout le temps", "Seulement quand il n'y a personne en face", "Jamais, je roule aux feux de croisement", "Seulement en ville"],
                "correct": 1,
                "explication": "Les feux de route éblouissent les autres conducteurs. Il faut les éteindre dès qu'un véhicule arrive en face."
            },
            {
                "question": "Dans un giratoire, quand dois-tu mettre ton clignotant à gauche ?",
                "options": ["Quand je sors à droite", "Quand je vais tout droit", "Quand je vais à gauche ou fais demi-tour", "Je ne mets jamais de clignotant dans un giratoire"],
                "correct": 2,
                "explication": "Le clignotant gauche indique que tu restes engagé dans le giratoire pour aller à gauche ou faire demi-tour."
            },
            {
                "question": "Dans quel cas n'as-tu PAS besoin d'utiliser ton clignotant ?",
                "options": ["Pour tourner à droite", "Pour tourner à gauche", "Pour continuer tout droit", "Pour sortir d'un stationnement"],
                "correct": 2,
                "explication": "Le clignotant sert à indiquer un changement de direction. Si tu continues tout droit, pas besoin."
            },
            {
                "question": "À quelle distance approximative les feux de route éclairent-ils ?",
                "options": ["30 mètres", "100 mètres", "200 mètres", "500 mètres"],
                "correct": 2,
                "explication": "Les feux de route éclairent jusqu'à environ 200 mètres, contre 30 mètres pour les feux de croisement."
            },
            {
                "question": "Quand dois-tu utiliser tes feux de brouillard avant ?",
                "options": ["Quand il pleut légèrement", "Quand il y a du brouillard ou des chutes de neige", "Quand il fait nuit en ville", "Toujours, c'est plus sûr"],
                "correct": 1,
                "explication": "Les feux de brouillard avant sont réservés aux conditions de visibilité réduite (brouillard, neige, pluie intense)."
            },
            {
                "question": "Que signifient tes feux de détresse (warning) ?",
                "options": ["Je vais me garer", "J'indique un danger ou un ralentissement important", "Je remercie un autre conducteur", "Je vais faire demi-tour"],
                "correct": 1,
                "explication": "Les feux de détresse signalent un danger inhabituel ou un ralentissement brutal aux autres usagers."
            },
            {
                "question": "Sur une voie rapide, que dois-tu faire si tu vois des véhicules immobilisés ?",
                "options": ["Klaxonner pour les prévenir", "Ralentir et rester sur ta voie", "Changer de voie si possible", "Accélérer pour passer vite"],
                "correct": 2,
                "explication": "Changer de voie permet d'éviter les véhicules immobilisés et de protéger les personnes qui pourraient être à côté."
            },
            {
                "question": "Quand dois-tu allumer tes feux de croisement ?",
                "options": ["Uniquement la nuit", "La nuit et quand la visibilité est réduite", "Uniquement quand il pleut", "Toujours, même en plein jour"],
                "correct": 1,
                "explication": "Les feux de croisement sont obligatoires la nuit, mais aussi par temps de pluie, brouillard ou dans les tunnels."
            },
            {
                "question": "Un véhicule arrive en face avec ses feux de route allumés. Que fais-tu ?",
                "options": ["Tu allumes tes feux de route aussi", "Tu klaxonnes pour le prévenir", "Tu ralentis et regardes sur le bord droit", "Tu fais un appel de phares et tu restes concentré"],
                "correct": 2,
                "explication": "Il faut ralentir et regarder sur le bord droit de la chaussée pour ne pas être ébloui. Un bref appel de phares peut rappeler l'autre conducteur."
            },
            {
                "question": "Que signifie un clignotant droit dans un giratoire ?",
                "options": ["Je vais à gauche", "Je sors du giratoire", "Je vais tout droit", "Je fais demi-tour"],
                "correct": 1,
                "explication": "Le clignotant droit indique que tu vas sortir du giratoire à la prochaine sortie."
            }
        ]
    },
    "🚦 Priorités & Intersections": {
        "icon": "🚦",
        "questions": [
            {
                "question": "Dans un giratoire, qui a la priorité ?",
                "options": ["Celui qui entre", "Celui qui est déjà engagé", "Celui qui va le plus vite", "Celui qui vient de droite"],
                "correct": 1,
                "explication": "La règle dans un giratoire est : priorité à gauche, donc aux véhicules déjà engagés."
            },
            {
                "question": "Dans un rond-point (sans signalisation), qui a la priorité ?",
                "options": ["Priorité à gauche", "Priorité à droite", "Priorité à celui qui entre", "Priorité au plus gros véhicule"],
                "correct": 1,
                "explication": "Par défaut, dans un rond-point (non giratoire), c'est la priorité à droite qui s'applique."
            },
            {
                "question": "Dans une voie verte, qui doit céder le passage ?",
                "options": ["Celui qui entre", "Celui qui sort", "Celui qui va tout droit", "Personne, c'est prioritaire"],
                "correct": 1,
                "explication": "La voie verte est prioritaire. Celui qui en sort doit céder le passage aux usagers qui restent sur la voie."
            },
            {
                "question": "Au feu vert, si tu tournes à droite, que dois-tu faire ?",
                "options": ["Tu passes sans t'arrêter", "Tu laisses passer les piétons qui traversent", "Tu laisses passer les usagers venant en face", "Tu klaxonnes pour signaler ta présence"],
                "correct": 1,
                "explication": "Au feu vert, tu dois laisser passer les piétons qui traversent et les vélos si un sas vélo existe."
            },
            {
                "question": "Que fais-tu si un obstacle bloque ta voie ?",
                "options": ["Tu accélères pour le contourner", "Tu klaxonnes pour qu'il bouge", "Tu cèdes le passage", "Tu fais demi-tour"],
                "correct": 2,
                "explication": "En présence d'un obstacle, c'est à toi de céder le passage si tu peux le contourner."
            },
            {
                "question": "Qui a la priorité dans une intersection avec panneau 'STOP' ?",
                "options": ["Le premier arrivé", "Celui qui vient de droite", "Celui qui s'est arrêté en premier", "Aucun, il faut s'arrêter et céder le passage à tous"],
                "correct": 3,
                "explication": "Le STOP impose de s'arrêter et de céder le passage à tous les usagers avant de s'engager."
            },
            {
                "question": "Quand tu arrives à un feu rouge, tu dois :",
                "options": ["Ralentir et passer si rien ne vient", "T'arrêter au niveau du feu", "T'arrêter avant la ligne d'arrêt", "T'arrêter après la ligne d'arrêt"],
                "correct": 2,
                "explication": "L'arrêt doit se faire avant le marquage au sol (ligne d'arrêt ou sas vélo)."
            },
            {
                "question": "Que signifie un panneau 'Cédez le passage' ?",
                "options": ["Tu as la priorité", "Tu dois t'arrêter obligatoirement", "Tu dois ralentir et céder si nécessaire", "Tu dois accélérer pour passer"],
                "correct": 2,
                "explication": "Le cédez-le-passage signifie que tu dois ralentir et laisser passer si d'autres usagers arrivent."
            },
            {
                "question": "Dans une intersection sans signalisation, qui a la priorité ?",
                "options": ["Celui qui vient de gauche", "Celui qui vient de droite", "Le premier arrivé", "Aucun, c'est au jugement"],
                "correct": 1,
                "explication": "Sans signalisation, c'est la règle de la priorité à droite qui s'applique en France."
            },
            {
                "question": "Tu arrives à un feu orange. Que fais-tu ?",
                "options": ["Tu accélères pour passer", "Tu freines si c'est possible sans danger", "Tu passes toujours", "Tu klaxonnes pour prévenir"],
                "correct": 1,
                "explication": "Le feu orange signifie : tu dois t'arrêter si tu peux le faire en sécurité. Sinon, tu passes avec prudence."
            }
        ]
    },
    "🏎️ Vitesse & Distances": {
        "icon": "🏎️",
        "questions": [
            {
                "question": "Quelle est la vitesse maximale en agglomération ?",
                "options": ["30 km/h", "50 km/h", "70 km/h", "90 km/h"],
                "correct": 1,
                "explication": "La vitesse maximale en ville est de 50 km/h, sauf zones à 30 km/h."
            },
            {
                "question": "Quelle est la vitesse maximale hors agglomération (valeur générale) ?",
                "options": ["70 km/h", "80 km/h", "90 km/h", "100 km/h"],
                "correct": 1,
                "explication": "Hors agglomération, la limite générale est de 80 km/h (sauf sections à 90 km/h)."
            },
            {
                "question": "Que deviennent les distances d'arrêt quand tu roules plus vite ?",
                "options": ["Elles diminuent", "Elles restent identiques", "Elles augmentent", "Seule la distance de freinage augmente"],
                "correct": 2,
                "explication": "La distance d'arrêt = distance de réaction + distance de freinage. Les deux augmentent avec la vitesse."
            },
            {
                "question": "Qu'est-ce qui augmente ton temps de réaction ?",
                "options": ["L'expérience", "La fatigue et l'alcool", "Une bonne visibilité", "Des pneus neufs"],
                "correct": 1,
                "explication": "La fatigue, l'alcool, les médicaments et la distraction allongent le temps de réaction."
            },
            {
                "question": "Quelle est la vitesse maximale sur autoroute par temps de pluie ?",
                "options": ["80 km/h", "100 km/h", "110 km/h", "130 km/h"],
                "correct": 2,
                "explication": "Sur autoroute, la vitesse maximale est de 110 km/h par temps de pluie (130 km/h par temps sec)."
            },
            {
                "question": "Quelle est la distance de sécurité minimale sur autoroute ?",
                "options": ["50 mètres", "2 secondes", "100 mètres", "5 secondes"],
                "correct": 1,
                "explication": "La règle des 2 secondes : garde 2 secondes d'intervalle avec le véhicule qui te précède (environ 73 mètres à 130 km/h)."
            },
            {
                "question": "À 50 km/h, quelle est approximativement ta distance d'arrêt ?",
                "options": ["10 mètres", "25 mètres", "40 mètres", "60 mètres"],
                "correct": 1,
                "explication": "À 50 km/h, la distance d'arrêt est d'environ 25 mètres (réaction + freinage)."
            },
            {
                "question": "Hors agglomération, sur certaines routes, quelle autre vitesse est autorisée ?",
                "options": ["70 km/h", "80 km/h", "90 km/h", "100 km/h"],
                "correct": 2,
                "explication": "Certaines routes sont aménagées pour permettre une vitesse de 90 km/h, mais c'est l'exception."
            },
            {
                "question": "Qu'est-ce qui ralentit ta distance de freinage ?",
                "options": ["Des pneus neufs", "Une chaussée mouillée", "Un moteur puissant", "Des freins récents"],
                "correct": 1,
                "explication": "L'eau sur la chaussée réduit l'adhérence, ce qui augmente considérablement la distance de freinage."
            },
            {
                "question": "Que signifie la règle du 'quart de la distance de sécurité' ?",
                "options": ["Il faut un quart de la distance d'arrêt devant toi", "Tu dois ralentir d'un quart de ta vitesse", "C'est une règle pour les motos", "C'est une vieille règle qui n'existe plus"],
                "correct": 0,
                "explication": "Sur route mouillée, il faut doubler la distance de sécurité (2 secondes → 4 secondes)."
            }
        ]
    },
    "🛑 Stationnement & Arrêt": {
        "icon": "🛑",
        "questions": [
            {
                "question": "Que signifie une ligne jaune continue au bord de la chaussée ?",
                "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Rien de particulier"],
                "correct": 1,
                "explication": "La ligne jaune continue interdit l'arrêt ET le stationnement sur toute sa longueur."
            },
            {
                "question": "Que signifie une ligne jaune discontinue ?",
                "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Stationnement payant"],
                "correct": 0,
                "explication": "La ligne jaune discontinue signifie : le stationnement est interdit, mais l'arrêt (déposer un passager) est autorisé."
            },
            {
                "question": "Dans quel cas est-il interdit de tenir son téléphone en main ?",
                "options": ["À l'arrêt à un feu rouge", "Dans un parking", "Sauf si tu es stationné correctement", "Toujours autorisé si tu as le Bluetooth"],
                "correct": 2,
                "explication": "Tu ne peux pas tenir ton téléphone en main en conduisant. C'est autorisé si tu es à l'arrêt ET correctement stationné."
            },
            {
                "question": "Que signifie un passage piéton surélevé ?",
                "options": ["Les voitures doivent ralentir", "Les piétons ont la priorité absolue", "C'est pour les cyclistes", "Ça permet de réduire la vitesse"],
                "correct": 1,
                "explication": "Sur un passage piéton surélevé, les piétons ont la priorité absolue."
            },
            {
                "question": "Peux-tu t'arrêter sur un trottoir ?",
                "options": ["Oui, si c'est pour déposer quelqu'un", "Oui, si tu mets tes warnings", "Non, jamais", "Oui, uniquement la nuit"],
                "correct": 2,
                "explication": "Il est interdit de s'arrêter ou de stationner sur un trottoir, sauf si une signalisation l'autorise."
            },
            {
                "question": "Où ne peux-tu PAS stationner dans une intersection ?",
                "options": ["À plus de 5 mètres", "À moins de 5 mètres", "À moins de 10 mètres", "N'importe où, l'intersection est prioritaire"],
                "correct": 1,
                "explication": "Le stationnement est interdit à moins de 5 mètres d'une intersection."
            },
            {
                "question": "Que dois-tu faire avant d'ouvrir ta portière ?",
                "options": ["Rien, c'est la rue", "Regarder dans le rétroviseur et derrière toi", "Klaxonner pour prévenir", "Ouvrir la portière très lentement"],
                "correct": 1,
                "explication": "Tu dois t'assurer qu'aucun véhicule ou cycliste n'arrive avant d'ouvrir ta portière."
            },
            {
                "question": "Peux-tu stationner sur une piste cyclable ?",
                "options": ["Oui, si c'est pour 5 minutes", "Oui, en mettant tes warnings", "Non, jamais", "Oui, la nuit"],
                "correct": 2,
                "explication": "Le stationnement sur une piste cyclable est totalement interdit."
            }
        ]
    },
    "⚠️ Sécurité & Divers": {
        "icon": "⚠️",
        "questions": [
            {
                "question": "Quel est l'effet de la pluie sur ta conduite ?",
                "options": ["Ça réduit le temps de réaction", "Ça augmente la distance de freinage", "Ça améliore l'adhérence", "Ça n'a pas d'effet"],
                "correct": 1,
                "explication": "La pluie rend la chaussée glissante et augmente la distance de freinage."
            },
            {
                "question": "Quelle est la limite d'alcool pour un jeune conducteur (en g/L) ?",
                "options": ["0,50 g/L", "0,20 g/L", "0,10 g/L", "0,80 g/L"],
                "correct": 1,
                "explication": "Pour les jeunes conducteurs (permis probatoire), la limite est de 0,20 g/L, contre 0,50 g/L pour les conducteurs expérimentés."
            },
            {
                "question": "Que dois-tu faire si un véhicule te dépasse ?",
                "options": ["Accélérer pour ne pas te faire dépasser", "Maintenir ton allure et serrer à droite", "Ralentir brusquement", "Mettre tes feux de détresse"],
                "correct": 1,
                "explication": "Si tu es dépassé, tu dois garder ton allure et te serrer à droite pour faciliter le dépassement."
            },
            {
                "question": "Dans cette situation, que NE DOIS-TU JAMAIS faire ?",
                "options": ["Serrer à droite", "Accélérer", "Ralentir", "Rester sur ta voie"],
                "correct": 1,
                "explication": "N'accélère jamais quand quelqu'un te dépasse, c'est dangereux et interdit."
            },
            {
                "question": "Où dois-tu monter les chaînes en cas de neige ?",
                "options": ["Sur les 4 roues", "Sur les roues avant", "Sur les roues arrière", "Sur les roues motrices"],
                "correct": 3,
                "explication": "Les chaînes se montent sur les roues motrices (avant ou arrière selon le véhicule)."
            },
            {
                "question": "Qu'est-ce que l'autopartage inclut généralement ?",
                "options": ["Carburant, péage et lavage", "Énergie, assurance et entretien", "Pneus, GPS et siège bébé", "Parking, taxes et nettoyage"],
                "correct": 1,
                "explication": "L'autopartage inclut l'énergie (électricité/carburant), l'assurance et l'entretien. Les péages sont à la charge de l'utilisateur."
            },
            {
                "question": "Que signifie un voyant de pression qui s'allume ?",
                "options": ["Un problème de moteur", "Un pneu sous-gonflé", "Un problème de frein", "Une batterie faible"],
                "correct": 1,
                "explication": "Le voyant de pression des pneus indique qu'au moins un pneu est sous-gonflé."
            },
            {
                "question": "Que signifie 'Pollution non conforme' au contrôle technique ?",
                "options": ["Une réparation simple", "Une défaillance majeure", "Un voyant à changer", "Une usure normale"],
                "correct": 1,
                "explication": "Une pollution non conforme est considérée comme une défaillance majeure. Le véhicule doit être réparé."
            },
            {
                "question": "Le chargement de ton véhicule peut-il dépasser ?",
                "options": ["Ni à l'avant ni à l'arrière", "Uniquement à l'avant", "Uniquement à l'arrière", "À l'avant et à l'arrière"],
                "correct": 2,
                "explication": "Le chargement peut dépasser à l'arrière, mais jamais à l'avant du véhicule."
            },
            {
                "question": "Qui paie les péages dans un autopartage ?",
                "options": ["Le propriétaire", "L'utilisateur", "L'assureur", "La société d'autopartage"],
                "correct": 1,
                "explication": "Les péages sont toujours à la charge de l'utilisateur de l'autopartage."
            }
        ]
    }
}

# ============================================================
# INTERFACE PRINCIPALE
# ============================================================

st.title("🚗 Quiz Code de la Route")
st.markdown("### Choisis un thème et teste tes connaissances !")

# Sélection du thème
theme_names = list(themes.keys())
selected_theme = st.selectbox(
    "📚 Sélectionne un thème :",
    theme_names,
    format_func=lambda x: f"{themes[x]['icon']} {x}"
)

st.divider()

# ============================================================
# QUIZ DU THÈME SÉLECTIONNÉ
# ============================================================

if selected_theme:
    theme_data = themes[selected_theme]
    questions = theme_data["questions"]
    
    # Initialisation des variables de session pour ce thème
    session_key = f"quiz_{selected_theme}"
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
    st.progress(current / total)
    st.markdown(f"**Question {current + 1} / {total}**")
    
    if not quiz["finished"] and current < total:
        q = questions[current]
        
        st.subheader(q["question"])
        
        # Afficher les options
        selected = st.radio(
            "Choisis ta réponse :",
            q["options"],
            key=f"{session_key}_{current}",
            index=None
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Valider", key=f"valider_{session_key}_{current}", use_container_width=True):
                if selected is not None:
                    correct_index = q["correct"]
                    is_correct = (q["options"].index(selected) == correct_index)
                    
                    quiz["answers"].append({
                        "question": q["question"],
                        "selected": selected,
                        "correct": q["options"][correct_index],
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
                st.session_state[session_key] = {
                    "current": 0,
                    "score": 0,
                    "answers": [],
                    "finished": False
                }
                st.rerun()
    
    elif quiz["finished"] or current >= total:
        # Résultats
        st.balloons()
        st.success("🎉 Quiz terminé !")
        
        score = quiz["score"]
        pourcentage = round((score / total) * 100)
        
        # Affichage du score
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;">
                <h1>{score} / {total}</h1>
                <h2>{pourcentage}%</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Appréciation
        if pourcentage >= 90:
            st.success("🌟 Excellent ! Tu maîtrises ce thème !")
        elif pourcentage >= 70:
            st.info("📚 Bien joué ! Revois quelques points pour être parfait.")
        elif pourcentage >= 50:
            st.warning("🤔 Pas mal, mais il faut réviser certaines parties.")
        else:
            st.error("📖 Il faut sérieusement réviser ce thème !")
        
        # Détail des réponses
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
                st.session_state[session_key] = {
                    "current": 0,
                    "score": 0,
                    "answers": [],
                    "finished": False
                }
                st.rerun()
        with col2:
            if st.button("🏠 Changer de thème", use_container_width=True):
                # Réinitialiser sans changer de thème (le selectbox fera le changement)
                for key in st.session_state.keys():
                    if key.startswith("quiz_"):
                        st.session_state[key]["finished"] = False
                        st.session_state[key]["current"] = 0
                st.rerun()

# Pied de page
st.divider()
st.caption("🚗 Quiz Code de la Route – 5 thèmes | 48 questions")
