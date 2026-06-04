import streamlit as st

# Configuración de página para ocultar elementos nativos y usar todo el ancho
st.set_page_config(page_title="Repaso General", layout="wide")

# CSS para ocultar el menú de Streamlit, centrar títulos y hacer fuentes grandes
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .title-text {
        font-size: 60px !important;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle-text {
        font-size: 35px !important;
        text-align: center;
        color: #555555;
        margin-bottom: 40px;
    }
    .content-text {
        font-size: 30px !important;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Lógica de navegación simulando diapositivas
if 'slide' not in st.session_state:
    st.session_state.slide = 0

def next_slide():
    if st.session_state.slide < 4:
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1

# --- DIAPOSITIVAS ---

if st.session_state.slide == 0:
    st.markdown('<p class="title-text">Desarrollo Web e Integración de Sistemas</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Repaso General para 3er Año</p>', unsafe_allow_html=True)

elif st.session_state.slide == 1:
    st.markdown('<p class="title-text">Tipos de Datos en Python</p>', unsafe_allow_html=True)
    st.markdown('<p class="content-text">En programación, cada dato tiene un tipo específico que define cómo se comporta dentro del sistema.</p>', unsafe_allow_html=True)
    
    st.code('''
# Enteros (int)
type(10)      
    
# Decimales (float)
type(3.5)     

# Texto (str)
type("Hola")  

# Booleanos (bool)
type(True)    
    ''', language='python')

elif st.session_state.slide == 2:
    st.markdown('<p class="title-text">Variables en Python</p>', unsafe_allow_html=True)
    st.markdown('<p class="content-text">Son espacios donde guardamos nuestra información para poder usarla y modificarla después.</p>', unsafe_allow_html=True)
    
    st.code('''
nombre = "Juan"
edad = 15
altura = 1.70

print(nombre)
    ''', language='python')

elif st.session_state.slide == 3:
    st.markdown('<p class="title-text">HTML5: El Esqueleto</p>', unsafe_allow_html=True)
    st.markdown('<p class="content-text">Define la estructura y los elementos que componen nuestra página web.</p>', unsafe_allow_html=True)
    
    st.code('''
<h1>Título Principal</h1>

<p>Esto es un párrafo de texto en la web.</p>

<img src="foto.jpg">
    ''', language='html')

elif st.session_state.slide == 4:
    st.markdown('<p class="title-text">CSS: La Estética</p>', unsafe_allow_html=True)
    st.markdown('<p class="content-text">Se encarga de los colores, los tamaños y la distribución visual de los elementos.</p>', unsafe_allow_html=True)
    
    st.code('''
h1 {
    color: blue;
    background-color: black;
}
    ''', language='css')

# --- CONTROLES DE NAVEGACIÓN ---
st.markdown("---")
col1, col2, col3 = st.columns([1, 8, 1])

with col1:
    if st.session_state.slide > 0:
        st.button("Anterior", on_click=prev_slide)
        
with col3:
    if st.session_state.slide < 4:
        st.button("Siguiente", on_click=next_slide)
        
