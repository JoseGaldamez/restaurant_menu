from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from sidemenu import SideMenu

Window.clearcolor = (1, 1, 1, 1)

class MiAplicacion(App):
    def build(self):
        self.title = 'Restaurante José Galdámez'
        
        root = FloatLayout()
        
        main_content = BoxLayout(orientation='vertical', padding=20, spacing=20)
        main_content.add_widget(Widget())
        main_content.add_widget(Label(text='Restaurante José Galdámez', color=(0, 0, 0, 1), font_size='30sp', size_hint_y=None, height=50))
        
        btn_open = Button(text='Ver menú', size_hint=(None, None), width=200, height=50, pos_hint={'center_x': 0.5})
        main_content.add_widget(btn_open)
        
        main_content.add_widget(Widget())
        
        side_menu = SideMenu()
        
        btn_open.bind(on_release=side_menu.open_menu)
        
        root.add_widget(main_content)
        root.add_widget(side_menu)
        
        return root

if __name__ == '__main__':
    MiAplicacion().run()