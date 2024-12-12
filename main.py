#Copyright (c) 2024 Josue Sebastian Cardenas Orozco
#Licensed under the MIT License. See LICENSE file in the project root for full license information.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
import random 
from kivy.uix.popup import Popup
from kivy.core.window import Window
# Establecer el tamaño de la ventana
Window.size = (960, 1700)

# Establecer el título de la ventana
Window.title = "Supervivencia Mental"

# Establecer el color de fondo de la ventana
Window.clearcolor = (0.02, 0.08, 0.15, 1)  # Azul oscuro
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        title = Label(
            text="Supervivencia Mental",
            font_size=50,
            bold=True,
            size_hint=(None, None),
            size=(600, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(title)

        play_button = Button(
            text="¡JUGAR!",
            font_size=80,
            size_hint=(None, None),
            size=(300, 175),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.1, 0.7, 0.1, 1)  # Verde
            
        )
        play_button.bind(on_press=self.start_game)
        layout.add_widget(play_button)

        config_button = Button(
            text="Configurar",
            font_size=50,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            background_color=(0.1, 0.5, 0.9, 1)  # Azul
        )
        config_button.bind(on_press=self.go_to_config)
        layout.add_widget(config_button)

        exit_button = Button(
            text="Salir",
            font_size=50,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.9, 0.1, 0.1, 1)  # Rojo
        )
        exit_button.bind(on_press=self.exit_app)
        layout.add_widget(exit_button)

        with layout.canvas.before:
            Color(0.02, 0.08, 0.15, 1)  # Fondo azul oscuro #021526
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[0])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.add_widget(layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def start_game(self, instance):
        self.manager.current = 'difficulty'

    def go_to_config(self, instance):
        self.manager.current = 'config'

    def exit_app(self, instance):
        App.get_running_app().stop()

class DifficultyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        title = Label(
            text="Selecciona la Dificultad",
            bold=True,
            font_size=84,
            size_hint=(None, None),
            size=(500, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(title)

        easy_button = Button(
            text="Fácil",
            font_size=40,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.1, 0.7, 0.1, 1)  # Verde
        )
        easy_button.bind(on_press=self.start_game_easy)
        layout.add_widget(easy_button)

        medium_button = Button(
            text="Medio",
            font_size=40,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            background_color=(0.1, 0.5, 0.9, 1)  # Azul
        )
        medium_button.bind(on_press=self.start_game_medium)
        layout.add_widget(medium_button)

        hard_button = Button(
            text="Difícil",
            font_size=40,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.9, 0.1, 0.1, 1)  # Rojo
        )
        hard_button.bind(on_press=self.start_game_hard)
        layout.add_widget(hard_button)

        # Botón para regresar al menú principal
        back_button = Button(
            text="Volver",
            font_size=40,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            background_color=(0.9, 0.7, 0.1, 1)  # Amarillo
        )
        back_button.bind(on_press=self.go_back_to_main_menu)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.02, 0.08, 0.15, 1)  # Fondo azul oscuro #021526
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[0])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)
            self.add_widget(layout)
    
    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def start_game_easy(self, instance=None):
        other_arg_value = 'facil'
        self.manager.current = 'game'
        self.manager.get_screen('game').set_difficulty(40, other_arg_value)

    def start_game_medium(self, instance=None):
        other_arg_value = 'medio' 
        self.manager.current = 'game'
        self.manager.get_screen('game').set_difficulty(30, other_arg_value)

    def start_game_hard(self, instance=None):
        other_arg_value = 'dificil'
        self.manager.current = 'game'
        self.manager.get_screen('game').set_difficulty(20, other_arg_value)

    def go_back_to_main_menu(self, instance=None):
        self.manager.current = 'main'
        # Implementation for going back to the main menu
        pass

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound_correct = SoundLoader.load('correct_answer.wav')
        self.sound_wrong = SoundLoader.load('wrong_answer.wav')
        self.sontrack = SoundLoader.load('PuzzleGame.wav')  #Aqui ira la musica de juego
        self.questions = []
        self.answers = []
        self.wrong_answers = []
        self.is_paused = False
        self.correct_answers = []   
        self.wrong_answers = []
        self.time_left = 0
        self.attempts = 0
        self.max_attempts = 5
        self.current_question_index = 0 
        self.remaining_time = 0  # Almacena el tiempo restante del jugador
        self.difficulty = None  # Almacena la dificultad actual 
        self.time_increment = 0  # Incremento de tiempo al acertarz
        self.timer_bar = ProgressBar()
        self.build_game_screen()
        self.initial_time = 0  # Tiempo inicial según la dificultad

    def build_game_screen(self):
        layout = FloatLayout()

        if self.timer_bar.parent:
            self.timer_bar.parent.remove_widget(self.timer_bar)
        layout.add_widget(self.timer_bar)

        with layout.canvas.before:
            Color(0.02, 0.08, 0.15, 1)
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[0])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.question_label = Label(
            text="Pregunta aquí",
            bold=True,
            font_size=42,
            size_hint=(None, None),
            size=(600, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.question_label.text_size = (400, None)
        layout.add_widget(self.question_label)

        self.attempts_label = Label(
            text=f"Intentos restantes: {self.max_attempts}",
            font_size=34,
            size_hint=(None, None),
            size=(300, 150),
            pos_hint={'center_x': 0.8, 'center_y': 0.9},  # Posición ajustada
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(self.attempts_label)  # Agrega el Label al layout

        # Botones de respuesta
        button_layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(None, None),
            size=(700, 250),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.answer_button1 = self.create_button("Respuesta 1")
        self.answer_button2 = self.create_button("Respuesta 2")
        self.answer_button3 = self.create_button("Respuesta 3")

        button_layout.add_widget(self.answer_button1)
        button_layout.add_widget(self.answer_button2)
        button_layout.add_widget(self.answer_button3)

        layout.add_widget(button_layout)

        # Botón de Stop
        self.stop_button = Button(
            text="Stop",
            font_size=44,
            size_hint=(None, None),
            size=(250, 150),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            background_normal='',
            background_color=(1, 0, 0, 1)
        )
        self.stop_button.bind(on_press=self.show_pause_popup)
        layout.add_widget(self.stop_button)

        with self.timer_bar.canvas.before:
            self.bar_color = Color(0.02, 0.08, 0.15, 1)  # Azul inicial
            self.bar_rect = RoundedRectangle(size=self.timer_bar.size, pos=self.timer_bar.pos)
            self.timer_bar.bind(pos=self._update_bar_rect, size=self._update_bar_rect)
        self.add_widget(layout)

    def update_attempts(self):
        """Actualiza el texto del label de intentos restantes."""
        self.attempts_label.text = f"Intentos restantes: {self.max_attempts - self.attempts}"

    def pause_game(self):
        if not self.is_paused:
            Clock.unschedule(self.update_time)  # Detener el temporizador
            self.is_paused = True
    
    def resume_game(self):
        if self.is_paused:
            Clock.schedule_interval(self.update_time, 1)  # Reiniciar el temporizador
            self.is_paused = False
    
    def show_pause_popup(self, instance):
        self.pause_game()  # Pausar el juego cuando se abre el popup
        content = FloatLayout()  # Cambiar a FloatLayout para centrar los botones

        # Botón de reanudar
        resume_button = Button(
            text="Reanudar",
            size_hint=(None, None),
            size=(300, 140),
            background_color=(0.1, 0.5, 0.9, 1),
            font_size=20
        )
        resume_button.bind(on_press=self.close_pause_popup)
        
        # Botón de regresar al menú
        menu_button = Button(
            text="Volver a Menú",
            font_size=20,
            size_hint=(None, None),
            size=(300, 140),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.9, 0.7, 0.1, 1)  # Amarillo
        )
        menu_button.bind(on_press=self.close_pause_popup)
        menu_button.bind(on_press=self.go_to_main)
        #layout.add_widget(menu_button)

        # Posicionar los botones en el centro de la pantalla
        content.add_widget(resume_button)
        content.add_widget(menu_button)
        
        # Posicionar los botones en el layout (ajustar las coordenadas según sea necesario)
        resume_button.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        menu_button.pos_hint = {'center_x': 0.5, 'center_y': 0.4}

        # Inicializa el Popup antes de abrirlo
        self.pause_popup = Popup(
            title='Juego Pausado',
            content=content,
            size_hint=(0.5, 0.5),
            size=(550, 300),
            auto_dismiss=False,
            separator_color=(0.1, 0.5, 0.9, 1),
            background_color=(0.02, 0.08, 0.15, 1),
            separator_height=2,
            title_color=(1, 1, 1, 1),
            title_size=24,
        )
        self.pause_popup.open() 

    def reset_attempts(self):
        self.attempts = 0 # Reiniciar el contador de intentos
        

    def close_pause_popup(self, instance,*args):
        if self.pause_popup:  # Asegúrate de que el popup exista
            self.pause_popup.dismiss()  # Cierra el popup
            self.resume_game()  # Reanuda el juego

    def _update_bar_rect(self, instance, value):
            self.bar_rect.pos = instance.pos
            self.bar_rect.size = instance.size

    def _update_bg_rect(self, instance, value):
            self.bg_rect.pos = instance.pos
            self.bg_rect.size = instance.size

    def create_button(self, text):
            button = Button(
                text=text,
                font_size=24,
                size_hint=(None, None),
                size=(300, 150),
                text_size=(200, None),  # Esto permitirá que el texto se ajuste dentro del botón
                halign='center',  # Centra horizontalmente
                valign='middle',  # Centra verticalmente
                background_normal='',
                background_color=(0.1, 0.5, 0.9, 1)  # Azul
            )
            button.bind(on_press=self.check_answer)
            return button

    def load_questions_and_answers(self, difficulty):
        # Definir la ruta base y la carpeta según la dificultad seleccionada
        base_path = f'{difficulty}'

        # Archivos basados en la dificultad
        question_file = f"{base_path}_questions.csv"
        correct_file = f"{base_path}_correct_answers.csv"
        wrong_file = f"{base_path}_wrong_answers.csv"

        # Leer las preguntas, respuestas correctas e incorrectas
        with open(question_file, 'r', encoding='utf-8') as file:
            self.questions = [line.strip() for line in file.readlines()]

        with open(correct_file, 'r', encoding='utf-8') as file:
            self.correct_answers = [line.strip() for line in file.readlines()]

        with open(wrong_file, 'r', encoding='utf-8') as file:
            self.wrong_answers = [line.strip().split(',') for line in file.readlines()]

        # Verificar que el número de preguntas y respuestas coincidan
        if len(self.questions) != len(self.correct_answers) or len(self.questions) != len(self.wrong_answers):
            raise ValueError("El número de preguntas no coincide con el número de respuestas.")

        # Mezclar las preguntas y respuestas manteniendo la correspondencia entre ellas
        question_data = list(zip(self.questions, self.correct_answers, self.wrong_answers))
        
        # Mezclar todo el conjunto de preguntas y respuestas
        random.shuffle(question_data)  # Aleatoriedad de las preguntas

        # Desempaquetar de nuevo en las listas originales, pero ya aleatorias
        self.questions, self.correct_answers, self.wrong_answers = zip(*question_data)

        # Iniciar mostrando la primera pregunta aleatoria
        self.load_question(0)

    def load_question(self, index):
        self.current_question_index = index
        self.question_label.text = self.questions[index]

        correct_answer = self.correct_answers[index]
        wrong_answers = self.wrong_answers[index]

        # Combinar respuestas correctas e incorrectas
        all_answers = wrong_answers + [correct_answer]
        random.shuffle(all_answers)  # Aleatoriedad de las respuestas

        # Asignar las respuestas aleatorias a los botones
        self.answer_button1.text = all_answers[0]
        self.answer_button2.text = all_answers[1]
        self.answer_button3.text = all_answers[2]

    def check_answer(self, instance):
        correct_answer = self.correct_answers[self.current_question_index]
        
        if instance.text == correct_answer:
            self.question_label.text = "¡Correcto!"
            if self.sound_correct:
                self.sound_correct.play()

            # Ajustar el tiempo añadido según la dificultad
            if self.difficulty == 'facil':
                self.time_left = min(self.time_left + 2, self.initial_time)
            elif self.difficulty == 'medio':
                self.time_left = min(self.time_left + 3, self.initial_time)
            elif self.difficulty == 'dificil':
                self.time_left = min(self.time_left + 4, self.initial_time)
            
            self.timer_bar.value = self.time_left
            
            if self.current_question_index + 1 < len(self.questions):
                self.load_question(self.current_question_index + 1)
            else:
                self.show_game_over_popup()
        
        else:
            self.attempts += 1
            
            # Ajustar el tiempo restado según la dificultad
            if self.difficulty == 'facil':
                self.time_left = max(self.time_left - 4, 0)
            elif self.difficulty == 'medio':
                self.time_left = max(self.time_left - 3, 0)
            elif self.difficulty == 'dificil':
                self.time_left = max(self.time_left - 2, 0)
            
            self.timer_bar.value = self.time_left
            
            if self.attempts >= self.max_attempts:
                self.question_label.text = "¡Has fallado los intentos!"
                Clock.unschedule(self.update_time)  # Detener el temporizador
                self.show_game_over_popup()
            else:
                self.attempts_label.text = f"Intentos restantes: {self.max_attempts - self.attempts}"
                self.question_label.text = "¡Incorrecto!"
                if self.sound_wrong:
                    self.sound_wrong.play()
    
    def update_time(self, dt):
        self.time_left -= 1
        if self.time_left <= 5:
            self.bar_color.rgb = (0.9, 0.1, 0.1)  # Rojo
        else:
            self.bar_color.rgb = (0.02, 0.08, 0.15)  # Azul oscuro
        
        self.timer_bar.value = max(0, self.time_left)  # Asegurarse que no sea menor a 0

        # Verificamos si el tiempo ha terminado
        if self.time_left <= 0:
            Clock.unschedule(self.update_time)  # Detenemos el temporizador
            self.show_game_over_popup()  # Mostramos el popup de fin del juego

    def set_difficulty(self, time_limit, difficulty):
        self.load_questions_and_answers(difficulty)  # Cargar preguntas basadas en la dificultad
        self.initial_time = time_limit  # Establecer el tiempo inicial
        self.time_left = time_limit  # El tiempo restante es igual al tiempo límite
        self.timer_bar.max = time_limit  # Establecer el máximo valor del temporizador
        self.timer_bar.value = time_limit  # Inicializar la barra de progreso con el tiempo restante
        self.difficulty = difficulty  # Establecer la dificultad seleccionada
        
        # Ajustar los intentos máximos según la dificultad
        if difficulty == 'facil':
            self.max_attempts = 5
        elif difficulty == 'medio':
            self.max_attempts = 4
        elif difficulty == 'dificil':
            self.max_attempts = 3  # Valor predeterminado
        Clock.schedule_interval(self.update_time, 1)

    def on_correct_answer(self):
        self.remaining_time += self.time_increment
        # Actualizar el UI o cualquier otro componente visual con el tiempo restante

    # Método llamado cuando el jugador falla una respuesta
    def on_wrong_answer(self):
        self.remaining_time -= self.time_decrement
        self.attempts -= 1

    def show_game_over_popup(self):
        popup = Popup(
            title='Fin del Juego',
            content=Label(text='¡El juego ha terminado!'),
            size_hint=(None, None),
            size=(400, 200)
        )
        self.attempts = 0
        popup.bind(on_dismiss=self.go_to_main_screen)
        popup.open()

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

    def go_to_main(self, instance):
        
        self.reset_attempts()
        self.manager.current = 'main'

class ConfigScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music_enabled = False  # Estado inicial de la música
        layout = FloatLayout()

        title = Label(
            text="Configuración",
            font_size=32,
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(title)

        self.music_button = Button(
            text="Música: Activada",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            background_color=(0.1, 0.5, 0.9, 1)
        )
        self.music_button.bind(on_press=self.toggle_music)
        layout.add_widget(self.music_button)
        
        back_button = Button(
            text="Volver",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.9, 0.7, 0.1, 1)  # Amarillo
        )
        back_button.bind(on_press=self.go_to_main)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.02, 0.08, 0.15, 1)  # Fondo azul oscuro #021526
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[10])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.add_widget(layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def toggle_music(self, instance):
        self.music_enabled = not self.music_enabled
        self.music_button.text = "Música: Desactivada" if self.music_enabled else "Música: Activada"
        if self.music_enabled:
            SoundLoader.load('PuzzleGame.wav').stop()
        else:
            SoundLoader.load('PuzzleGame.wav').play()

    def toggle_sounds(self, instance):
        self.sounds_enabled = not self.sounds_enabled
        self.sounds_button.text = "Sonidos: Activados" if self.sounds_enabled else "Sonidos: Desactivados"

    def go_to_main(self, instance):
        self.manager.current = 'main'

class QuizApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(DifficultyScreen(name='difficulty'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ConfigScreen(name='config'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
