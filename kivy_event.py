from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

KV = '''
<Tab>:
    orientation: "horizontal"
    MDLabel:
        id: label
        text: root.text
        halign: "center"
    MDLabel:
        id: label
        text: root.text
        halign: "center"

BoxLayout:
    orientation: "vertical"
    
    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
'''

class Tab(BoxLayout, MDTabsBase):
    pass

class MainApp(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass


MainApp().run()
