import design;
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)


def show_power_menu(qtile):
    controls = [
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=200,
        height=100,
        controls=controls,
        background=design.colors[1],
        initial_focus=None,
    )

    layout.show(x=1960, y=40)
