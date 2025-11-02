import matplotlib.pyplot as plt
import numpy as np


def boxplot(
    dfg,
    col,
    colors,
    ax=None,
    label_n=True,
    min_n=5,
    scatter_kwargs=None,
    boxplot_kwargs=None,
):
    ax = ax or plt.gca()

    if scatter_kwargs is None:
        scatter_kwargs = {}

    scatter_kwargs.setdefault("lw", 0)
    scatter_kwargs.setdefault("alpha", 0.3)

    if boxplot_kwargs is None:
        boxplot_kwargs = {}

    boxplot_kwargs.setdefault("vert", True)
    boxplot_kwargs.setdefault("whis", [2.5, 97.5])
    boxplot_kwargs.setdefault("widths", [0.5])
    boxplot_kwargs.setdefault("showfliers", False)
    boxplot_kwargs.setdefault("showmeans", True)
    boxplot_kwargs.setdefault("medianprops", dict(color="black"))
    boxplot_kwargs.setdefault(
        "meanprops",
        dict(color="black", marker="o", mew=1, markeredgecolor="black", markerfacecolor="white", markersize=3),
    )

    for (i, (group, data)), color in zip(enumerate(dfg), colors):
        y = data[col]
        n = len(y)
        jitter = np.random.uniform(-0.15, 0.15, size=n)
        x = i + jitter
        label = group

        if label_n:
            label += f"\n(N={n})"

        ax.scatter(x, y, color=color, **scatter_kwargs)

        if n >= min_n:
            ax.boxplot(y, positions=[i], labels=[label], **boxplot_kwargs)

    return ax
