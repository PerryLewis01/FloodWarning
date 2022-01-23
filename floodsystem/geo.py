# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from curses.ascii import NUL
import numpy as np
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


def stations_by_distance(stations, p):
    locations = np.array([station.coord for station in stations])
    
    # using haversine formula
    # using r as 6371km, numpy uses radians so all angles must be converted from degrees before calculation

    distanceToP = 2 * 6371 * np.arcsin(
        np.sqrt(
            (np.sin((np.deg2rad(p[0] - locations[:,0]))/2))**2 + np.cos(np.deg2rad(locations[:,0])) * np.cos(np.deg2rad(p[0])) * (np.sin((np.deg2rad(p[1] - locations[:,1]))/2))**2
        )
    )
    
    #now sort via distance with names and county
    distanceandTown = sorted([(station.name, station.town, distanceToP[i]) for i, station in enumerate(stations)], key = lambda x:x[2])
    return distanceandTown


def rivers_with_station(stations):
    stationRivers = set()
    for station in stations:
        stationRivers.add(station.river)
    stationRivers = sorted(stationRivers)
    return stationRivers

def stations_by_river(stations):
    stationRivers = set(rivers_with_station(stations)) #sligtly quicker then for sorting later
    riversStations = {} #empty dictionary
    for station in stations:
        if not station.river in riversStations:
            riversStations.update({station.river: list([station.name])}) 
            #add item to dictionary if it doesn't exist and create list with it
        else:
            riversStations[station.river] = list(riversStations[station.river]) + [station.name]
            #if it does exist add the station name to the list that already exists
    
    for station in stationRivers:
        riversStations[station] = sorted(riversStations[station])
        #sort the names in the lists for all rivers

    return riversStations
        
        