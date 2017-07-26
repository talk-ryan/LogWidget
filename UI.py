import kivy
kivy.require('1.9.1') # replace with your current kivy version !

""" Run this script as the start of the application.  This will show a UI widget with check boxes that can be clicked.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import ConfigurationUtility as Cu
import LogMain as Lm
import LogCheckBox as LCB

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
LOGCHECKBOX = 'logcheckbox'

class LogsWidget(Widget):

    def btn_press(self, instance):
        print('The button is being pressed')

    def reposition_button(self):
        self.button.pos = 200, self.height/2 - self.button.height/2
        print("It ran")



class UIApp(App):
    # TODO get a design machine to pick
    # TODO design a way to grab a file from the widget
    # TODO Create a way to indicate success in log zippage

    # Holds the logs that we need to pass into the backend
    log_checked_boxes = set()

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

        log_check_boxes = self.initCheckBoxLayer()

        root.add_widget(ip_address_layer)
        root.add_widget(log_check_boxes)
        root.add_widget(log_btn)
        # b.add_widget(file_view)
        return root

    def initCheckBoxLayer(self, num_cols=3):
        # Configure Check Box Layer
        log_check_boxes = GridLayout(cols=num_cols)
        for section in Cu.get_sections_of_log_files():
            wid = LCB.LogCheckBox(section)
            wid.bindActiveFunction(self.on_log_checkbox_active)
            log_check_boxes.add_widget(wid)
        return log_check_boxes

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

    def on_log_checkbox_active(self, checkbox, value, **kwargs):
        print(kwargs[LOGCHECKBOX])
        log_cbx = kwargs[LOGCHECKBOX]
        if value:
            self.log_checked_boxes.add(log_cbx)
        else:
            self.log_checked_boxes.remove(log_cbx)

if __name__ == '__main__':
    UIApp().run()