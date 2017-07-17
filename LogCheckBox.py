from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class LogCheckBox(object):
    """ Log Check box contains a Label and a Checkbox in the same widget.
    """
    def __init__(self, name, orientation='horizontal'):
        cbx = CheckBox()
        label = Label(text=name)
        widget = BoxLayout(orientation=orientation)
        widget.add_widget(label)
        widget.add_widget(cbx)

    def bindActiveFunction(self, func):
        self.cbx.bind(active=func)

    def getWidget(self):
        return self.widget

