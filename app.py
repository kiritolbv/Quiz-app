import streamlit as st

st.set_page_config(page_title="Quiz Code de la Route", page_icon="🚗", layout="centered")
st.title("🚗 Quiz – Code de la Route")
st.markdown("### Fiche mémo – 38 questions")
st.divider()

questions = [
    {"question": "Quelle est la vitesse maximale autorisée en agglomération ?", "options": ["30 km/h", "50 km/h", "70 km/h", "90 km/h"], "correct": 1},
    {"question": "Quelle est la vitesse maximale autorisée hors agglomération (valeur générale) ?", "options": ["70 km/h", "80 km/h", "90 km/h", "100 km/h"], "correct": 1},
    {"question": "Que deviennent les distances de réaction, de freinage et d'arrêt quand la vitesse augmente ?", "options": ["Elles diminuent", "Elles restent identiques", "Elles augmentent", "Seule la distance de freinage augmente"], "correct": 2},
    {"question": "Lequel de ces facteurs n'augmente PAS le temps de réaction ?", "options": ["La fatigue", "L'alcool", "La distraction", "Une bonne visibilité"], "correct": 3},
    {"question": "Hors agglomération, quelle autre vitesse est parfois autorisée sur certaines sections aménagées ?", "options": ["70 km/h", "80 km/h", "90 km/h", "110 km/h"], "correct": 2},
    {"question": "Dans une voie verte, qui doit céder le passage ?", "options": ["Celui qui entre", "Celui qui sort", "Celui qui va tout droit", "Celui qui est le plus lent"], "correct": 1},
    {"question": "Que doit faire un conducteur qui rencontre un obstacle sur sa voie ?", "options": ["Il accélère pour passer vite", "Il klaxonne", "Il cède le passage", "Il fait demi-tour"], "correct": 2},
    {"question": "Dans un giratoire, qui a la priorité ?", "options": ["Les véhicules qui entrent", "Les véhicules déjà engagés", "Les véhicules venant de droite", "Les véhicules les plus rapides"], "correct": 1},
    {"question": "Dans un rond-point, quelle est la règle de priorité par défaut (sauf signalisation) ?", "options": ["Priorité à gauche", "Priorité à droite", "Priorité aux poids lourds", "Priorité à celui qui va le plus vite"], "correct": 1},
    {"question": "Au feu vert, si je tourne, que dois-je laisser passer ?", "options": ["Les véhicules venant de droite", "Les véhicules venant de gauche", "Les usagers venant en face", "Les piétons uniquement"], "correct": 2},
    {"question": "Dans quel cas ne dois-je PAS utiliser mon clignotant ?", "options": ["Pour tourner à gauche", "Pour tourner à droite", "Pour continuer tout droit", "Pour sortir d'un stationnement"], "correct": 2},
    {"question": "Dans un giratoire, quand dois-je mettre le clignotant à gauche ?", "options": ["Pour aller tout droit", "Pour sortir à droite", "Pour aller à gauche ou faire demi-tour", "Pour entrer dans le giratoire"], "correct": 2},
    {"question": "Si un véhicule me dépasse, quelle est la bonne attitude ?", "options": ["Accélérer pour ne pas être dépassé", "Me rabattre brusquement", "Maintenir mon allure et serrer à droite", "Mettre mes feux de détresse"], "correct": 2},
    {"question": "Dans cette situation, qu'est-ce que je ne dois JAMAIS faire ?", "options": ["Serrer à droite", "Accélérer", "Ralentir", "Rester sur ma voie"], "correct": 1},
    {"question": "Quel est l'effet de la pluie sur la distance de freinage ?", "options": ["Elle diminue", "Elle reste identique", "Elle augmente", "Elle est divisée par deux"], "correct": 2},
    {"question": "La nuit, hors agglomération, quand dois-je éteindre mes feux de route ?", "options": ["Quand il pleut", "Quand je suis en ville", "Seulement si personne n'arrive en face", "Quand quelqu'un arrive en face (ou me suit de près)"], "correct": 3},
    {"question": "Sur quelles roues doit-on monter les chaînes en cas de neige ?", "options": ["Sur les 4 roues", "Sur les roues avant uniquement", "Sur les roues arrière uniquement", "Sur les roues motrices"], "correct": 3},
    {"question": "Dans quelles situations dois-je allumer mes feux de détresse ?", "options": ["Quand je roule vite", "En cas de ralentissement important ou danger inhabituel", "Quand je dépasse", "Quand je m'arrête pour faire une pause"], "correct": 1},
    {"question": "Sur une voie rapide, si des véhicules sont immobilisés, que dois-je faire si possible ?", "options": ["Mettre mes warnings", "Changer de voie", "Ralentir fortement", "Klaxonner"], "correct": 1},
    {"question": "Que signifie une ligne jaune continue ?", "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Rien de particulier"], "correct": 1},
    {"question": "Que signifie une ligne jaune discontinue ?", "options": ["Stationnement interdit, arrêt autorisé", "Arrêt et stationnement interdits", "Arrêt interdit, stationnement autorisé", "Stationnement autorisé uniquement pour les riverains"], "correct": 0},
    {"question": "Dans quel cas est-il interdit de tenir son téléphone en main ?", "options": ["À l'arrêt à un feu rouge", "Dans un parking", "Sauf véhicule correctement stationné (donc interdit en circulation)", "Toujours autorisé si on utilise un GPS"], "correct": 2},
    {"question": "Que ne dois-je JAMAIS faire devant ou derrière un bus à l'arrêt ?", "options": ["Attendre qu'il reparte", "Traverser", "Klaxonner", "Contourner par la gauche"], "correct": 1},
    {"question": "De quoi dépend l'autonomie d'un véhicule électrique ?", "options": ["De la couleur et de la marque", "Du style de conduite et de la charge de la batterie", "De la météo et du nombre de passagers", "De l'âge du conducteur et du pneu"], "correct": 1},
    {"question": "Que signale le voyant de pression ?", "options": ["Un problème de moteur", "Un pneu sous-gonflé", "Un problème de frein", "Une batterie faible"], "correct": 1},
    {"question": "Que signifie un 'pollution non conforme' au contrôle technique ?", "options": ["Une réparation simple", "Une défaillance majeure", "Un voyant à changer", "Une usure normale"], "correct": 1},
    {"question": "Quel autre nom désigne le diesel ?", "options": ["Super", "Gazole", "Éthanol", "GPL"], "correct": 1},
    {"question": "Le chargement peut-il dépasser à l'avant et/ou à l'arrière ?", "options": ["Ni à l'avant ni à l'arrière", "Uniquement à l'avant", "Uniquement à l'arrière", "À l'avant et à l'arrière"], "correct": 2},
    {"question": "Quelle est la limite d'alcool pour un jeune conducteur (en g/L) ?", "options": ["0,50 g/L", "0,20 g/L", "0,10 g/L", "0,80 g/L"], "correct": 1},
    {"question": "Qu'est-ce qui est inclus dans l'autopartage ?", "options": ["Le carburant, le péage et le lavage", "L'énergie, l'assurance et l'entretien", "Les pneus, le GPS et le siège bébé", "Le parking, les taxes et le nettoyage"], "correct": 1},
    {"question": "Qui paie les péages dans l'autopartage ?", "options": ["Le propriétaire du véhicule", "L'utilisateur", "L'assureur", "La société d'autopartage"], "correct": 1},
    {"question": "Quand peut-on compléter le verso du constat amiable ?", "options": ["Avant la signature", "Pendant la signature", "Après la signature", "Uniquement le lendemain"], "correct": 2},
    {"question": "Dans un giratoire, la priorité est à ?", "options": ["Droite", "Gauche", "Celui qui entre", "Celui qui sort"], "correct": 1},
    {"question": "Face à un obstacle, je ?", "options": ["Accélère", "Klaxonne", "Cède", "Dépasse"], "correct": 2},
    {"question": "Sous la pluie, le freinage est ?", "options": ["Plus court", "Plus long", "Identique", "Impossible"], "correct": 1},
    {"question": "Devant un bus à l'arrêt, j' ?", "options": ["Traverse vite", "Attends qu'il reparte", "Klaxonne", "Le dépasse par la droite"], "correct": 1},
    {"question": "Pour un jeune conducteur, la limite d'alcool est de ?", "options": ["0,50 g/L", "0,20 g/L", "0,30 g/L", "0,00 g/L"], "correct": 1},
    {"question": "Règle des feux de route la nuit hors agglo :", "options": ["Toujours allumés", "Éteints en ville seulement", "Allumés seulement si personne n'arrive en face", "Allumés seulement quand il pleut"], "correct": 2}
]

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.finished = False
    st.session_state.selected = None

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.finished = False
    st.session_state.selected = None

