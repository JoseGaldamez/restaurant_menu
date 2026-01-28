import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Configurar tamaño de ventana para simular smartphone
Window.size = (390, 800)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

JSON_FILE = 'menu.json'

def cargar_datos():        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

class SectionHeader(BoxLayout):
    def __init__(self, title, bg_color, back_func, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 60
        self.padding = [10, 0]
        
        with self.canvas.before:
            Color(*bg_color)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rect, size=self._update_rect)
        
        btn_back = Button(
            text="< Volver", 
            size_hint_x=None, width=100, 
            background_normal='', 
            background_color=(1, 1, 1, 0.2) 
        )
        btn_back.bind(on_release=back_func)
        
        lbl_title = Label(text=title, font_size='20sp', bold=True)
        
        self.add_widget(btn_back)
        self.add_widget(lbl_title)

    def _update_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        lbl = Label(text="Restaurante\nJosé Galdámez", 
                   font_size='30sp', color=(0.2, 0.2, 0.2, 1), halign='center')
        layout.add_widget(lbl)
        
        btn = Button(
            text="VER MENÚ",
            size_hint=(None, None), size=(200, 80),
            pos_hint={'center_x': 0.5},
            background_normal='', background_color=(0.1, 0.6, 0.8, 1),
            font_size='20sp', bold=True
        )
        btn.bind(on_release=self.ir_a_categorias)
        layout.add_widget(btn)
        self.add_widget(layout)

    def ir_a_categorias(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'categorias'

class CategoryScreen(Screen):
    def on_enter(self):
        self.layout_principal.clear_widgets()
        
        header = SectionHeader(
            title="Categorías", 
            bg_color=(0.2, 0.2, 0.2, 1), 
            back_func=self.volver_inicio
        )
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=20)
        grid.bind(minimum_height=grid.setter('height'))
        
        data = cargar_datos()
        for cat in data['categories']:
            btn = Button(
                text=cat['name'],
                size_hint_y=None, height=80,
                background_normal='', background_color=(0.1, 0.5, 0.8, 1),
                font_size='18sp'
            )
            btn.bind(on_release=lambda x, category=cat: self.ir_a_productos(category))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        self.layout_principal.add_widget(header)
        self.layout_principal.add_widget(scroll)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout_principal = BoxLayout(orientation='vertical')
        self.add_widget(self.layout_principal)

    def volver_inicio(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

    def ir_a_productos(self, category_data):
        products_screen = self.manager.get_screen('productos')
        products_screen.category_data = category_data
        self.manager.transition.direction = 'left'
        self.manager.current = 'productos'

class ProductScreen(Screen):
    category_data = {}

    def on_enter(self):
        self.layout_principal.clear_widgets()
        
        title_text = self.category_data.get('name', 'Productos')
        
        header = SectionHeader(
            title=title_text,
            bg_color=(0.1, 0.6, 0.8, 1), 
            back_func=self.volver_categorias
        )
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=2, padding=0)
        grid.bind(minimum_height=grid.setter('height'))
        
        products = self.category_data.get('products', [])
        
        for prod in products:
            row = BoxLayout(size_hint_y=None, height=60, padding=[20, 0])
            
            with row.canvas.before:
                Color(1, 1, 1, 1)
                row.bg_rect = Rectangle(pos=row.pos, size=row.size)
            
            def update_row_rect(instance, value):
                instance.bg_rect.pos = instance.pos
                instance.bg_rect.size = instance.size
            row.bind(pos=update_row_rect, size=update_row_rect)

            lbl_name = Label(
                text=prod['name'], 
                color=(0.2, 0.2, 0.2, 1),
                text_size=(None, None), halign='left', valign='middle',
                size_hint_x=0.7
            )
            lbl_name.bind(size=lambda x,y: setattr(x, 'text_size', (x.width, None)))
            
            lbl_price = Label(
                text=f"L. {prod['price']}", 
                color=(0, 0.5, 0, 1), bold=True, 
                size_hint_x=0.3
            )
            
            row.add_widget(lbl_name)
            row.add_widget(lbl_price)
            grid.add_widget(row)
            
        scroll.add_widget(grid)
        self.layout_principal.add_widget(header)
        self.layout_principal.add_widget(scroll)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout_principal = BoxLayout(orientation='vertical')
        self.add_widget(self.layout_principal)

    def volver_categorias(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'categorias'


class RestauranteApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CategoryScreen(name='categorias'))
        sm.add_widget(ProductScreen(name='productos'))
        return sm

if __name__ == '__main__':
    RestauranteApp().run()