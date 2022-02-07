# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from curses.ascii import NUL
import numpy as np
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


def stations_by_distance(stations, p):
    """stations_by_distance(stations, p) where p is the location (lat, long) and stations is a list of stations, will return the name town and distance from p in an list of tuples"""
    locations = np.array([station.coord for station in stations])
    
    # using haversine formula
    # using r as 6371km, numpy uses radians so all angles must be converted from degrees before calculation

    distanceToP = 2 * 6371 * np.arcsin(
        np.sqrt(
            (np.sin((np.deg2rad(p[0] - locations[:,0]))/2))**2 + np.cos(np.deg2rad(locations[:,0])) * np.cos(np.deg2rad(p[0])) * (np.sin((np.deg2rad(p[1] - locations[:,1]))/2))**2
        )
    )
    
    #now sort via distance with names and county
    distanceandTown = sorted([(station, distanceToP[i]) for i, station in enumerate(stations)], key = lambda x:x[1])
    return distanceandTown


def rivers_with_station(stations):
    """rivers_with_station(stations) returns a sorted list of the rivers stations are on without repeats"""
    stationRivers = set()
    for station in stations:
        stationRivers.add(station.river)
    stationRivers = sorted(stationRivers)
    return stationRivers

def stations_by_river(stations):
    """stations_by_river(stations) returns dictionary of rivers (the key) and a sorted list of stations on that river"""
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
        



def stations_within_radius(stations, centre, r):
    """stations_within_radius(stations, centre, r) returns an alphabetical list of the stations within radius r of the coordinate, centre"""
    # Calls stations from previous function
    stations_dist = stations_by_distance(stations, centre)

    #create list of stations in radius
    stations_in_r = []

    #adds stations to stations_in_r
    for i, stations in enumerate(stations):
        if stations_dist[i][1] < r:
            stations_in_r.append(stations_dist[i][0].name)
        else:
            break
    
    #sort stations_in_r alphabetically
    stations_in_r.sort()
    
    return stations_in_r



def rivers_by_station_number(stations, N):
    """rivers_by_station_number returns a list of tuples(river name, number of stations) sorted by number of stations for the first N rivers"""

    #use dictionary from stations_by_river(stations)
    stations_by_riv = stations_by_river(stations) 

    #create empty list of rivers
    rivers_stations = []

    #add number of stations to list
    for key, value in stations_by_riv.items():
        rivers_stations.append((key, len(value)))

    #sort list by number of stations
    rivers_stations = sorted(rivers_stations, key = lambda x:-x[1])  

    output = rivers_stations[:N]

    #sort what happens if nth entry has equal sumber of stations
    list_complete = False
    while list_complete == False:
        if rivers_stations[-N][1] == rivers_stations[-(N+1)]:
            output.append(rivers_stations[-(N+1)])
            
        else:
            list_complete = True

    return output