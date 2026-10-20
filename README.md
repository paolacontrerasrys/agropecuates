# AgroCebada · Agropecuates — tablero para Streamlit

Plataforma de resultados del equipo **Agropecuates** para el Reto AgroCebada
FIRA 2026: predicciones de las 59 parcelas, mapa con simulador climático,
comparación y validación del modelo, calculadora de inclusión financiera,
informe y descargas.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `app.py` | La aplicación de Streamlit. Muestra el sitio a pantalla completa |
| `requirements.txt` | Lo único que Streamlit tiene que instalar: `streamlit` |
| `sitio/` | El sitio ya compilado: páginas, datos, modelo del simulador y documentos |
| `README.md` | Este archivo |

Todo el cálculo —mapa, gráficas, simulador y calculadora— ocurre en el
navegador de quien abre el tablero. Streamlit sólo entrega los archivos, así que
no hace falta ninguna otra librería de Python.

## Cómo publicarlo en GitHub y Streamlit

1. En el repositorio de GitHub que usa Streamlit, **borra el contenido
   anterior** para que no queden archivos viejos mezclados. Funcionaría igual
   aunque se quedaran, pero así el repositorio queda limpio.
2. Sube **el contenido de esta carpeta tal cual**: `app.py`, `requirements.txt`
   y `README.md` en la raíz, y la carpeta `sitio/` completa, con todas sus
   subcarpetas. En la web de GitHub basta con arrastrarlos a «Add file → Upload
   files». Son menos de 100 archivos, que es el límite de cada subida.
3. Haz *commit* en la rama principal (`main`). Streamlit Community Cloud
   detecta el cambio y vuelve a desplegar solo en uno o dos minutos.
4. En share.streamlit.io comprueba que la app apunta a esa rama y a `app.py`
   como archivo principal. Si ya apuntaba a `app.py`, no hay que tocar nada.
5. Abre el enlace en una ventana de incógnito y recorre las secciones.

**Antes de presentarlo al jurado:** las apps gratuitas de Streamlit se duermen
cuando nadie las visita en un tiempo y muestran un botón para despertarlas.
Ábrela un rato antes para que esté despierta.

## Probarlo en tu computadora

```
pip install -r requirements.txt
streamlit run app.py
```

Se abre en http://localhost:8501.

## No editar `sitio/` a mano

`sitio/` es la versión compilada del sitio, no su código fuente: los archivos
de `sitio/assets/` están minificados y cambiarlos a mano rompe el tablero. Los
cambios se hacen en el proyecto de la plataforma y se vuelve a generar esta
carpeta.
