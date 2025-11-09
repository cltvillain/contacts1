from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class ContactShareApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Do you want to share your contact?", font_size=20))
        
        btn_layout = BoxLayout(size_hint_y=0.3, spacing=20)
        yes_btn = Button(text="Yes", background_color=(0, 0.6, 1, 1))
        no_btn = Button(text="No", background_color=(0.8, 0, 0, 1))
        
        yes_btn.bind(on_release=self.yes_action)
        no_btn.bind(on_release=self.no_action)
        
        btn_layout.add_widget(yes_btn)
        btn_layout.add_widget(no_btn)
        layout.add_widget(btn_layout)
        return layout

    def yes_action(self, instance):
        popup = Popup(title='Confirmed',
                      content=Label(text='You clicked YES. Action simulated ethically.'),
                      size_hint=(0.7,0.3))
        popup.open()

    def no_action(self, instance):
        popup = Popup(title='Cancelled',
                      content=Label(text='You clicked NO. Nothing happens.'),
                      size_hint=(0.7,0.3))
        popup.open()

if __name__ == "__main__":
    ContactShareApp().run()
