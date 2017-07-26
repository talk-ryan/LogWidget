from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from functools import partial

class LogCheckBox(BoxLayout):
    """ Log Check box contains a Label and a Checkbox in the same widget.
    """

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.cbx = CheckBox()
        self.label = Label(text=name)
        self.add_widget(self.label)
        self.add_widget(self.cbx)

    def bindActiveFunction(self, func):
        self.cbx.bind(active=partial(func, logcheckbox=self))

    def getCheckBox(self):
        return self.cbx

    def getLabel(self):
        return self.label

