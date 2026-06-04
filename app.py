import streamlit as st

# Configuración de página para usar todo el ancho de la pantalla
st.set_page_config(page_title="Repaso General", layout="wide")

# Estilo personalizado para agrandar fuentes y simular una presentación
st.markdown("""
    <style>
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #1E88E5;
    }
    .medium-font {
        font-size: 30px !important;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Menú lateral para navegar como si fueran diapositivas
st.sidebar.title("Navegación")
diapositiva = st.sidebar.radio("Ir a:", [
    "1. Inicio", 
    "2. Python: Tipos de Datos", 
    "3. Python: Variables", 
    "4. Web: HTML5", 
    "5. Web: CSS"
])

# --- DIAPOSITIVA 1 ---
if diapositiva == "1. Inicio":
    st.markdown('<p class="big-font">Desarrollo Web e Integración de Sistemas</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p class="medium-font">Repaso General: Python, HTML5 y CSS</p>', unsafe_allow_html=True)

# --- DIAPOSITIVA 2 ---
elif diapositiva == "2. Python: Tipos de Datos":
    st.markdown('<p class="big-font">Python: ¿Qué es type?</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p class="medium-font">En programación, cada dato tiene un "tipo[span_0](start_span)"[span_0](end_span).</p>', unsafe_allow_html=True)
    
    st.code('''
# Números enteros
type(10)      # int 
    
# Números con coma
type(3.5)     # float 

# Texto
type("Hola")  # str 

# Verdadero o falso
type(True)    # bool 
    ''', language='python')

# --- DIAPOSITIVA 3 ---
elif diapositiva == "3. Python: Variables":
    st.markdown('<p class="big-font">Python: Variables</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p class="medium-font">Las usamos para guardar información.</p>', unsafe_allow_html=True)
    
    st.code('''
nombre = "Juan"
edad = 15
altura = 1.70

print(nombre)
    ''', language='python')

# --- DIAPOSITIVA 4 ---
elif diapositiva == "4. Web: HTML5":
    st.markdown('<p class="big-font">HTML5: El Esqueleto</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p class="medium-font">Define la estructura de nuestra página web.</p>', unsafe_allow_html=True)
    
    st.code('''
<h1>Título de la página</h1>

<p>Esto es un párrafo normal.</p>

<img src="foto.jpg">
    ''', language='html')

# --- DIAPOSITIVA 5 ---
elif diapositiva == "5. Web: CSS":
    st.markdown('<p class="big-font">CSS: El Estilo</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<p class="medium-font">Se encarga de la estética y los colores.</p>', unsafe_allow_html=True)
    
    st.code('''
h1 {
    color: blue;
    background-color: black;
}
    ''', language='css')
  
