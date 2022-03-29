import design
import hook
import panels

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Match, Screen
from libqtile.lazy import lazy

keys = hook.binds()  # setting the key bindings
groups = hook.groups()  # setting the groups
hook.extend_binds(groups, keys)
layouts = design.layouts()
widget_defaults = panels.w_default_prop
extension_defaults = panels.e_default_prop

screens = panels.screens()

mouse = hook.m_binds()

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = design.floating_layout()
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "qtile"
