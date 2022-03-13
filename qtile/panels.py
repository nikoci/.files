import os
import socket
import subprocess

from libqtile import bar, widget, qtile

from colors import reaper
from unicodes import lower_left_triangle

user = os.getenv('USER')
host = socket.gethostname()
backlight = int(subprocess.getoutput("light -G").split(".")[0])

wdefaults = dict(
    #font="JetBrains Mono Nerd Font",
    #font="ShureTechMono Nerd Font",
    font="BM mini",
    foreground=reaper['foreground'],
    fontsize=18,
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
            fontsize=20,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('firefox')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text=" ﬏ ",
            fontsize=22,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('code')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            fontsize=22,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('idea')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            fontsize=22,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('clion')}
        ),
        widget.TextBox(
            background=reaper['black4'],
            text="  ",
            fontsize=22,
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
            fontsize=20,
            disable_drag=True,
            center_aligned=True,
            borderwidth=0,
            margin_x=0,
            padding_x=10,
            highlight_method='line',
            block_highlight_text_color=reaper['highlight'],
            highlight_color=reaper['background']
        ),
        widget.Spacer(length=bar.STRETCH),
        lower_left_triangle(reaper['background'], reaper['black4']),
        widget.Clock(
            format=' %H:%M ',
            background=reaper['black4']
        ),
        lower_left_triangle(reaper['black4'], reaper['green1']),
        widget.Image(
            background=reaper['green1'],
            filename='~/.icons/pixelarticons/png/sort.png',
            margin=4
        ),
        widget.Wlan(
            interface='wlp1s0',
            background=reaper['green1'],
            foreground=reaper['background'],
            disconnected_message='DOWN ',
            format='UP ',
            fontsize=16
        ),
        widget.Image(
            background=reaper['green1'],
            filename='~/.icons/pixelarticons/png/sun.png',
            margin=4
        ),
        widget.TextBox(
            background=reaper['green1'],
            foreground=reaper['background'],
            text=f"{backlight}%",
            fontsize=16
        ),
        widget.Image(
            background=reaper['green1'],
            filename='~/.icons/pixelarticons/png/volume.png',
            margin=4
        ),
        widget.Volume(
            background=reaper['green1'],
            foreground=reaper['background'],
            fmt='{} ',
            fontsize=16
        ),
        widget.Image(
            background=reaper['green1'],
            filename='~/.icons/pixelarticons/png/battery.png',
            margin=4
        ),
        widget.Battery(
            background=reaper['green1'],
            foreground=reaper['background'],
            format='{percent:0.0%}  ',
            low_foreground=reaper['red1'],
            update_interval=10,
            fontsize=16
        ),
        #lower_left_triangle(reaper['green1'], reaper['cyan1']),
        widget.TextBox(
            text="    ",
            background=reaper['green2'],
            foreground=reaper['background'] 
        )
    ],

    size=32,
    background=reaper['background']
)