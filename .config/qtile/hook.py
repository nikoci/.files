from libqtile.config import Group, Key, Drag, Click
from libqtile.lazy import lazy
import menus

mod = "mod4"
terminal = "kitty"
browser = "firefox"
explorer = "ranger"
launcher = "rofi"


def binds(): return [
    #   <────────(Backlight/Volume)────────>
    # Increase backlight brightness
    Key(
        [], "XF86MonBrightnessUp",
        lazy.spawn("light -A 10"),
        desc="Increase backlight brightness"
    ),
    # Decrease backlight brightness
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("light -U 10"),
        desc="Decrease backlight brightness"
    ),
    # Increase master volume
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+"),
        desc="Increase master volume"
    ),
    # Decrease master volume
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-"),
        desc="Decrease master volume"
    ),
    # Toggle mute for master volume
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"),
        desc="Toggle mute for master volume"
    ),

    #   <──────────(Applications)──────────>
    # Launch terminal
    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    # Launch browser
    Key(
        [mod], "b",
        lazy.spawn(browser),
        desc="Launch browser"
    ),
    Key(
        [mod], "s",
        lazy.spawn("ulauncher --no-window-shadow"),
        desc="Launch ulauncher"
    ),
    Key(
        [mod, "shift"], "r",
        lazy.spawn("kitty -e ranger"),
        desc="Launch ranger"
    ),

    #   <─────────────(Layout)─────────────>
    Key(
        [mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key(
        [mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key(
        [mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key(
        [mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),

    #   <──────────────(Other)─────────────>
    Key(
        [mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key(
        [mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key(
        [mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    Key(
        [mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
    ),
    Key(
        [mod], "p",
        lazy.function(menus.show_power_menu)
    )
]


def m_binds(): return [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


def groups(): return [
    Group('1', label="壱", layout="monadtall"),
    Group('2', label="弐", layout="monadtall"),
    Group('3', label="参", layout="monadtall"),
    Group('4', label="四", layout="monadtall"),
    Group('5', label="五", layout="monadtall"),
    Group('6', label="六", layout="monadtall"),
]


def extend_binds(g, k):
    for i in g:
        k.extend(
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


def switch_to_group(i):

    lazy.group[i.name].toscreen()

