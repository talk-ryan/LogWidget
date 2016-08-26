import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.filechooser import FileChooserIconView

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class LogsWidget(Widget):

    def btn_press(self, instance):
        print('The button is being pressed')

    def reposition_button(self):
        self.button.pos = 200, self.height/2 - self.button.height/2
        print("It ran")


class UIApp(App):
    def build(self):
        '''In this method we need to return the root widget and set up the widget hierarchy'''
        b = BoxLayout(orientation='vertical')
        c = BoxLayout(orientation='horizontal')
        # d = BoxLayout(orientation='horizontal')
        a = AnchorLayout(anchor_x='center', anchor_y='center')

        btn = Button(text="Get Logs") # , pos=(self.x, self.height / 2))
        btn.bind(on_press=self.btn_press)
        t = TextInput(multiline=False)

        l = Label(text='i.p. address: ', size_hint_y=None)
        c.size_hint_y = 1
        c.add_widget(l)
        c.add_widget(a)
        a.add_widget(t)



        file_view = FileChooserIconView(path='C:\ZippedLogs')

        b.add_widget(c)
        b.add_widget(btn)
        b.add_widget(file_view)
        return b

    def btn_press(self, instance):
        print(instance)
        print("Hello!")
        pass

if __name__ == '__main__':
    UIApp().run()