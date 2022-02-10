
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
import floodsystem.stationdata as stationdata
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy

import datetime
import numpy as np
import floodsystem.flood as flood
import floodsystem.plot as plot
import matplotlib.pyplot as plt

"""
def test_plot_water_level_with_fit():
    
    #create stations to test
    stations = build_station_list()
    update_water_levels(stations)

    #Choose station to test
    for station in stations:
        if station.name == "Gaw Bridge":
            station_to_test = station

    #get data
    dates, levels = fetch_measure_levels(station_to_test.measure_id, dt=datetime.timedelta(days=4))
    poly, d0 = polyfit(dates, levels, 3)

    #run tests
    pass
"""

def test_plot_water_levels():

    stations = build_station_list()
    update_water_levels(stations)
    dates = np.empty(5, dtype=object)
    levels = np.empty(5, dtype=object)
    dt = 10
    for i in range(5):
        dates[i], levels[i] = fetch_measure_levels(
            stations[i].measure_id, dt=datetime.timedelta(days=dt))

        plot_water_levels(stations[i], dates[i], levels[i])

    assert plt.show() == None

test_plot_water_levels()