"""Flood Submodule"""






from curses.ascii import NUL
import numpy as np
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation

from floodsystem.stationdata import build_station_list, update_water_levels


def stations_highest_rel_level(stations, N):
    """stations_highest_rel_level(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    difference = []
    update_water_levels(stations)

    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, station.latest_level - station.typical_range[1]))
            
            except Exception:
                pass
                #if station.latest_level == None


    difference = sorted(difference, key = lambda x:-x[1])

    return difference[:N]


