import bpy
from bpy import context

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


ShowMessageBox(message = "this is messqge ", title = "Message Box", icon = 'INFO')