##THIS IS A PLOTTING FUNCTION##
import matplotlib.pyplot as plt
"""
   Function for plotting simple graphs with 2 
   arguments ,change visual parameters accord
   ing to needs
"""
def plottingfunction(xAxisVector,yAxisVector,titleString,stringxAxis,stringyAxis,stringFileName):
    plt.figure(figsize=(8,6))
    plt.plot(xAxisVector,yAxisVector,color="blue",linewidth=4)
    plt.title(titleString,fontsize=14)
    plt.xlabel(stringxAxis, fontsize=14)
    plt.ylabel(stringyAxis,fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.grid(visible=True)
    plt.savefig(stringFileName,dpi=600)
    plt.show()
"""
   Function for plotting multiple signals, of differe
   nt types(line,scatter,stem)
   on the same main plot.
   Input-plot_multiple_signals((x_val,y_val,'line/scatter/stem'),title = 'title')
   add or change more plot types according to your needs
   EXAMPLE-
   plot_signals(
    (t, np.sin(t), 'line', 'Continuous Sine'),
    (t_disc, np.sin(t_disc), 'stem', 'Sampled Sine'),
    title='Continuous vs Sampled'
    )
"""
def plot_multiple_graphs(*signals, title='Graph'):
    n = len(signals)
    fig, axes = plt.subplots(n, 1, figsize=(10, 4 * n))
    
    if n == 1:
        axes = [axes]
    # MODIFY HERE FOR ADDING MORE GRAPHS
    
    for i, (t, y, plot_type, subplot_title) in enumerate(signals):
        ax = axes[i]
        if plot_type == 'line':
            ax.plot(t, y)
        elif plot_type == 'stem':
            ax.stem(t, y)
        elif plot_type == 'scatter':
            ax.scatter(t, y)
        ax.set_title(subplot_title)
        ax.grid(True)
    
    fig.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()
    
""" 
    Function for plotting with x and y axis cleanly
"""
def style_plot(ax=None, equal_aspect=False, grid=True, xlabel=None, ylabel=None):
    import matplotlib.pyplot as plt

    if ax is None:
        ax = plt.gca()

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    if grid:
        ax.grid(True, linestyle='--', alpha=0.5)

    if equal_aspect:
        ax.set_aspect('equal', adjustable='box')

    if xlabel:
        ax.set_xlabel(xlabel)

    if ylabel:
        ax.set_ylabel(ylabel)

    return ax
##END##
