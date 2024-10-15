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
from kivy.core.window import Window
# Establecer el tamaño de la ventana
Window.size = (800, 600)

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
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(title)

        play_button = Button(
            text="¡JUGAR!",
            font_size=40,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.1, 0.7, 0.1, 1)  # Verde
            
        )
        play_button.bind(on_press=self.start_game)
        layout.add_widget(play_button)

        config_button = Button(
            text="Configurar",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            background_color=(0.1, 0.5, 0.9, 1)  # Azul
        )
        config_button.bind(on_press=self.go_to_config)
        layout.add_widget(config_button)

        exit_button = Button(
            text="Salir",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
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
            font_size=32,
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            color=(1, 1, 1, 1)  # Texto blanco
        )
        layout.add_widget(title)

        easy_button = Button(
            text="Fácil",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.1, 0.7, 0.1, 1)  # Verde
        )
        easy_button.bind(on_press=self.start_game_easy)
        layout.add_widget(easy_button)

        medium_button = Button(
            text="Medio",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            background_color=(0.1, 0.5, 0.9, 1)  # Azul
        )
        medium_button.bind(on_press=self.start_game_medium)
        layout.add_widget(medium_button)

        hard_button = Button(
            text="Difícil",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.9, 0.1, 0.1, 1)  # Rojo
        )
        hard_button.bind(on_press=self.start_game_hard)
        layout.add_widget(hard_button)

        # Botón para regresar al menú principal
        back_button = Button(
            text="Volver",
            font_size=24,
            size_hint=(None, None),
            size=(200, 50),
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
        self.manager.get_screen('game').set_difficulty(35, other_arg_value)

    def start_game_medium(self, instance=None):
        other_arg_value = 'medio' 
        self.manager.current = 'game'
        self.manager.get_screen('game').set_difficulty(23, other_arg_value)

    def start_game_hard(self, instance=None):
        other_arg_value = 'dificil'
        self.manager.current = 'game'
        self.manager.get_screen('game').set_difficulty(15, other_arg_value)

    def go_back_to_main_menu(self, instance=None):
        # Implementation for going back to the main menu
        pass
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound_correct = SoundLoader.load('sounds/correct_answer.wav')
        self.sound_wrong = SoundLoader.load('sounds/wrong_answer.wav')
        self.questions = []
        self.correct_answers = []
        self.wrong_answers = []
        self.time_left = 0
        self.attempts = 0
        self.max_attempts = 3
        self.current_question_index = 0 
        self.timer_bar = ProgressBar()
        self.build_game_screen()

    def build_game_screen(self):
        layout = FloatLayout()

        if self.timer_bar.parent:
            self.timer_bar.parent.remove_widget(self.timer_bar)
        layout.add_widget(self.timer_bar)

        with layout.canvas.before:
            Color(0.02, 0.08, 0.15, 1)  # Fondo azul oscuro #021526
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[0])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.question_label = Label(
            text="Pregunta aquí",
            font_size=32,
            size_hint=(None, None),
            size=(600, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1)  # Texto blanco
        )
        self.question_label.text_size = (400, None)
        layout.add_widget(self.question_label)

        button_layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )

        self.answer_button1 = self.create_button("Respuesta 1")
        self.answer_button2 = self.create_button("Respuesta 2")
        self.answer_button3 = self.create_button("Respuesta 3")

        button_layout.add_widget(self.answer_button1)
        button_layout.add_widget(self.answer_button2)
        button_layout.add_widget(self.answer_button3)

        layout.add_widget(button_layout)

        # No vuelvas a crear el timer_bar aquí, ya lo has creado en __init__
        #layout.add_widget(self.timer_bar)

        with self.timer_bar.canvas.before:
            self.bar_color = Color(0.1, 0.5, 0.9, 1)  # Azul inicial
            self.bar_rect = RoundedRectangle(size=self.timer_bar.size, pos=self.timer_bar.pos)
            self.timer_bar.bind(pos=self._update_bar_rect, size=self._update_bar_rect)
        # Solo agrega el layout una vez
        self.add_widget(layout)
    
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
                size=(200, 50),
                background_normal='',
                background_color=(0.1, 0.5, 0.9, 1)  # Azul
            )
            button.bind(on_press=self.check_answer)
            return button

    def load_questions_and_answers(self, difficulty):
       
        # Definir la ruta base y la carpeta según la dificultad seleccionada
        base_path = f'text/{difficulty}/'
        
        # Archivos basados en la dificultad
        question_file = f"{base_path}questions.txt"
        correct_file = f"{base_path}correct_answers.txt"
        wrong_file = f"{base_path}wrong_answers.txt"

        with open(question_file, 'r', encoding='utf-8') as file:
            self.questions = [line.strip() for line in file.readlines()]

        with open(correct_file, 'r', encoding='utf-8') as file:
            self.correct_answers = [line.strip() for line in file.readlines()]

        with open(wrong_file, 'r', encoding='utf-8') as file:
            self.wrong_answers = [line.strip().split(',') for line in file.readlines()]

        if len(self.questions) != len(self.correct_answers) or len(self.questions) != len(self.wrong_answers):
            raise ValueError("El número de preguntas no coincide con el número de respuestas.")

        self.load_question(0)

    def load_question(self, index):
        self.current_question_index = index
        self.question_label.text = self.questions[index]

        correct_answer = self.correct_answers[index]
        wrong_answers = self.wrong_answers[index]

        all_answers = wrong_answers + [correct_answer]
        random.shuffle(all_answers)

        self.answer_button1.text = all_answers[0]
        self.answer_button2.text = all_answers[1]
        self.answer_button3.text = all_answers[2]

    def check_answer(self, instance):
            correct_answer = self.correct_answers[self.current_question_index]
            if instance.text == correct_answer:
                self.question_label.text = "¡Correcto!"
                if self.sound_correct:
                    self.sound_correct.play()
                # Sumar 2 segundos al temporizador sin exceder el máximo permitido
                self.time_left = min(self.time_left + 2, self.initial_time)  
                self.timer_bar.value = self.time_left
                
                if self.current_question_index + 1 < len(self.questions):
                    self.load_question(self.current_question_index + 1)
                else:
                    self.show_game_over_popup()
            else:#
                self.attempts += 1
                # Restar 2 segundos al temporizador sin reiniciar
                self.time_left = max(self.time_left - 2, 0)  # Asegurarte de que no sea menor a 0
                self.timer_bar.value = self.time_left
                
                if self.attempts >= self.max_attempts:
                    self.question_label.text = "¡Has fallado los 3 intentos!"
                    Clock.unschedule(self.update_time)  # Detener el temporizador
                    self.show_game_over_popup()
                else:
                    self.question_label.text = f"Incorrecto. Intentos restantes: {self.max_attempts - self.attempts}"
                    if self.sound_wrong:
                        self.sound_wrong.play()


    def update_time(self, dt):
            # Decrementamos el tiempo restante
        self.time_left -= 1
        if self.time_left <= 5:
            self.bar_color.rgba = (0.9, 0.1, 0.1, 1)  # Rojo
        else:
            self.bar_color.rgba = (0.1, 0.5, 0.9, 1)  # Azul                
        # Actualizamos el valor de la barra de progreso
        self.timer_bar.value = max(0, self.time_left)  # Nos aseguramos que no baje de 0
        
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
            Clock.schedule_interval(self.update_time, 1)  # Iniciar el temporizador
            #self.load_questions_and_answers()

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

class ConfigScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
            self.bg_rect = RoundedRectangle(size=layout.size, pos=layout.pos, radius=[0])
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.add_widget(layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

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
