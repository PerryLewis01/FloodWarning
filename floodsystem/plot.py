import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
from .analysis import polyfit
import numpy as np



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

    

def plot_water_level_with_fit(station, dates, levels, p):
    """plots water level data and best fit polynomial"""

    #check data exists
    if len(dates) == 0 or len(levels) == 0:
        pass    
    else:
        poly, d0 = polyfit(dates, levels, p)

        #format data
        dates = matplotlib.dates.date2num(dates) - d0    
        x1 = np.linspace(dates[0],dates[-1],30)

        #plot 
        plt.plot(dates, levels, '.')
        plt.plot(x1, poly(x1),"-m", label = "Fitted polynomial")
        plt.plot(x1, np.linspace(station.typical_range[0],station.typical_range[0],30),"-r", label="Typical Max/Min")
        plt.plot(x1, np.linspace(station.typical_range[1],station.typical_range[1],30),"-r")

        #add titles and labels

        plt.show()