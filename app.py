#Surprise Emilie#

import streamlit as st
import time

# --- Configuration de la page ---
st.set_page_config(page_title="Pour Emilie ", page_icon="🌹")

# --- CSS pour le style (Rose & Romantique) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style des boutons */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #D42B2B;
        transform: scale(1.02);
    }
    
    /* Style du texte */
    h1, h2, h3 {
        color: #333;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Gestion de l'histoire (État) ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- TITRE ---
st.title("Une surprise pour toi... 💌")

# ---------------------------------------------------------
# ÉTAPE 1 : VOLTAIRE DANS LA BIBLIOTHÈQUE
# ---------------------------------------------------------
if st.session_state.step == 1:
    st.write("---")
    st.subheader("1 : La découverte")
    st.write("Fin de journée. Voltaire cherche sa balle...")
    
    st.info("🐶 *Snif snif...* Voltaire a trouvé quelque chose de bizarre coincé sous ton canapé !")
    st.write("Ça ressemble à une petite enveloppe...")
    
    st.write("") # Espace vide
    
    if st.button("Voir ce que c'est ^^"):
        st.session_state.step = 2
        st.rerun()

# ---------------------------------------------------------
# ÉTAPE 2 : LE MESSAGE DOUX
# ---------------------------------------------------------
elif st.session_state.step == 2:
    st.write("---")
    st.subheader("2 : Le message")
    
    st.success("C'est une pensée pour toi ahah")
    
    st.markdown("""
    <div style="text-align: center; font-style: italic; margin-bottom: 20px;">
        "Même la plus brillante des juristes a besoin d'une pause douceur."
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Voltaire remue la queue, il a préparé une dernière surprise avec moi.")
    st.write("Es-tu prête ?")
    
    st.write("")
    
    if st.button("Oui, montre-moi ! 🐾"):
        st.session_state.step = 3
        st.rerun()

# ---------------------------------------------------------
# ÉTAPE 3 : LE JARDIN DE TULIPES (FINALE)
# ---------------------------------------------------------
elif st.session_state.step == 3:
    st.write("---")
    st.subheader("3 : Ton Jardin")
    
    st.write("Comme je ne peux pas être là pour te les offrir en vrai aujourd'hui...")
    st.write("**On a fait pousser ça pour toi (garanti sans bêtises du mimi).**")
    
    # Bouton pour lancer l'animation
    if st.button("Recevoir mes fleurs 🌷"):
        
        # 1. Animation : Ballons
        st.balloons()
        
        # 2. Animation : Texte qui change
        status_text = st.empty()
        status_text.write("🌱 Plantation des graines...")
        time.sleep(1)
        status_text.write("🌧️ Un peu d'eau...")
        time.sleep(1)
        status_text.write("☀️ Un peu de soleil...")
        time.sleep(1)
        status_text.empty()
        
        # 3. Animation : Les fleurs poussent
        jardin_container = st.container()
        fleurs_str = ""
        placeholder = st.empty()
        
        # On fait apparaître 12 tulipes
        for i in range(12):
            fleurs_str += "🌷 "
            # On centre les fleurs avec du Markdown
            placeholder.markdown(f"<h1 style='text-align: center;'>{fleurs_str}</h1>", unsafe_allow_html=True)
            time.sleep(0.4)
            
        # 4. Message Final
        st.markdown("---")
        st.markdown("""
        <div style="background-color: #ffe6e6; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ffcccc;">
            <h2 style="color: #d63384;">Joyeuse Saint-Valentin Émilie ! </h2>
            <p>Passe une bonne soirée !! .</p>
        </div>
        """, unsafe_allow_html=True)
        
        # (Plus de mail ici, ça s'arrête sur le joli message)





