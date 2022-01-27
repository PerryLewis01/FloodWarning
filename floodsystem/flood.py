"""Flood Submodule"""






#from curses.ascii import NUL
import numpy as np
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


from floodsystem.stationdata import build_station_list, update_water_levels


def stations_highest_rel_level(stations, N):
    """stations_highest_rel_level(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    difference = []
    if stations[0].latest_level == None:
        update_water_levels(stations)

    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, (station.latest_level - station.typical_range[1])))

            except Exception:
                pass
                # if station.latest_level == None

    difference = sorted(difference, key=lambda x: -x[1])
    #print(difference)
    return difference[:N]



def stations_level_over_threshold(stations, tol):
    """returns a list of tuples containing (station, relative water level at the station) 
    for which the relative water level is over tol. tuples are sorted by relative level in descending order"""

    update_water_levels(stations)

    #set up empty list
    stations_over_tol = []

    #iterate through all stations and check if relative level is over tol
    for station in stations:
        try:
            #print('tring if')
            if (station.relative_water_level() > tol):
                    #print('adding station')
                    stations_over_tol.append((station.name, station.relative_water_level()))
        except Exception:
            #print('failed to add')
            pass

    #sort by relative level
    stations_over_tol = sorted(stations_over_tol, key = lambda x:-x[1])
    
    return stations_over_tol
