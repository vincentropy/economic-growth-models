from matplotlib import pyplot as plt  # type: ignore

TimeData = list[float]
TimeDataSpec = dict[str, TimeData]


def plot_time_data(
    time_data: TimeDataSpec,
    title: str | None = None,
    separate: bool = False,
    y_label: str | None = None,
    normalize_t0: bool = False,
) -> tuple[plt.Figure, list[plt.Axes]]:
    labels = list(time_data.keys())
    series = list(time_data.values())

    if normalize_t0:
        series = [[value / data[0] for value in data] for data in series]

    prop_cycle = plt.rcParams["axes.prop_cycle"]
    colors = [p["color"] for p in prop_cycle]

    if separate:
        n = len(series)
        height = max(2, 3 - 0.15 * n) * n
        fig, axes = plt.subplots(n, 1, sharex=True, figsize=(10, height))
        fig.supxlabel("Time Steps")
        if n == 1:
            axes = [axes]
        for i, (ax, label, data) in enumerate(zip(axes, labels, series)):
            ax.plot(data, label=label, color=colors[i % len(colors)])
            ax.legend()
            ax.set_ylabel(y_label if y_label else label)

    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.supxlabel("Time Steps")

        axes = [ax]
        for label, data in zip(labels, series):
            ax.plot(data, label=label)
        ax.set_ylabel(y_label if y_label else "Value")
        ax.legend()

    if title:
        fig.suptitle(title, fontsize=18)

    fig.tight_layout()
    return fig, axes
