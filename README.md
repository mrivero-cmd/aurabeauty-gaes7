# AURABEAUTY — portal corporativo y de investigación

Proyecto académico con:
- Python + Flask para servir la página y recibir el formulario.
- HTML semántico.
- CSS propio y diseño responsive.
- Bootstrap 5.3 para navegación, cuadrícula, formularios y acordeón.
- C++ como programa complementario de consola para calcular indicadores de encuesta.
- Estadísticas compartidas por el equipo y transcripciones editadas de las entrevistas.

## Requisitos
- Python 3.10 o superior
- Conexión a internet para cargar Bootstrap CDN, Google Fonts, imágenes externas y mapa.

## Ejecutar en Windows
1. Descomprime `aurasoft_portal.zip`.
2. Abre la carpeta en Visual Studio Code.
3. Abre la terminal en esa carpeta.
4. Ejecuta:

```bash
py -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
py app.py
```

5. En el navegador abre `http://127.0.0.1:5000`.

En algunos equipos, si `py` no funciona, usa `python` en lugar de `py`.

## Ejecutar el archivo C++
El archivo `cpp/analisis_encuesta.cpp` es complementario y corre por separado. Si tienes un compilador g++:

```bash
g++ cpp/analisis_encuesta.cpp -o analisis_encuesta
./analisis_encuesta
```

En Windows, el ejecutable puede ser `analisis_encuesta.exe`.

## Importante antes de publicar
- Cambia la clave secreta de Flask y desactiva `debug=True` en producción.
- El formulario guarda mensajes en `contactos.csv` localmente. No lo publiques con datos reales sin definir controles de seguridad, acceso, retención y tratamiento de datos.
- La dirección física de AURABEAUTY no fue proporcionada; el mapa es solo una referencia de Mosquera.
- Los enlaces a documentos de investigación están pendientes de conectar a los archivos reales.
- Añade las bitácoras de observación y fotografías autorizadas; la guía académica las solicita.
- Confirma la identidad/cargo exactos del entrevistado de Bella Piel, porque la transcripción de audio fue aproximada.
- Las imágenes son enlaces externos ilustrativos y pueden necesitar reemplazo por imágenes autorizadas del proyecto.
- Las estadísticas se copiaron de las capturas compartidas y deben contrastarse con el CSV completo antes de su entrega definitiva.
- La misión, visión, valores y explicación del logo son propuestas de redacción que debe aprobar el equipo.
- El sitio no implementa todavía recomendaciones reales de IA, catálogo comercial ni pagos.


## Imágenes del equipo
Las imágenes aportadas por GAES 7 se guardan en `static/images/` y se muestran en la portada y la galería. Los referentes de interfaces se presentan como inspiración visual, no como funcionalidades implementadas.
