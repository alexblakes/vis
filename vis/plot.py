import matplotlib.pyplot as plt
import numpy as np


def boxplot(
    dfg,
    col,
    colors,
    ax=None,
    label_n=True,
    min_n_box=5,
    min_n_alpha=25,
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
        dict(
            color="black",
            marker="o",
            mew=1,
            markeredgecolor="black",
            markerfacecolor="white",
            markersize=3,
        ),
    )

    for (i, (group, data)), color in zip(enumerate(dfg), colors):
        y = data[col]
        n = len(y)
        jitter = np.random.uniform(-0.15, 0.15, size=n)
        x = i + jitter
        label = group

        if label_n:
            label += f"\n(N={n})"

        if n < min_n_alpha:
            scatter_kwargs.update(alpha=1)

        ax.scatter(x, y, color=color, **scatter_kwargs)

        if n < min_n_box:
            # Plot an empty boxplot
            ax.boxplot(
                y,
                positions=[i],
                labels=[label],
                showbox=False,
                showcaps=False,
                showmeans=False,
                whiskerprops=dict(linestyle="None"),
                medianprops=dict(linestyle="None"),
            )
        else:
            ax.boxplot(y, positions=[i], labels=[label], **boxplot_kwargs)

    return ax
