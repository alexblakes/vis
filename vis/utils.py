import matplotlib.pyplot as plt

def rotate_tick_labels(axis, ax=None, **kwargs):
    if axis not in ("x", "y"):
        raise ValueError("axis must be 'x' or 'y'")

    kwargs.setdefault("rotation", 45)
    kwargs.setdefault("rotation_mode", "anchor")
    kwargs.setdefault("ha", "right")

    ax = ax or plt.gca()

    if axis == "x":
        ax.set_xticks(ax.get_xticks(), labels=ax.get_xticklabels(), **kwargs)
    if axis == "y":
        ax.set_yticks(ax.get_yticks(), labels=ax.get_yticklabels(), **kwargs)

    return ax