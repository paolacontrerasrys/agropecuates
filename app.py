"""Tablero AgroCebada 2026 · equipo Agropecuates — el sitio completo dentro de Streamlit.

    streamlit run app.py

Streamlit no ejecuta aquí ningún cálculo. El sitio es una aplicación web
estática (sitio/, la compilación de la plataforma) y todo corre en el
navegador: mapa, tablas, gráficas, simulador y calculadora de crédito.
Streamlit sólo la sirve, como componente personalizado, y la muestra a
pantalla completa.

Por qué un componente y no `components.html` ni los archivos estáticos de la
app: un componente es la única vía por la que Streamlit sirve una carpeta
entera —código, estilos, fuentes, datos, PDF y Word— cada archivo con su tipo
correcto, dentro de un marco que permite ejecutar código, descargar, abrir
pestañas e imprimir.

Para actualizar sitio/ después de cambiar la plataforma:
    npm run streamlit        (en la raíz del proyecto de la plataforma)
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AgroCebada · Agropecuates",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# El sitio trae su propia cabecera, su menú y su pie: se retira todo el marco de
# Streamlit para que la página sea sólo el sitio. El alto del componente lo
# fija el propio sitio al de la ventana (src/lib/streamlit.ts), así que aquí
# además se quita el desplazamiento exterior para que no haya dos barras.
st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], footer { display: none !important; }
      /* Fondo blanco mientras carga el sitio, aunque el navegador esté en modo
         oscuro: así no hace falta .streamlit/config.toml, una carpeta oculta que
         el Finder no muestra y que es fácil dejar fuera al subir a GitHub. */
      .stApp, [data-testid="stAppViewContainer"] { background: #ffffff !important; }
      [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"], [data-testid="stMain"] { overflow: hidden !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

sitio = components.declare_component("sitio", path=str(Path(__file__).parent / "sitio"))
sitio(key="sitio", default=None)
