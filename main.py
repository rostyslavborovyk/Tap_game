from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
import time
import random


class BoxContainer(BoxLayout):

    def __init__(self, **kwargs):
        super(BoxContainer, self).__init__(**kwargs)
        self.ls_of_buttons = [(self.button1, 1), (self.button2, 2), (self.button3, 3), (self.button4, 4),
                              (self.button5, 5), (self.button6, 6), (self.button7, 7), (self.button8, 8)]
    tapped = NumericProperty(1)
    pb_value = NumericProperty(100)
    decreasing_speed = NumericProperty(0.2)
    current_button = ObjectProperty(None)
    current_button_id = NumericProperty(0)

    def main_loop(self, *args):
        self.pb_value -= self.decreasing_speed

    def action(self, btn_id):
        if self.pb_value <= 0:
            for i in self.ls_of_buttons:
                i[0].text = "{}!".format(self.tapped)

        else:
            if self.current_button_id == btn_id or not self.current_button:
                ls_btns = self.ls_of_buttons.copy()
                if self.current_button:
                    ls_btns.remove((self.current_button, self.current_button_id))
                button = random.choice(ls_btns)

                button[0].background_color = (random.uniform(0.5, 1), random.uniform(0.5,1), random.uniform(0.5, 1), 1)
                button[0].text = str(self.tapped)
                self.tapped += 1
                if self.current_button:
                    self.current_button.background_color = (1, 1, 1, 1)
                    self.current_button.text = ''
                self.current_button = button[0]
                self.current_button_id = button[1]

                self.pb_value += 2
                self.decreasing_speed += 0.02


class TestApp(App):
    def build(self):
        bc = BoxContainer()
        Clock.schedule_interval(bc.main_loop, 1 / 30)
        return bc


if __name__ == '__main__':
    TestApp().run()
