from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class LogCheckBox(Widget):
    """ Log Check box contains a Label and a Checkbox in the same widget.
    """

    def __init__(self, name, orientation='horizontal'):
        super().__init__()
        self.cbx = CheckBox()
        self.label = Label(text=name)
        self.widget = BoxLayout(orientation=orientation)
        self.widget.add_widget(self.label)
        self.widget.add_widget(self.cbx)

    def bindActiveFunction(self, func):
        self.cbx.bind(active=func)

    def getWidget(self):
        return self.widget

    def getCheckBox(self):
        return self.cbx

    def getLabel(self):
        return self.label

