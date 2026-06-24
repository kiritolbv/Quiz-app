import streamlit as st
import random

# ============================================================
# CHARGEMENT DES QUESTIONS DEPUIS LE FICHIER TXT
# ============================================================

def load_questions_from_txt(file_path="questions.txt"):
    """Charge les questions depuis un fichier texte formaté"""
    themes = {}
    current_theme = None
    current_question = None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        st.error(f"❌ Fichier {file_path} introuvable !")
        return {}
    
    for line in lines:
        line = line.strip()
        
        if not line or line.startswith("#"):
            continue
        
        if line.startswith("[THÈME]"):
            current_theme = line.replace("[THÈME]", "").strip()
            if current_theme not in themes:
                themes[current_theme] = []
            continue
        
        if line.startswith("Q:"):
            current_question = {
                "question": line.replace("Q:", "").strip(),
                "options": [],
                "correct": None,
                "explication": ""
            }
            continue
        
        if line.startswith("O:") and current_question is not None:
            option = line.replace("O:", "").strip()
            current_question["options"].append(option)
            continue
        
        if line.startswith("C:") and current_question is not None:
            correct = line.replace("C:", "").strip()
            if correct.startswith("[") and correct.endswith("]"):
                current_question["correct"] = [int(x.strip()) for x in correct[1:-1].split(",")]
            else:
                current_question["correct"] = int(correct)
            continue
        
        if line.startswith("E:") and current_question is not None:
            current_question["explication"] = line.replace("E:", "").strip()
            continue
        
        if line.startswith("---") and current_question is not None:
            if current_theme and current_theme in themes:
                if all(k in current_question for k in ["question", "options", "correct", "explication"]):
                    themes[current_theme].append(current_question)
            current_question = None
    
    if current_question and current_theme and current_theme in themes:
        if all(k in current_question for k in ["question", "options", "correct", "explication"]):
            themes[current_theme].append(current_question)
    
    return themes

# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="Quiz Code de la Route",
    page_icon="🚗",
    layout="wide"
)

# ============================================================
# CHARGEMENT DES QUESTIONS
# ============================================================

themes = load_questions_from_txt()

if not themes:
    st.error("❌ Aucune question chargée. Vérifie le fichier questions.txt")
    st.stop()

# ============================================================
# GESTION DE L'ÉTAT DE LA PAGE
# ============================================================

# Initialiser l'état si nécessaire
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = None

# ============================================================
# PAGE D'ACCUEIL
# ============================================================

if st.session_state.page == 'home':
    # CSS pour centrer et styliser la page d'accueil
    st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #FF4B4B;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #666;
    }
    .stButton button {
        width: 100%;
        height: 180px;
        background-color: #f0f2f6;
        border: 2px solid transparent;
        border-radius: 15px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        font-size: 1rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
    }
    .stButton button:hover {
        background-color: #e0e2e6;
        border-color: #FF4B4B;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .theme-icon-home {
        font-size: 3rem;
    }
    .theme-name-home {
        font-size: 1.2rem;
        font-weight: 600;
    }
    .theme-count-home {
        font-size: 0.9rem;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

    # Titre
    st.markdown('<p class="main-title">🚗 Quiz Code de la Route</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Choisis un thème et teste tes connaissances !</p>', unsafe_allow_html=True)

    # Statistiques
    total_questions = sum(len(q) for q in themes.values())
    st.markdown(f"<p style='text-align:center; color:#888; margin-bottom:2rem;'>📚 {len(themes)} thèmes • {total_questions} questions</p>", unsafe_allow_html=True)

    # Grille des thèmes (3 colonnes)
    cols = st.columns(3)
    theme_list = list(themes.keys())
    
    for i, theme_name in enumerate(theme_list):
        with cols[i % 3]:
            icon = theme_name.split()[0] if theme_name else "📚"
            count = len(themes[theme_name])
            
            # Bouton qui change la page
            if st.button(
                f"{icon}\n\n**{theme_name}**\n\n{count} questions",
                key=f"home_{theme_name}",
                use_container_width=True
            ):
                st.session_state.page = 'quiz'
                st.session_state.selected_theme = theme_name
                # Nettoyer l'ancien état du quiz
                for key in list(st.session_state.keys()):
                    if key.startswith("quiz_"):
                        del st.session_state[key]
                st.rerun()

    # Pied de page
    st.divider()
    st.caption("🚗 Quiz Code de la Route – Questions modifiables dans questions.txt")

# ============================================================
# PAGE DU QUIZ (sans sidebar)
# ============================================================

elif st.session_state.page == 'quiz':
    # Récupérer le thème sélectionné
    theme_name = st.session_state.get('selected_theme', list(themes.keys())[0])
    questions = themes[theme_name]
    
    # Bouton retour à l'accueil (en haut)
    col_back, col_spacer = st.columns([1, 5])
    with col_back:
        if st.button("🏠 Retour à l'accueil", use_container_width=True):
            st.session_state.page = 'home'
            st.session_state.selected_theme = None
            # Nettoyer l'état du quiz
            for key in list(st.session_state.keys()):
                if key.startswith("quiz_"):
                    del st.session_state[key]
            st.rerun()
    
    st.divider()
    
    # Afficher le nom du thème
    icon = theme_name.split()[0] if theme_name else "📚"
    st.title(f"{icon} Quiz {theme_name}")
    
    # Mélanger les questions
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
        
        q_key = f"shuffled_options_{theme_name}_{current}"
        if q_key not in st.session_state:
            options_with_index = list(enumerate(q["options"]))
            random.shuffle(options_with_index)
            st.session_state[q_key] = options_with_index
        
        options_with_index = st.session_state[q_key]
        shuffled_options = [opt[1] for opt in options_with_index]
        
        st.subheader(q["question"])
        
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
            if st.button("🏠 Retour à l'accueil", use_container_width=True):
                st.session_state.page = 'home'
                st.session_state.selected_theme = None
                for key in list(st.session_state.keys()):
                    if key.startswith("quiz_"):
                        del st.session_state[key]
                st.rerun()
