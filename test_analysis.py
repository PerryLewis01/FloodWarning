from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import floodsystem.stationdata as stationdata
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy


def test_polyfit():

    #create stations to test
    stations = build_station_list()
    stationdata.update_water_levels(stations)

    for station in stations:
        if station.name == "Gaw Bridge":
            station_to_test = station

    dates, levels = fetch_measure_levels(station_to_test.measure_id, dt=datetime.timedelta(days=4))
    poly, d0 = polyfit(dates, levels, 3)

    #run tests
    assert d0 != None
    assert len(poly) != 0
    assert type(poly) == numpy.poly1d
    assert type(d0) == numpy.float64
    