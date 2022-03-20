from libqtile import bar, widget, qtile

from colors import reaper
from unicodes import lower_left_triangle

wdefaults = dict(
    font="JetBrains Mono Nerd Font",
    foreground=reaper['foreground'],
    fontsize=12,
    padding=0,
)

bar = bar.Bar(
    [
        widget.TextBox(
            text="  Reaper",
            background=reaper['blue2'],
            foreground=reaper['background']
        ),
        lower_left_triangle(reaper['blue2'], reaper['black4']),
        widget.TextBox(
            background=reaper['black4'],
            text=" ",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('firefox')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text=" ﬏ ",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('code')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('idea')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('clion')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pycharm')}
        ),
        widget.Prompt(
            background=reaper['black4'],
            foreground=reaper['red1'],
            prompt='   '
        ),
        lower_left_triangle(reaper['black4'], reaper['background']),
        widget.WindowName(
            format="{state}{name}",
            max_chars=60
        ),
        widget.Spacer(length=bar.STRETCH),
        widget.GroupBox(
            active=reaper['inactive'],
            inactive=reaper['inactive'],
            fontsize=16,
            disable_drag=True,
            center_aligned=True,
            borderwidth=0,
            margin_x=0,
            padding_x=10,
            highlight_method='line',
            block_highlight_text_color=reaper['magenta2'],
            highlight_color=reaper['background']
        ),
        widget.Spacer(length=bar.STRETCH),
        lower_left_triangle(reaper['background'], reaper['black4']),
        widget.Clock(
            format=' %H:%M ',
            background=reaper['black4']
        ),
        lower_left_triangle(reaper['black4'], reaper['green1']),
        widget.CPU(
            background=reaper['green1'],
            foreground=reaper['background'],
            format=' cpu {load_percent} '
        ),
        widget.TextBox(
            text="    ",
            margin=10,
            background=reaper['green2'],
            foreground=reaper['background'] 
        )
    ],

    size=24,
    background=reaper['background']
)