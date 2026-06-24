import streamlit as st
import random

# ============================================================
# CHARGEMENT DES QUESTIONS
# ============================================================

def load_questions_from_txt(file_path="questions.txt"):
    themes = {}
    current_theme = None
    current_question = None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        st.error("Fichier questions.txt introuvable !")
        return {}
    
    for line in lines:
        line = line.strip()
        
        if not line or line.startswith("#"):
            continue
        
        if line.startswith("[THEME]"):
            current_theme = line.replace("[THEME]", "").strip()
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
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Quiz Code de la Route",
    page_icon="",
    layout="centered"
)

themes = load_questions_from_txt()

if not themes:
    st.error("Aucune question chargee. Verifie le fichier questions.txt")
    st.stop()

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = None

# ============================================================
# PAGE D'ACCUEIL
# ============================================================

if st.session_state.page == 'home':
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    .main-title {
        text-align: center;
        font-size: 5.5rem;
        font-weight: 900;
        color: #FF6B6B;
        margin-top: 2rem;
        margin-bottom: 0.2rem;
        text-shadow: 0 0 60px rgba(255,107,107,0.3);
        letter-spacing: 2px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.3rem;
        color: #a8a8b8;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }
    .stats {
        text-align: center;
        color: #8888aa;
        margin-bottom: 2.5rem;
        font-size: 1.1rem;
    }
    .stButton button {
        width: 100% !important;
        height: 70px !important;
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.8rem !important;
        transition: all 0.3s ease !important;
        text-align: center !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        letter-spacing: 0.5px;
    }
    .stButton button:hover {
        background: rgba(255,255,255,0.15) !important;
        border-color: #FF6B6B !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(255,107,107,0.2) !important;
    }
    .stButton button:active {
        transform: scale(0.97) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="main-title">QUIZ CODE</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Choisis un theme et teste tes connaissances</p>', unsafe_allow_html=True)

    total_questions = sum(len(q) for q in themes.values())
    st.markdown(f'<p class="stats">{len(themes)} themes  •  {total_questions} questions</p>', unsafe_allow_html=True)

    for theme_name in themes.keys():
        count = len(themes[theme_name])
        if st.button(f"{theme_name}  ({count} questions)", use_container_width=True):
            st.session_state.page = 'quiz'
            st.session_state.selected_theme = theme_name
            for key in list(st.session_state.keys()):
                if key.startswith("quiz_"):
                    del st.session_state[key]
            st.rerun()

# ============================================================
# PAGE DU QUIZ
# ============================================================

elif st.session_state.page == 'quiz':
    theme_name = st.session_state.get('selected_theme', list(themes.keys())[0])
    questions = themes[theme_name]
    
    if st.button("Retour a l'accueil", use_container_width=True):
        st.session_state.page = 'home'
        st.session_state.selected_theme = None
        for key in list(st.session_state.keys()):
            if key.startswith("quiz_"):
                del st.session_state[key]
        st.rerun()
    
    st.divider()
    
    st.title(f"Quiz : {theme_name}")
    
    if f"shuffled_{theme_name}" not in st.session_state:
        shuffled = questions.copy()
        random.shuffle(shuffled)
        st.session_state[f"shuffled_{theme_name}"] = shuffled
    
    questions = st.session_state[f"shuffled_{theme_name}"]
    
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
    
    st.progress(current / total if total > 0 else 0)
    st.markdown(f"**Question {current + 1} / {total}**")
    
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
                "Choisis toutes les bonnes reponses :",
                shuffled_options,
                key=f"{session_key}_{current}"
            )
        else:
            selected = st.radio(
                "Choisis ta reponse :",
                shuffled_options,
                key=f"{session_key}_{current}",
                index=None
            )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Valider", key=f"valider_{session_key}_{current}", use_container_width=True):
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
                        st.warning("Selectionne au moins une reponse !")
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
                        st.warning("Selectionne une reponse avant de valider !")
        
        with col2:
            if st.button("Recommencer", key=f"reset_{session_key}", use_container_width=True):
                st.session_state[session_key] = {"current": 0, "score": 0, "answers": [], "finished": False}
                for key in list(st.session_state.keys()):
                    if key.startswith(f"shuffled_{theme_name}") or key.startswith(f"shuffled_options_{theme_name}"):
                        del st.session_state[key]
                st.rerun()
    
    elif quiz["finished"] or current >= total:
        st.balloons()
        st.success("Quiz termine !")
        
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
            st.success("Excellent ! Tu maitrises ce theme !")
        elif pourcentage >= 70:
            st.info("Bien joue ! Revois quelques points pour etre parfait.")
        elif pourcentage >= 50:
            st.warning("Pas mal, mais il faut reviser certaines parties.")
        else:
            st.error("Il faut serieusement reviser ce theme !")
        
        with st.expander("Voir le detail des reponses"):
            for i, ans in enumerate(quiz["answers"]):
                if ans["is_correct"]:
                    st.success(f"**{i+1}.** {ans['question']}")
                else:
                    st.error(f"**{i+1}.** {ans['question']}")
                    st.markdown(f"Ta reponse : **{ans['selected']}**")
                    st.markdown(f"Bonne reponse : **{ans['correct']}**")
                st.info(f"{ans['explication']}")
                st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Recommencer", key=f"reset_final_{session_key}", use_container_width=True):
                st.session_state[session_key] = {"current": 0, "score": 0, "answers": [], "finished": False}
                for key in list(st.session_state.keys()):
                    if key.startswith(f"shuffled_{theme_name}") or key.startswith(f"shuffled_options_{theme_name}"):
                        del st.session_state[key]
                st.rerun()
        with col2:
            if st.button("Retour a l'accueil", use_container_width=True):
                st.session_state.page = 'home'
                st.session_state.selected_theme = None
                for key in list(st.session_state.keys()):
                    if key.startswith("quiz_"):
                        del st.session_state[key]
                st.rerun()
