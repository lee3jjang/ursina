from kivy.lang import Builder
from kivymd.app import MDApp
from kv_class import *
from kivymd.uix.list import OneLineIconListItem

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('kv_file.kv')

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }

        for icon_name in list(icons_item.keys())[:-2]:
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        def func(name):
            self.root.ids.nav_drawer.set_state("close")
            self.root.ids.screen_manager.current = name

        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon="checkbox-marked", text="Shared with me", on_release=lambda x: func("scr 1"))
        )

        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon="upload", text="upload", on_release=lambda x: func("scr 2"))
        )

MyApp().run()