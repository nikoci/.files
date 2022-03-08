#▒▒▒▒▒▒▒▒▒▄██████     ▄▄▄█▄
#▒▒▒▒▒▒▒▄██▀░░▀██▄    ████████▄
#▒▒▒▒▒▒███░░░░░░██      █▀▀▀▀▀██▄▄
#▒▒▒▒▒▄██▌░░░░░░░██    ▐▌        ▀█▄
#▒▒▒▒▒███░░▐█░█▌░██    █▌          ▀▌
#▒▒▒▒████░▐█▌░▐█▌██   ██        ──────────────────────────────────────────────
#▒▒▒▐████░▐░░░░░▌██   █▌            QTile 'Reaper' configuration by Dehys
#▒▒▒▒████░░░▄█░░░██  ▐█         ──────────────────────────────────────────────
#▒▒▒▒████░░░██░░██▌  █▌         >   Version: 1.0.0
#▒▒▒▒████▌░▐█░░███   █          >   License: MIT
#▒▒▒▒▐████░░▌░███   ██          >   Author: Arijan (Dehys) Nikoci
#▒▒▒▒▒████░░░███    █▌
#▒▒▒██████▌░████   ██           Link: https://github.com/dehys/reaper-qtile/qtile
#▒▐████████████  ███            Github: https://github.com/dehys
#▒█████████████▄████            Website: https://dehys.com
#██████████████████             Discord: https://discord.gg/SxwUsgk 

#───────────────────────[Imports]───────────────────────
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.widget.textbox import TextBox
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#──────────────────────[Variables]──────────────────────
mod = "mod4"
terminal = "kitty"
browser = "firefox"

#─────────────────────[Keybindings]─────────────────────
keys = [
#   <────────(Backlight/Volume)────────>
        # Increase backlight brightness
        Key(
            [],"XF86MonBrightnessUp",
            lazy.spawn("light -A 10"),
            desc="Increase backlight brightness"
        ),
        # Decrease backlight brightness
        Key(
            [],"XF86MonBrightnessDown",
            lazy.spawn("light -U 10"),
            desc="Decrease backlight brightness"
        ),
        # Increase master volume
        Key(
            [],"XF86AudioRaiseVolume",
            lazy.spawn("amixer set Master 5%+"),
            desc="Increase master volume"
        ),
        # Decrease master volume
        Key(
            [],"XF86AudioLowerVolume",
            lazy.spawn("amixer set Master 5%-"),
            desc="Decrease master volume"
        ),
        # Toggle mute for master volume
        Key(
            [],"XF86AudioMute",
            lazy.spawn("amixer set Master toggle"),
            desc="Toggle mute for master volume"
        ),
    
#   <──────────(Applications)──────────>
        # Launch terminal
        Key(
            [mod],"Return",
            lazy.spawn(terminal),
            desc="Launch terminal"
        ),
        # Launch browser
        Key(
            [mod],"b",
            lazy.spawn(browser),
            desc="Launch browser"
        ),

#   <─────────────(Layout)─────────────>
        Key(
            [mod],"h",
            lazy.layout.left(),
            desc="Move focus to left"
        ),
        Key(
            [mod],"l",
            lazy.layout.right(),
            desc="Move focus to right"
        ),
        Key(
            [mod],"j",
            lazy.layout.down(),
            desc="Move focus down"
        ),
        Key(
            [mod],"k",
            lazy.layout.up(),
            desc="Move focus up"
        ),
        Key(
            [mod],"space",
            lazy.layout.next(),
            desc="Move window focus to other window"),
        Key(
            [mod, "shift"],"h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left"
        ),
        Key(
            [mod, "shift"],"l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right"
        ),
        Key(
            [mod, "shift"],"j",
            lazy.layout.shuffle_down(),
            desc="Move window down"
        ),
        Key(
            [mod, "shift"],"k",
            lazy.layout.shuffle_up(),
            desc="Move window up"
        ),
        Key(
            [mod, "control"],"h",
            lazy.layout.grow_left(),
            desc="Grow window to the left"
        ),
        Key(
            [mod, "control"],"l",
            lazy.layout.grow_right(),
            desc="Grow window to the right"
        ),
        Key(
            [mod, "control"],"j",
            lazy.layout.grow_down(),
            desc="Grow window down"
        ),
        Key(
            [mod, "control"],"k",
            lazy.layout.grow_up(),
            desc="Grow window up"
        ),
        Key(
            [mod],"n",
            lazy.layout.normalize(),
            desc="Reset all window sizes"
        ),
        Key(
            [mod, "shift"],"Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key(
            [mod],"Tab",
            lazy.next_layout(),
            desc="Toggle between layouts"
        ),

#   <──────────────(Other)─────────────>
        Key(
            [mod],"w",
            lazy.window.kill(),
            desc="Kill focused window"
        ),
        Key(
            [mod, "control"],"r",
            lazy.reload_config(),
            desc="Reload the config"
        ),
        Key(
            [mod, "control"],"q",
            lazy.shutdown(),
            desc="Shutdown Qtile"
        ),
        Key(
            [mod],"r",
            lazy.spawncmd(),
            desc="Spawn a command using a prompt widget"
        ),
]

#───────────────────────[Groups]───────────────────────
groups = [
    Group('1', label="零", layout="monadtall"),
    Group('2', label="dev", layout="monadtall"),
    Group('3', label="sys", layout="monadtall"),
    Group('4', label="chat", layout="monadtall"),
    Group('5', label="other", layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # Yeet yourself yo another group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # Yeet window to another group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
            ),
        ]
    )


#───────────────────────[Layout]───────────────────────
layout_theme = {
    "border_normal": "#000000",
	"border_focus": "#93baea",
	"border_width": 2,
	"margin": 20
}

layouts = [
    # layout.Columns(**layout_theme, fair="TRUE"),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_normal="#000000", border_focus="#93baea", border_width=2, margin=15),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#───────────────────────[Wigets/Screen]───────────────────────
widget_defaults = dict(
    font="Jetbrains Mono",
    fontsize=14,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(format="%a | %I:%M")
            ],
            32,
        ),
    ),
]


#───────────────────────[Floating/Other]───────────────────────
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"
