import pandas as pd
import seaborn as sns

def clear_barplot(
    ax,
    percent=0,
    vertical=True,
    plot_title="",
    pad_top=13,
    pad_bottom=2,
    plot_xlabel="",
    plot_ylabel="",
    title_color="#045c6b",
    legend_visibility=False,
):

    ax.set(xlabel=plot_xlabel, ylabel=plot_ylabel)
    ax.set_title(plot_title, color=title_color, fontsize=14)
    ax.tick_params(
        axis="both",
        which="both",
        length=0,
    )
    
    # Frames
    if not legend_visibility:
        ax.legend([],frameon=legend_visibility)
    
    if vertical:
        ax.set_yticklabels([])
        sns.despine(left=True)
    else:
        ax.set_xticklabels([])
        sns.despine(bottom=True)

    # Plot on top of the bars
    for c in ax.containers:
        ax.bar_label(c, padding=pad_top, color="black", fontsize=10.5)
    if percent != 0:
        ax.bar_label(
            ax.containers[0],
            padding=pad_bottom,
            labels=percent,
            color="black",
            fontsize=9,
        )

def create_countplot(df, ax, col, palette=["grey", "tab:blue"], percent=0):
    sns.countplot(
        df[col],
        hue=df["TravelInsurance"],
        palette=palette,
        alpha=0.7,
        ax=ax,
    )

    ax.legend(["No", "Yes"], title="Purchased Travel Insurance")

    # Find percentages
    if percent == 0:
        percentage = round(
            100
            * df.groupby([col, "TravelInsurance"]).size()
            / sum(df.groupby([col, "TravelInsurance"]).size()),
            1,
        ).tolist()
        percentage = [f"({percentage[i]}%)" for i in [0, 2, 1, 3]]
    else:
        percentage = percent

    # Add percentages to the bars using bar_label
    for p, label in zip(ax.patches, percentage):
        ax.annotate(
            label,
            (p.get_x() + p.get_width() / 2.0, p.get_height() - 70),
            ha="center",
            va="bottom",
        )