import kivy
kivy.require('1.9.1') # replace with your current kivy version !

"""Disclaimer, this UI code is poor and needs to be refactored a lot"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.checkbox import CheckBox
import ConfigurationUtility as Cu
import LogMain as Lm

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')


class LogsWidget(Widget):

    def btn_press(self, instance):
        print('The button is being pressed')

    def reposition_button(self):
        self.button.pos = 200, self.height/2 - self.button.height/2
        print("It ran")



class UIApp(App):
    # TODO refactor to use Kivy Language
    # TODO get a design machine to pick
    # TODO design a way to grab a file from the widget
    # TODO REFACTOR!!!!!!
    # TODO Create a way to indicate success in log zippage
    checked_boxes = []
    def build(self):
        '''In this method we need to return the root widget and set up the widget hierarchy'''
        root = BoxLayout(orientation='vertical')
        ip_address_layer = BoxLayout(orientation='horizontal')
        # d = BoxLayout(orientation='horizontal')
        a = AnchorLayout(anchor_x='center', anchor_y='center')

        # --------------- NEED TO REFACTOR BUTTON INTO KIVY LANGUAGE
        log_btn = Button(text="Get Logs") # , pos=(self.x, self.height / 2))
        log_btn.bind(on_press=self.btn_press)

        # REFACTOR THIS!!!! self needs to be refactored to possibly include a declaration
        self.ip_address_input = TextInput(multiline=False)

        ip_address_label = Label(text='i.p. address: ')#, size_hint_y=None)

        # Configure ip address layer
        ip_address_layer.size_hint_y = .35
        ip_address_layer.add_widget(ip_address_label)
        ip_address_layer.add_widget(a) #ip_address_dropdown) #ip_address_dropdown)
        a.add_widget(self.ip_address_input)

        # file_view = FileChooserIconView(path='C:\ZippedLogs')

        # ----------------- NEED TO REFACTOR THIS INTO LABEL CHECKBOX CLASSES OR TEMPLATES
        # Configure Check Box Layer
        log_check_boxes = GridLayout(cols=3)
        cb1_horizontal = BoxLayout(orientation='horizontal')
        self.cb1_Label = Label(text='BRE:')
        self.cb1 = CheckBox()
        cb1_horizontal.add_widget(self.cb1_Label)
        cb1_horizontal.add_widget(self.cb1)

        cb2_horizontal = BoxLayout(orientation='horizontal')
        self.cb2_Label = Label(text='WEB:')
        self.cb2 = CheckBox()
        cb2_horizontal.add_widget(self.cb2_Label)
        cb2_horizontal.add_widget(self.cb2)

        cb3_horizontal = BoxLayout(orientation='horizontal')
        self.cb3_Label = Label(text='NET:')
        self.cb3 = CheckBox()
        cb3_horizontal.add_widget(self.cb3_Label)
        cb3_horizontal.add_widget(self.cb3)

        cb4_horizontal = BoxLayout(orientation='horizontal')
        self.cb4_Label = Label(text='OFF:')
        self.cb4 = CheckBox()
        cb4_horizontal.add_widget(self.cb4_Label)
        cb4_horizontal.add_widget(self.cb4)

        cb5_horizontal = BoxLayout(orientation='horizontal')
        self.cb5_Label = Label(text='DAL:')
        self.cb5 = CheckBox()
        cb5_horizontal.add_widget(self.cb5_Label)
        cb5_horizontal.add_widget(self.cb5)

        cb6_horizontal = BoxLayout(orientation='horizontal')
        self.cb6_Label = Label(text='WIN:')
        self.cb6 = CheckBox()
        cb6_horizontal.add_widget(self.cb6_Label)
        cb6_horizontal.add_widget(self.cb6)

        self.cb1.bind(active=self.on_checkbox_active)
        self.cb2.bind(active=self.on_checkbox_active)
        self.cb3.bind(active=self.on_checkbox_active)
        self.cb4.bind(active=self.on_checkbox_active)
        self.cb5.bind(active=self.on_checkbox_active)
        self.cb6.bind(active=self.on_checkbox_active)
        # ----------------- NEED TO REFACTOR THIS INTO LABEL CHECKBOX CLASSES OR TEMPLATES


        log_check_boxes.add_widget(cb1_horizontal)
        log_check_boxes.add_widget(cb2_horizontal)
        log_check_boxes.add_widget(cb3_horizontal)
        log_check_boxes.add_widget(cb4_horizontal)
        log_check_boxes.add_widget(cb5_horizontal)
        log_check_boxes.add_widget(cb6_horizontal)


        root.add_widget(ip_address_layer)
        root.add_widget(log_check_boxes)
        root.add_widget(log_btn)
        # b.add_widget(file_view)
        return root

    # TODO remove btn_press function outside of this class
    # TODO get the checked check boxes
    def btn_press(self, instance):
        print("Hello!" + self.ip_address_input.text)
        print(instance)
        user = Cu.get_user()
        print(user)

        password = Cu.get_password()
        print(password)
        code = Lm.connect_and_process('\\\\' + self.ip_address_input.text, user, password)
        pass

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
            self.checked_boxes.append(checkbox)
        else:
            print('The checkbox', checkbox, 'is inactive')

if __name__ == '__main__':
    UIApp().run()