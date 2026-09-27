from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizMastiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Quiz Masti!', font_size='30sp'))
        layout.add_widget(Button(text='Start Quiz', size_hint=(1, 0.2)))
        return layout

QuizMastiApp().run()
