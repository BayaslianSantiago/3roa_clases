import streamlit as st

# Configuración de página
st.set_page_config(page_title="Repaso General", layout="wide", initial_sidebar_state="collapsed")

# CSS para modo oscuro, ocultar elementos y dar formato a la presentación
st.markdown("""
    <style>
    /* Forzar modo oscuro en el fondo y texto base */
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .title-text {
        font-size: 55px !important;
        font-weight: bold;
        color: #4DB8FF; /* Azul claro adaptado a modo oscuro */
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle-text {
        font-size: 30px !important;
        text-align: center;
        color: #A0A0A0;
        margin-bottom: 40px;
    }
    .content-text {
        font-size: 26px !important;
        margin-bottom: 20px;
        color: #E0E0E0;
    }
    /* Estilo para los cuadros de conceptos clave */
    .concept-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 8px;
        border-left: 6px solid #4DB8FF;
        margin-bottom: 25px;
        font-size: 22px;
        color: #CCCCCC;
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
    
    st.markdown('''
    <div class="concept-box">
        <strong>Concepto Clave:</strong> La función <code>type</code> sirve para saber qué tipo de dato tiene una variable[span_0](start_span)[span_0](end_span).<br><br>
        En programación, cada dato tiene un "tipo[span_1](start_span)"[span_1](end_span):<br>
        • <strong>int:</strong> números enteros[span_2](start_span)[span_2](end_span).<br>
        • <strong>float:</strong> números con coma[span_3](start_span)[span_3](end_span).<br>
        • <strong>str:</strong> texto[span_4](start_span)[span_4](end_span).<br>
        • <strong>bool:</strong> verdadero o falso[span_5](start_span)[span_5](end_span).
    </div>
    ''', unsafe_allow_html=True)
    
    st.code('''
# Ejemplos de verificación de tipos
print(type(10))      # int 
print(type(3.5))     # float 
print(type("Hola"))  # str 
print(type(True))    # bool 
    ''', language='python')

elif st.session_state.slide == 2:
    st.markdown('<p class="title-text">Variables en Python</p>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="concept-box">
        <strong>Concepto Clave:</strong> Una variable es un espacio en la memoria de la computadora donde guardamos un dato para usarlo más adelante. Sirve para entender qué estamos guardando y evitar errores al operar con esos datos[span_6](start_span)[span_6](end_span).
    </div>
    ''', unsafe_allow_html=True)
    
    st.code('''
# Declaración y asignación de variables
nombre = "Juan"
edad = 15
altura = 1.70

print(nombre)
    ''', language='python')

elif st.session_state.slide == 3:
    st.markdown('<p class="title-text">HTML5: Estructura</p>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="concept-box">
        <strong>Concepto Clave:</strong> HTML (Lenguaje de Marcado de Hipertexto) no es un lenguaje de programación, sino de <strong>marcado</strong>. Utiliza <strong>etiquetas</strong> para definir la estructura de la página (títulos, párrafos, imágenes).
    </div>
    ''', unsafe_allow_html=True)
    
    st.code('''
<!-- Etiqueta de título principal -->
<h1>Bienvenidos a mi Portfolio</h1>

<!-- Etiqueta de párrafo -->
<p>Este es mi primer proyecto web.</p>

<!-- Etiqueta de imagen con atributo de origen -->
<img src="foto.jpg">
    ''', language='html')

elif st.session_state.slide == 4:
    st.markdown('<p class="title-text">CSS: Estética</p>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="concept-box">
        <strong>Concepto Clave:</strong> CSS (Hojas de Estilo en Cascada) se separa del HTML para controlar la presentación visual. Utiliza <strong>selectores</strong> para apuntar a elementos HTML y <strong>propiedades</strong> para cambiar su aspecto.
    </div>
    ''', unsafe_allow_html=True)
    
    st.code('''
/* El selector apunta a la etiqueta h1 del HTML */
h1 {
    color: #4DB8FF;              /* Propiedad de color de texto */
    background-color: #1E1E1E;   /* Propiedad de color de fondo */
    text-align: center;          /* Alineación del texto */
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
        
