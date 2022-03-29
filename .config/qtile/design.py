from libqtile import layout
from libqtile.config import Match

colors = [
    # DEFAULT COLORS
    "#0b0b0f",  # [0] Primary Black color0
    "#1B1E27",  # [1] Secondary Black color8 OLD:16161D
    "#FF5D62",  # [2] Primary Red color1
    "#E46876",  # [3] Secondary Red color9
    "#6A9589",  # [4] Primary Green color2
    "#98BB6C",  # [5] Secondary Green color10
    "#FFA066",  # [6] Primary Yellow color3
    "#E6C384",  # [7] Secondary Yellow color11
    "#223249",  # [8] Primary Blue color4
    "#2D4F67",  # [9] Secondary Blue color12
    "#957FB8",  # [10] Primary Magenta color5
    "#D27E99",  # [11] Secondary Magenta color13
    "#7E9CD8",  # [12] Primary Cyan color6
    "#9CABCA",  # [13] Secondary Cyan color14
    "#DCD7BA",  # [14] Primary White color7
    "#727169",  # [15] Secondary White color15

    # EXTRA COLORS
    "#1E1F28",  # [16] 4.. (Darkest)
    "#2A2A37",  # [17] Shades.. (Dark)
    "#363646",  # [18] Of.. (Ligher)
    "#54546D",  # [19] Black (Light)
    "#7AA89F",  # [20] Pine Green
    "#D27E99",  # [21] Gumball Pink
    "#E82424",  # [22] Urgent Red
    "#7FB4CA",  # [23] Light Baby Blue
    "#658594",  # [24] Oceanic Blue
    "#C0A36E",  # [25] Vomit Brown

    "#16161e"  # [26] ULTRA DARK, not really
]

colors_default = [
    "#1F1F28",
    "#2A2A37",
    "#223249",
    "#727169",
    "#C8C093",
    "#DCD7BA",
    "#938AA9",
    "#363646",
    "#C34043",
    "#FFA066",
    "#DCA561",
    "#98BB6C",
    "#7FB4CA",
    "#7E9CD8",
    "#957FB8",
    "#D27E99",

    # EXTRA COLORS
    "#1E1F28",  # [16] 4.. (Darkest)
    "#2A2A37",  # [17] Shades.. (Dark)
    "#363646",  # [18] Of.. (Ligher)
    "#54546D",  # [19] Black (Light)
    "#7AA89F",  # [20] Pine Green
    "#D27E99",  # [21] Gumball Pink
    "#E82424",  # [22] Urgent Red
    "#7FB4CA",  # [23] Light Baby Blue
    "#658594",  # [24] Oceanic Blue
    "#C0A36E",  # [25] Vomit Brown
]

layout_theme = {
    "border_normal": colors[16],
    "border_focus": colors[16],
    "margin": 12,
    "border_on_single": True,
    "border_width": 4
}


def layouts(): return [layout.Columns(**layout_theme)]


def floating_layout():
    return layout.Floating(
        border_width=4,
        border_normal=colors[16],
        border_focus=colors[16],
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
