import time

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (400, 300)
Window.clearcolor = get_color_from_hex('#3385ff')

KV = '''
BoxLayout:
    orientation: 'vertical'

    Label:
        id: time
        text: '[b]00[/b]:00:00'
        font_size: 55
        markup: True
'''

class ClockApp(App):
    def build(self):
        return Builder.load_string(KV)

    def update_clock(self, nap):
        self.root.ids.time.text = time.strftime('   Clock\n[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_clock, 1)

ClockApp().run()
