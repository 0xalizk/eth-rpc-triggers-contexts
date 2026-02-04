#!/usr/bin/env python3
"""
Based on https://github.com/0xalizk/mopro-benchmarks/blob/main/src/main.py
Generate RPC call distribution bar plot from aggregate statistics.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
from matplotlib import rcParams
import numpy as np
import os

# Register Ubuntu font
ubuntu_regular = '/tmp/Ubuntu-Regular.ttf'
ubuntu_bold = '/tmp/Ubuntu-Bold.ttf'

if os.path.exists(ubuntu_regular):
    fm.fontManager.addfont(ubuntu_regular)
if os.path.exists(ubuntu_bold):
    fm.fontManager.addfont(ubuntu_bold)

# Create font properties
ubuntu_font = fm.FontProperties(fname=ubuntu_regular)
ubuntu_bold_font = fm.FontProperties(fname=ubuntu_bold)

def update_rcParams():
    rcParams['savefig.pad_inches'] = .2
    rcParams['axes.grid'] = True
    rcParams['axes.titlesize'] = 36
    rcParams['axes.labelsize'] = 28
    rcParams['font.family'] = ubuntu_font.get_name()
    rcParams['font.sans-serif'] = [ubuntu_font.get_name(), 'Helvetica', 'Arial']
    rcParams['figure.titleweight'] = 'bold'
    rcParams['figure.titlesize'] = 45
    rcParams['figure.subplot.hspace'] = 0.9
    rcParams['figure.subplot.wspace'] = 0.1
    rcParams['figure.subplot.left'] = 0.1
    rcParams['figure.subplot.right'] = 0.9
    rcParams['figure.subplot.top'] = 0.90
    rcParams['figure.subplot.bottom'] = 0.1
    rcParams['grid.alpha'] = 1
    rcParams['grid.color'] = '#b3cccc'
    rcParams['grid.linestyle'] = 'solid'
    rcParams['grid.linewidth'] = 0.5
    rcParams['axes.grid.axis'] = 'y'
    rcParams['axes.grid.which'] = 'both'
    rcParams['xtick.color'] = 'black'
    rcParams['xtick.direction'] = 'out'
    rcParams['xtick.labelsize'] = 22
    rcParams['xtick.major.pad'] = 1.0
    rcParams['xtick.major.size'] = 10.0
    rcParams['xtick.major.width'] = 1.0
    rcParams['xtick.minor.pad'] = 1.0
    rcParams['xtick.minor.size'] = 5.0
    rcParams['xtick.minor.width'] = 1
    rcParams['xtick.minor.visible'] = False
    rcParams['ytick.color'] = 'black'
    rcParams['ytick.direction'] = 'out'
    rcParams['ytick.labelsize'] = 22
    rcParams['ytick.major.pad'] = 4.0
    rcParams['ytick.major.size'] = 10.0
    rcParams['ytick.major.width'] = 1.0
    rcParams['ytick.minor.pad'] = 4.0
    rcParams['ytick.minor.size'] = 5
    rcParams['ytick.minor.width'] = 1
    rcParams['ytick.minor.visible'] = False
    rcParams['legend.borderaxespad'] = 0.5
    rcParams['legend.borderpad'] = 0.4
    rcParams['legend.columnspacing'] = 2.0
    rcParams['legend.edgecolor'] = 'inherit'
    rcParams['legend.facecolor'] = 'inherit'
    rcParams['legend.fancybox'] = False
    rcParams['legend.fontsize'] = 30
    rcParams['legend.framealpha'] = 1
    rcParams['legend.frameon'] = False
    rcParams['legend.handleheight'] = 0.7
    rcParams['legend.handlelength'] = 2.0
    rcParams['legend.handletextpad'] = 0.8
    rcParams['legend.labelspacing'] = 0.5
    rcParams['legend.markerscale'] = 1.0
    rcParams['legend.numpoints'] = 2
    rcParams['legend.scatterpoints'] = 3
    rcParams['legend.shadow'] = False


def beautify_ax(ax, colors, labels, groups, title, x_label, y_label, xticks):
    ax.set_title(title, y=1.26, pad=50, fontsize=56, fontproperties=ubuntu_bold_font)
    ax.tick_params(labeltop=False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.yaxis.set_minor_locator(ticker.NullLocator())
    ax.grid(True, axis='y', which='major')
    ax.grid(False, axis='y', which='minor')
    ax.set_xticks(xticks)
    ax.set_xticklabels(groups, fontsize=26, fontproperties=ubuntu_font)  # Increased x-axis label size 3x
    ax.set_xlabel(x_label, fontsize=22, fontproperties=ubuntu_font)
    ax.set_ylabel(y_label, fontsize=15, fontproperties=ubuntu_font)

    # Apply Ubuntu font to tick labels with consistent size for y-axis
    for label in ax.get_xticklabels():
        label.set_fontproperties(ubuntu_font)
        label.set_fontsize(18)

    # Set y-axis tick labels with same size on both sides
    y_tick_fontsize = 18
    for label in ax.yaxis.get_ticklabels(which='both'):
        label.set_fontproperties(ubuntu_font)
        label.set_fontsize(y_tick_fontsize)

    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom='on', labeltop=False)
    ax.tick_params(axis='y', which='both', left='on', right='on', labelleft='on', labelright='on',
                   labelsize=y_tick_fontsize)

    # Ensure right y-axis labels have the same size
    ax.tick_params(axis='y', which='both', labelsize=y_tick_fontsize)

    # Create larger legend font
    legend_font = fm.FontProperties(fname=ubuntu_regular, size=20)

    patches = []
    for c, l in zip(colors, labels):
        patches.append(mpatches.Patch(color=c, label=l))
    legend = ax.legend(
        handles=patches,
        loc='upper center',
        bbox_to_anchor=(0.5, 1.20),
        frameon=True,
        ncol=4,
        prop=legend_font,
        labelspacing=0.6,
        handlelength=2.2,
        handletextpad=0.5,
        columnspacing=1.5,
        borderpad=1.0,
    )
    frame = legend.get_frame()
    frame.set_linewidth(0)
    frame.set_facecolor('white')


def main():
    update_rcParams()

    # Data extracted from aggregate files
    # Categories: State, Receipts, Transactions, Blocks
    # State: eth_getBalance, eth_getStorageAt, eth_getCode, eth_call
    # Receipts: eth_getTransactionReceipt, eth_getLogsANY (eth_getLogs + eth_getFilterLogs + eth_getFilterChanges)
    # Transactions: eth_getTransactionCount, eth_getBlockTransactionCountByHash, eth_getBlockTransactionCountByNumber,
    #               eth_getTransactionByHash, eth_getTransactionByBlockHashAndIndex, eth_getTransactionByBlockNumberAndIndex
    # Blocks: eth_getBlockByHash, eth_getBlockByNumber

    codebases = ['Aave Frontend', 'Helios', 'Rotki', 'Kohaku', 'Zerion Frontend\n(portfolio)']
    categories = ['State', 'Receipts', 'Transactions', 'Blocks']

    # Computed from aggregate files:
    # Aave: State=1+0+3+5=9, Receipts=33+0=33, Transactions=0+0+0+1+0+0=1, Blocks=1+1=2
    # Helios: State=14+13+14+12=53, Receipts=20+39=59, Transactions=14+10+10+15+14+14=77, Blocks=13+15=28
    # Rotki: State=2+0+3+3=8, Receipts=2+2=4, Transactions=3+0+0+3+0+0=6, Blocks=0+3=3
    # Kohaku: State=0+0+7+5=12, Receipts=5+1=6, Transactions=4+0+0+2+0+0=6, Blocks=0+5=5
    # Zerion: State=1+1+2+5=9, Receipts=4+3=7, Transactions=2+1+1+3+1+1=9, Blocks=1+4=5

    data = {
        'State':        [9,  53, 8,  12, 9],
        'Receipts':     [33, 59, 4,  6,  7],
        'Transactions': [1,  77, 6,  6,  9],
        'Blocks':       [2,  28, 3,  5,  5],
    }

    # Colors - distinct, colorblind-friendly palette
    colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B3']  # Blue, Green, Red, Purple

    x = np.arange(len(codebases))
    width = 0.18
    multiplier = 0

    fig, ax = plt.subplots(figsize=(14, 9))

    for category, color in zip(categories, colors):
        offset = width * multiplier
        bars = ax.bar(x + offset, data[category], width, label=category, color=color, edgecolor='white', linewidth=0.5)

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}',
                           xy=(bar.get_x() + bar.get_width() / 2, height),
                           xytext=(0, 3),
                           textcoords="offset points",
                           ha='center', va='bottom',
                           fontsize=11, fontweight='bold',
                           fontproperties=ubuntu_font)
        multiplier += 1

    # Center the x-ticks
    xticks = x + width * 1.5

    beautify_ax(
        ax=ax,
        colors=colors,
        labels=categories,
        groups=codebases,
        title='RPC Call Distribution',
        x_label='Context',
        y_label='No. RPC call triggers touching state, receipts, ..',
        xticks=xticks
    )

    # Add legend explanation text on the right side
    # Create font for code (Courier New)
    code_font = fm.FontProperties(family='Courier New', size=8)
    plus_font = fm.FontProperties(fname=ubuntu_regular, size=9)

    # Helper function to render code tokens with individual grey backgrounds
    def render_code_line(ax, x, y, tokens, transform):
        """Render a line of code tokens, each with its own grey background, separated by +"""
        current_x = x
        for i, token in enumerate(tokens):
            # Add the code token with grey background
            txt = ax.text(current_x, y, token, transform=transform,
                         fontproperties=code_font, fontsize=8,
                         ha='left', va='top', color='white',
                         bbox=dict(boxstyle='round,pad=0.2', facecolor='#555555', edgecolor='none'))

            # Get the width of the text to position the next element
            renderer = fig.canvas.get_renderer()
            bbox = txt.get_window_extent(renderer=renderer)
            bbox_axes = bbox.transformed(ax.transAxes.inverted())
            current_x = bbox_axes.x1 + 0.005  # Small gap

            # Add "+" between tokens (except after the last one)
            if i < len(tokens) - 1:
                # Get the height of the token box to center the "+"
                token_bbox = txt.get_window_extent(renderer=renderer)
                token_bbox_axes = token_bbox.transformed(ax.transAxes.inverted())
                plus_y = (token_bbox_axes.y0 + token_bbox_axes.y1) / 2  # Vertical center

                plus_txt = ax.text(current_x, plus_y, " + ", transform=transform,
                                   fontproperties=plus_font, fontsize=9,
                                   ha='left', va='center', color='black')
                bbox = plus_txt.get_window_extent(renderer=renderer)
                bbox_axes = bbox.transformed(ax.transAxes.inverted())
                current_x = bbox_axes.x1

    # Data: label and list of code tokens for each line
    lines_data = [
        ("State:", ["getBalance", "getStorageAt", "getCode", "call"]),
        ("Receipts:", ["getTxReceipt", "getLogs", "getFilterLogs", "getFilterChanges"]),
        ("Transactions:", ["getTxCount", "getBlockTxCountBy{Hash,Number}", "getTxByBlock{Hash,Number}AndIndex"]),
        ("Blocks:", ["getBlockByHash", "getBlockByNumber"]),
    ]

    label_x = 0.40
    code_x = 0.52
    y_positions = [0.96, 0.90, 0.84, 0.78]  # Compact vertical spacing

    for i, (label, tokens) in enumerate(lines_data):
        y = y_positions[i]

        # Bold label
        ax.text(label_x, y, label, transform=ax.transAxes,
                fontproperties=ubuntu_bold_font, fontsize=10,
                ha='left', va='top', color='black')

        # Code tokens with individual grey backgrounds
        render_code_line(ax, code_x, y, tokens, ax.transAxes)

    plt.tight_layout()
    plt.savefig('rpc-dist.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("Saved plot to rpc-dist.png")


if __name__ == '__main__':
    main()