total_questions = len(questions)
current = st.session_state.current_question

if not st.session_state.finished and current < total_questions:
    q = questions[current]
    st.progress(current / total_questions)
    st.markdown(f"**Question {current + 1} / {total_questions}**")
    st.divider()
    st.subheader(q["question"])
    options = q["options"]
    selected = st.radio("Choisis une réponse :", options, key=f"q_{current}", index=None)
    
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("✅ Valider", use_container_width=True):
            if selected is not None:
                correct_index = q["correct"]
                is_correct = (options.index(selected) == correct_index)
                st.session_state.answers.append({"question": q["question"], "selected": selected, "correct": options[correct_index], "is_correct": is_correct})
                if is_correct: st.session_state.score += 1
                st.session_state.current_question += 1
                st.session_state.selected = None
                st.rerun()
            else:
                st.warning("Veuillez sélectionner une réponse !")
    with col2:
        if st.button("🔄 Réinitialiser", use_container_width=True):
            reset_quiz()
            st.rerun()

elif st.session_state.finished or current >= total_questions:
    st.balloons()
    st.success("🎉 Quiz terminé !")
    score = st.session_state.score
    total = total_questions
    pourcentage = round((score / total) * 100)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;">
            <h1>{score} / {total}</h1>
            <h2>{pourcentage}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    if pourcentage >= 90: st.success("🌟 Excellent ! Tu es un as du Code !")
    elif pourcentage >= 70: st.info("📚 Bien joué ! Revois les points faibles pour être parfait.")
    elif pourcentage >= 50: st.warning("🤔 Pas mal, mais il faut réviser certaines parties.")
    else: st.error("📖 Il faut sérieusement réviser la fiche mémo !")
    
    with st.expander("📋 Voir le détail des réponses"):
        for i, ans in enumerate(st.session_state.answers):
            if ans["is_correct"]: st.success(f"✅ **{i+1}.** {ans['question']}")
            else:
                st.error(f"❌ **{i+1}.** {ans['question']}")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;Ta réponse : **{ans['selected']}**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;Bonne réponse : **{ans['correct']}**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Recommencer le quiz", use_container_width=True):
            reset_quiz()
            st.rerun()
    with col2:
        if st.button("🏠 Accueil", use_container_width=True):
            reset_quiz()
            st.rerun()

st.divider()
st.caption("🚗 Quiz Code de la Route – Basé sur la fiche mémo officielle")
