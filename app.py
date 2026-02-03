#proposition Emilie#

import streamlit as st
from datetime import date


# --- Configuration de la page ---
st.set_page_config(page_title="Petite Enquête...", page_icon="🐾")

# --- CSS  ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stTextInput > label {font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# --- Gestion des étapes ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- BARRE DE PROGRESSION  ---
progress = (st.session_state.step - 1) / 4
if st.session_state.step < 5:
    st.progress(progress)

# --- TITRE ---
st.title("Vu que tu es une grande joueuse !")
if st.session_state.step < 5:
    st.write(f"Niveau {st.session_state.step}/4 avant de débloquer la question finale...")

# ---------------------------------------------------------
# ÉTAPE 1 : LA BOUGIE
# ---------------------------------------------------------
if st.session_state.step == 1:
    st.subheader("Énigme N°1 ")
    st.info("Je suis grande quand je suis jeune, et petite quand je suis vieille. Qui suis-je ?")
    
    reponse1 = st.text_input("Ta réponse :", key="r1")
    
    if st.button("Valider"):
        if any(x in reponse1.lower() for x in ["bougie", "une bougie", "la bougie"]):
            st.success("Correct ! Ça commence bien.")
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Non... Je fonds souvent. Essaie encore !")

# ---------------------------------------------------------
# ÉTAPE 2 : LE SECRET
# ---------------------------------------------------------
elif st.session_state.step == 2:
    st.subheader("Énigme N°2 ")
    st.info("Plus j'ai de gardiens, moins je suis en sécurité. Moins j'en ai, plus je suis caché. Qui suis-je ?")
    
    reponse2 = st.text_input("Ta réponse :", key="r2")
    
    if st.button("Valider"):
        if any(x in reponse2.lower() for x in ["secret", "un secret", "le secret"]):
            st.success("Pas mal mais ce n'est pas la fin de ta peine !")
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("Ce n'est pas ça mais je pense que tu es capable d'en garder.")

# ---------------------------------------------------------
# ÉTAPE 3 : VOLTAIRE (LE CHIEN)
# ---------------------------------------------------------
elif st.session_state.step == 3:
    st.subheader("Énigme N°3 🐾")
    # Référence au philosophe + couleur (suisse blanc) + bêtises
    st.info("""
    Je porte le nom d'un célèbre philosophe des Lumières.
    Mon manteau est blanc comme la neige, mais mes pattes laissent parfois des traces de bêtises...
    Qui suis-je ?
    """)
    
    reponse3 = st.text_input("Ta réponse :", key="r3")
    
    if st.button("Valider"):
        # On accepte "Voltaire", "voltaire", "mon chien"
        mots_cles_voltaire = ["voltaire", " mon chien", "Voltaire", "berger suisse"]
        if any(x in reponse3.lower() for x in mots_cles_voltaire):
            st.success("Wouf ! C'est la bonne réponse 🐶")
            st.balloons() # Des ballons pour Voltaire !
            st.session_state.step = 4
            st.rerun()
        else:
            st.error("Indice : Je suis très mignon, suisse et blanc.")

# ---------------------------------------------------------
# ÉTAPE 4 : LE DROIT (BUSINESS)
# ---------------------------------------------------------
elif st.session_state.step == 4:
    st.subheader("Énigme N°4 ")
    # Référence aux codes, contrats et entreprises
    st.info("""
    Je suis le berceau de l'art oratoire.
    Avec moi tout fonctionne mais sans moi tout s'écroule 
    J'ai la faculté de te faire chouiner
    Quel est ce domaine ?
    """)
    
    reponse4 = st.text_input("Ta réponse :", key="r4")
    
    if st.button("Valider"):
        mots_cles_droit = ["droit", "law", "avocat", "juriste", "affaire"]
        if any(x in reponse4.lower() for x in mots_cles_droit):
            st.success("je n'en attendais pas moins! Bravo.")
            st.session_state.step = 5
            st.rerun()
        else:
            st.error("Indice : Dalloz est trop présent.")

# ---------------------------------------------------------
# ÉTAPE 5 : LE CALENDRIER FINAL
# ---------------------------------------------------------
elif st.session_state.step == 5:
    st.markdown("---")
    st.header("✨ Félicitations !")
    
    st.write("Tu as résolu toutes les énigmes (et Voltaire est fier de toi).")
    st.write("Dis-moi quand es tu disponible ^^ ?")
    
    # Création de la liste des dates du 14 au 27 février
    dates_dispo = [f"{i} Février" for i in range(14, 28)]
    
    choix = st.multiselect(
        "Sélectionne tes dates possibles ici :",
        dates_dispo
    )
    
    if choix:
        st.success(f"Noté pour : {', '.join(choix)} !")
        
        # --- CONFIGURATION EMAIL ---
        mon_email = "hbardonnaut@gmail.com"  # <--- METS TON EMAIL ICI
        sujet = "Disponibilités Février "
        corps = f"Diantre ! J'ai réussi le quiz. Je suis dispo les : {', '.join(choix)}. A très vite !"
        
        mailto_link = f"mailto:{mon_email}?subject={sujet}&body={corps}"
        
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{mailto_link}" target="_blank" style="
                text-decoration:none; 
                background-color:#FF4B4B; 
                color:white; 
                padding:12px 25px; 
                border-radius:25px; 
                font-size: 18px;
                font-weight:bold;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                Envoyer ma réponse
            </a>
        </div>
        """, unsafe_allow_html=True)