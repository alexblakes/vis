from matplotlib import cm
from matplotlib import colors as mc

red = cm.Reds(0.8)
blue = cm.Blues(0.8)


def adjust_alpha(color, alpha):
    return mc.to_rgba(color, alpha)
