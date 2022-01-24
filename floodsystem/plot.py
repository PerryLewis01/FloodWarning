import matplotlib.pyplot as plt
from datetime import datetime, timedelta




def plot_water_levels(station, dates, levels):
    """plot_water_levels(station, dates, levels) input a Monitoring station a list of date objects and list of levels to plot
    
    This function does not plot.show()
    """
    # Plot
    plt.plot(dates, levels, label=station.name)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);

    
