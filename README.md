## 🦜️🔗 LangChain Script

### Descripción
Este script en Python utiliza la biblioteca Streamlit junto con LangChain para crear un flujo de trabajo de procesamiento de lenguaje natural (NLP). El objetivo principal es generar títulos y scripts de videos de YouTube basados en un prompt proporcionado por el usuario. Además, utiliza la API de Wikipedia para incorporar investigación en los scripts.

### Inspiración
Este código se basa en el tutorial del siguiente video de YouTube: [LangChain Tutorial](https://www.youtube.com/watch?v=MlK6SIjcjE8).

### Uso
1. Clona el repositorio.
2. Configura la clave de la API de OpenAI en el archivo `apiKey.py`.
3. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
4. Ejecuta el script con `streamlit run nombre_del_script.py`.
5. Ingresa un prompt en la interfaz de usuario para generar títulos y scripts.

### Componentes Principales
- **Prompt Templates**: Define plantillas para la generación de títulos y scripts.
- **Memory**: Almacena el historial de conversaciones para el tema y el título.
- **Modelo de Lenguaje (LLM)**: Utiliza OpenAI como modelo de lenguaje para la generación de texto.
- **WikipediaAPIWrapper**: Realiza consultas a la API de Wikipedia para obtener información adicional.
- **Interfaz de Usuario (UI)**: Creada con Streamlit para facilitar la interacción del usuario.

### Ejecución
Si se proporciona un prompt, el script generará títulos y scripts, realizará investigaciones en Wikipedia y mostrará los resultados en la interfaz de usuario de Streamlit. Además, se visualiza el historial de conversaciones y la investigación de Wikipedia.

### Contribuciones
¡Contribuciones son bienvenidas! Si encuentras mejoras o sugerencias, por favor, abre un problema o envía una solicitud de extracción.

### Agradecimientos
Agradecimientos al creador del tutorial en YouTube que inspiró este proyecto.

---
