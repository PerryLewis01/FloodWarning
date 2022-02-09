"""Flood Submodule"""






#from curses.ascii import NUL
import string
from turtle import st
import numpy as np

from floodsystem.geo import stations_by_river
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











import numpy as np

def assess_risk(stations):
    """assess_risk(stations), returns a (station.name, station.level, station risk) in order of risk """

    dtype = [('stationName', 'S10'), ('value', float)]
    #computing current level risk
    current_levels = np.array(stations_highest_rel_level(stations, len(stations)))
    
    #1m above max has a risk of 1, 0.4 m below max has risk of 0
    levelRisk = current_levels[:, 1].astype(float)
    levelRisk = (1)/(1.4)*(levelRisk + 0.4)
    levelRisk = np.array([[current_levels[i, 0].astype(str), levelRisk[i].astype(float)] for i in range(len(levelRisk))], dtype=dtype)
    

    #relative level risk
    #relative level 1.5 risk 1, relative level 0 risk 0
    rellevels = np.array([[station.name, station.relative_water_level()/1.5] if station.relative_water_level() != None else [station.name, station.relative_water_level()] for station in stations])
    
    levelRisk = levelRisk[np.argsort(levelRisk[:,0])]
    rellevels = rellevels[np.argsort(rellevels[:,0])]

    #levelRisk = sorted(levelRisk, key=lambda x: x[0])
    #rellevels = sorted(rellevels, key=lambda x: x[0])
    print(levelRisk[:,1])
    print(rellevels[:,1])
    StationsAndRisk = np.array([[levelRisk[i, 0], ((levelRisk[i,1] + rellevels[i,1])/2)]  if rellevels[i,1] != None else [levelRisk[i, 0], levelRisk[i,1]] for i in range(len(stations)) ])

    print(StationsAndRisk)


    










