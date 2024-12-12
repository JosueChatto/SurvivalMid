# SurvivalMid
Juego Para la especialidad
---

# Proyecto de Videojuego - Supervivencia Mental
Supervivencia Mental es un juego educativo diseñado para poner a prueba los conocimientos generales de los jugadores con preguntas de cultura general. Es una herramienta divertida para mejorar habilidades cognitivas.

## Descripción general del repositorio

Este repositorio contiene el código fuente de un videojuego educativo llamado **Supervivencia Mental**, el cual está diseñado para poner a prueba los conocimientos generales de los jugadores a través de una serie de preguntas de cultura general. El juego permite a los jugadores elegir un nivel de dificultad (fácil, intermedio y difícil), y ofrece un sistema de puntuación y tiempos que se ajustan según el rendimiento de los jugadores. El objetivo es ayudar a los usuarios a mejorar sus habilidades cognitivas mientras se divierten.

## Propósito dentro del proyecto global

El propósito de este repositorio es ofrecer la implementación del juego **Supervivencia Mental**, que es parte de un proyecto educativo más grande. Este juego tiene como objetivo promover el aprendizaje de una forma interactiva y divertida, permitiendo a los usuarios desafiarse a sí mismos con preguntas de cultura general mientras gestionan un cronómetro y su número de intentos. Este código implementa las mecánicas del juego, desde la lógica de preguntas hasta la interacción con la interfaz.

## Instrucciones de instalación, configuración y ejecución

### Instalación

Para ejecutar este proyecto en tu máquina local, debes asegurarte de que tienes instalados los siguientes requisitos previos:

1. **Python 3.x** (recomendado: 3.7 o superior)
2. **Kivy** (para la interfaz gráfica)
   - Si no tienes Kivy instalado, puedes instalarlo ejecutando:
     ```bash
     pip install kivy
     ```

### Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/JosueChatto/SurvivalMid.git
   ```

2. Accede al directorio del proyecto:
   ```bash
   cd SurvivalMid
   ```

3. Si estás utilizando un entorno virtual (recomendado), crea uno y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En sistemas Unix/macOS
   .\venv\Scripts\activate    # En Windows
   ```


### Ejecución

1. Una vez que el entorno esté configurado, ejecuta el siguiente comando para iniciar el juego:
   ```bash
   python main.py
   ```

2. El juego se iniciará, permitiéndote seleccionar el nivel de dificultad y comenzando a responder las preguntas.

## Dependencias

El proyecto depende de las siguientes herramientas y librerías:

- **Kivy** (versión 2.1.0 o superior) - Usado para la creación de la interfaz gráfica.
- **Python 3.x** (recomendado: 3.7 o superior) - Lenguaje de programación principal utilizado.

Para instalar las dependencias necesarias, asegúrate de seguir las instrucciones de instalación proporcionadas en la sección anterior.

## Estructura del repositorio

El código está organizado de la siguiente manera:

```
/SurvivalMid
|-- main.py                 # Archivo principal para ejecutar el juego
|-- correct_answer.csv      # Archivos con preguntas y respuestas
|-- questions.csv           # Archivos con preguntas y respuestas
|-- wrong_answer.csv        # Archivos con preguntas y respuestas
|-- correct_aswer.wav       # Archivos de los recursos como imágenes o sonidos 
|-- wrong_answer.wav        # Archivos de los recursos como imágenes o sonidos 
|-- PuzzleGame.wav          # Archivos de los recursos como imágenes o sonidos 
|-- iconCerb.png            # Archivos de los recursos como imágenes o sonidos 
|-- README.md               # Este archivo de documentación
```

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

---
