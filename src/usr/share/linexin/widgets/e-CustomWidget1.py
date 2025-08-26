import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MyCustomWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.widgetname = "Custom Widget"
        # Icon can be any image format: .svg, .png, .jpg, etc.
        self.widgeticon = ""
        
        # Add your widget content here
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        
        title = Gtk.Label(label="Welcome to My Custom Widget!")
        title.add_css_class("title-2")
        self.append(title)
        
        description = Gtk.Label(label="This is an example widget with a custom icon")
        self.append(description)
        
        button = Gtk.Button(label="Click Me!")
        button.set_halign(Gtk.Align.CENTER)
        self.append(button)
