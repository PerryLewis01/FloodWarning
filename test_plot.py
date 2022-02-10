from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import floodsystem.stationdata as stationdata
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy

def test_plot_water_level_with_fit():
    
    #create stations to test
    stations = build_station_list()
    stationdata.update_water_levels(stations)

    #Choose station to test
    for station in stations:
        if station.name == "Gaw Bridge":
            station_to_test = station

    #get data
    dates, levels = fetch_measure_levels(station_to_test.measure_id, dt=datetime.timedelta(days=4))
    poly, d0 = polyfit(dates, levels, 3)

    #run tests
    pass