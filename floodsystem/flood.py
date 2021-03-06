"""Flood Submodule"""






#from curses.ascii import NUL
import string
from turtle import st
from unittest import skip
import numpy as np

from floodsystem.geo import stations_by_river
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


from floodsystem.stationdata import build_station_list, update_water_levels


def stations_highest_rel_level(stations, N):
    """stations_highest_rel_level(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    rel_levels = stations_level_over_threshold(stations, -50)

    return rel_levels[:N]


def stations_highest_rel_level_wrong(stations, N):
    """stations_highest_rel_level_wrong(stations, N) returns a list of N stations in which the water level is closest to the maximum"""
    difference = []
    if stations[0].latest_level == None:
        update_water_levels(stations)

    for station in stations:
        if station.typical_range_consistent():
            try:
                if (station.latest_level - station.typical_range[1]) < 50:
                    difference.append((station.name, (station.latest_level - station.typical_range[1])))

            except Exception:
                difference.append((station.name, -5000))
                # if station.latest_level == None
        else:
            difference.append((station.name, -5000))

    difference = sorted(difference, key=lambda x: -x[1])
    #print(difference)
    return difference[:N]



def stations_level_over_threshold(stations, tol):
    """returns a list of tuples containing (station, relative water level at the station) 
    for which the relative water level is over tol. tuples are sorted by relative level in descending order"""

    #update_water_levels(stations)

    #set up empty list
    stations_over_tol = []

    #iterate through all stations and check if relative level is over tol
    for station in stations:
        #print('tring if')
        if station.typical_range_consistent() and (station.relative_water_level() != None):
            #print("consistent", station)
            if (station.relative_water_level() > tol):
                #print('adding station' , station)
                stations_over_tol.append((station, station.relative_water_level()))
        else:
            pass
    
    #sort by relative level
    stations_over_tol = sorted(stations_over_tol, key = lambda x:-x[1])
    

    return stations_over_tol











import numpy as np

def assess_risk(stations):
    """assess_risk(stations), returns a (station.name, station risk) in order of risk """

    dtype = [('stationName', str), ('value', float)]
    #computing current level risk
    current_levels = np.array(stations_highest_rel_level_wrong(stations, len(stations)+1))
    
    #1m above max has a risk of 1, 0.4 m below max has risk of 0
    levelRisk = current_levels[:, 1].astype(float)
    levelRisk = (1)/(1.4)*(levelRisk + 0.4)
    levelRisk = np.array([[current_levels[i, 0].astype(str), levelRisk[i]] for i in range(len(levelRisk))])
    

    #relative level risk
    #relative level 1.5 risk 1, relative level 0 risk 0
    rellevels = np.array([[station.name, station.relative_water_level()/1.5] if station.relative_water_level() != None else [station.name, station.relative_water_level()] for station in stations])
    
    levelRisk = levelRisk[np.argsort(levelRisk[:,0])]
    rellevels = rellevels[np.argsort(rellevels[:,0])]

    #levelRisk = sorted(levelRisk, key=lambda x: x[0])
    #rellevels = sorted(rellevels, key=lambda x: x[0])
    #print(levelRisk.shape)
    #print(rellevels.shape)
    #print(len(stations))
    StationsAndRisk = np.empty((len(levelRisk),2), dtype=object)

    skipstationcounter = 0

    for i in range(len(levelRisk)):
        StationsAndRisk[i, 0] = levelRisk[i, 0]
        if (levelRisk[i,0] == rellevels[i+skipstationcounter,0]):
            if rellevels[i+skipstationcounter,1] != None:
                #print(levelRisk[i,1], rellevels[i,1])
                StationsAndRisk[i,1] = ((float(levelRisk[i,1]) + float(rellevels[i+skipstationcounter,1]))/2)
            else:
                StationsAndRisk[i,1] = (levelRisk[i,1])
        else:
            #print("ERROR!!! STATIONS dont match")
            #print(levelRisk[i,0], rellevels[i+skipstationcounter,0])
            #print("in position", i)

            StationsAndRisk[i,1] = levelRisk[i,1]
            skipstationcounter += 1

            while(levelRisk[i,0] != rellevels[i+skipstationcounter,0]):
                #print(levelRisk[i+skipstationcounter,0], rellevels[i,0])
                skipstationcounter += 1
            
    #output array generation
    output = np.empty((len(StationsAndRisk), 2), dtype=object)
    for i, value in enumerate(StationsAndRisk):
        output[i,0] = value[0]
        if float(value[1]) > 1:
            output[i,1] = "Severe"
        elif float(value[1]) > 0.7:
            output[i,1] = "High"
        elif float(value[1]) > 0.4:
            output[i,1] = "Moderate"
        else:
            output[i,1] = "Low"
    
    return(output)

    
    #print(StationsAndRisk)


    










