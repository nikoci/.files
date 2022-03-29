import libqtile
from libqtile.config import Screen

from design import colors
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration

w_default_prop = dict(
    font="JetBrainsMonoMedium Nerd Font",
    fontsize=14,
    padding=0,
    foreground=colors[14],
    background=colors[0]
)

e_default_prop = dict(
    font="JetBrainsMonoMedium Nerd Font",
    fontsize=18,
    padding=0,
    foreground=colors[14],
    background=colors[0]
)

bar_prop = {
    "size": 44,
    "background": colors[0]
}

left_bar_prop = {
    "size": 44,
    "background": colors[0]
}

line_decor_horiz = {
    "decorations": [
        BorderDecoration(
            border_width=[0, 0, 4, 0],
            colour=colors[1],
            padding=0,
            padding_x=-5,
            padding_y=None
        )
    ],
    "padding": 0,
}

line_decor_vert = {
    "decorations": [
        BorderDecoration(
            border_width=[0, 4, 0, 0],
            colour=colors[1],
            padding=0,
            padding_x=None,
            padding_y=-5
        )
    ],
    "padding": 0,
}

app_decor = {
    "decorations": [
        #RectDecoration(
        #    colour=colors[26], radius=8, filled=True, padding=8
        #),
        BorderDecoration(
            border_width=[0, 4, 0, 0],
            colour=colors[1],
            padding_x=None,
            padding_y=-8,
        )
    ]
}

app_decor_spacer = {
    "decorations": [
        BorderDecoration(
            border_width=[0, 0, 2, 0],
            colour=colors[1],
            padding_x=20,
            padding_y=0,
        )
    ]
}

app_margin = {
    "margin_x": 12,
    "margin_y": 6
}

def w_groups(): return widget.GroupBox(
    #**line_decor_horiz,
    active=colors[15],
    inactive=colors[15],
    disable_drag=True,
    center_aligned=True,
    borderwidth=0,
    margin_x=0,
    padding_x=8,
    fontsize=18,
    highlight_method='text',
    highlight_color=colors[10]
)


def w_battery(): return widget.Battery(
    #**line_decor_horiz,
    fmt='  {}',
    format='{percent:0.0%}  ',
    hide_threshold=100,
    update_interval=10,
)


def w_full_spacer(): return widget.Spacer(
    #**line_decor_horiz,
    length=libqtile.bar.STRETCH
)


def bar_widgets(): return [
    widget.Image(
        filename="~/.icons/default/arch.png",
        margin=12,
        decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour=colors[1], padding_x=40)]
    ),
    widget.TextBox(text="dehys", **line_decor_horiz, foreground=colors[4], fontsize=18),
    widget.TextBox(text="@", fontsize=18, foreground=colors[14], decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#181b23", padding=0)]),
    widget.TextBox(text="by", fontsize=18, foreground=colors[4], decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#15181f", padding=0)]),
    widget.TextBox(text="th", fontsize=18, foreground=colors[4], decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#12151b", padding=0)]),
    widget.TextBox(text="ew", fontsize=18, foreground=colors[4], decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#101217", padding=0)]),
    widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#0d0f13", padding=0)]),
    widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 0, 4, 0], colour="#0a0c0f", padding=0)]),
    widget.Prompt(),
    w_full_spacer(),
    w_groups(),
    w_full_spacer(),
    w_battery(),
    widget.Clock(format=" %H:%M"),
    widget.Spacer(length=20)
]


def left_bar_widgets(): return [
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/firefox2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('firefox')}
    ),
    #widget.TextBox(text=" ╿ ", foreground=colors[1], **line_decor_vert),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/vscode2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('code')}
    ),
    #widget.TextBox(text=" ╿ ", foreground=colors[1], **line_decor_vert),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/intellij2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('idea')}
    ),
    #widget.TextBox(text=" ╿ ", foreground=colors[1], **line_decor_vert),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/pycharm2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('pycharm')}
    ),
    #widget.TextBox(text=" ╿ ", foreground=colors[1], **line_decor_vert),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/terminal2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('kitty')}
    ),
    #widget.TextBox(text=" ╿ ", foreground=colors[1], **line_decor_vert),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/github2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('firefox --new-window https://github.com/dehys')}
    ),
    widget.Image(
        **app_decor, **app_margin,
        filename="~/.icons/default/discord2.png",
        mouse_callbacks={'Button1': lambda: libqtile.qtile.cmd_spawn('discord')}
    ),
    widget.Spacer(**line_decor_vert, length=libqtile.bar.STRETCH),
    widget.TextBox(text="qタイル ウィンドウ マネージャ  ", **line_decor_vert, foreground=colors[1], fontsize=18),
    widget.Spacer(length=libqtile.bar.STRETCH, **line_decor_vert),
    widget.Image(
        **app_decor,
        filename="~/.icons/default/bluetooth.png",
        margin=10
    ),
    widget.Image(
        **app_decor,
        filename="~/.icons/default/speaker.png",
        margin=10
    ),
    widget.Image(
        **app_decor,
        filename="~/.icons/default/power.png",
        margin=10
    ),
    widget.Spacer(**line_decor_vert, length=4)
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#181b23", padding_y=-2)]),
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#15181f", padding_y=-2)]),
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#12151b", padding_y=-2)]),
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#101217", padding_y=-2)]),
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#0d0f13", padding_y=-2)]),
    #widget.Spacer(length=20, decorations=[BorderDecoration(border_width=[0, 4, 0, 0], colour="#0a0c0f", padding_y=-2)])
]


def bar(): return libqtile.bar.Bar(
    bar_widgets(),
    **bar_prop
)


def left_bar(): return libqtile.bar.Bar(
    left_bar_widgets(),
    **left_bar_prop
)


def screens(): return [Screen(
    top=bar(),
    left=left_bar()
)]
