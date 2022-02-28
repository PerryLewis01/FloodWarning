# %%
import datetime
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood
import floodsystem.plot as plot

import matplotlib.pyplot as plt

def run():
    """Task 2E"""
    print("run starts")
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    noStations = 5

    # Station name to find
    station_list = flood.stations_highest_rel_level(stations, noStations)
         

    
    # Fetch data over past 10 days
    dt = 10
    for i in range(len(station_list)):
        dates, levels = fetch_measure_levels(
            station_list[i][0].measure_id, dt=datetime.timedelta(days=dt))

        plot.plot_water_levels(station_list[i][0], dates, levels)
    
    plt.title("5 current highest")
    plt.legend(loc="upper left")
    plt.xlim([datetime.datetime.utcnow() - datetime.timedelta(days=dt), datetime.datetime.utcnow()])
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    print("Showing Plot")
    plt.show()


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

# %%
