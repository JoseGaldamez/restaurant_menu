from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation

class SideMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (0.75, 1)
        self.pos_hint = {'x': -0.75}  # Esto es para que no se vea el menu al inicio 
        self.padding = 20
        self.spacing = 10
        
        # Fondo del menú, un gris calito
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Contenedor para el botón de cerrar (alineado a la derecha)
        header = BoxLayout(size_hint_y=None, height=50)
        header.add_widget(Widget()) # Espaciador para empujar el botón a la derecha
        
        close_btn = Button(text='X', size_hint=(None, None), size=(50, 50),
                           background_normal='', background_color=(0.8, 0.2, 0.2, 1))

        close_btn.bind(on_release=self.close_menu)
        header.add_widget(close_btn)
        
        self.add_widget(header)
        self.add_widget(Label(text='Opciones del Menú', color=(0,0,0,1), font_size='20sp'))
        self.add_widget(Widget())

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def open_menu(self, *args):
        anim = Animation(pos_hint={'x': 0}, duration=0.3, t='out_quad')
        anim.start(self)

    def close_menu(self, *args):
        anim = Animation(pos_hint={'x': -0.75}, duration=0.3, t='in_quad')
        anim.start(self)