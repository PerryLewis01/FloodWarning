# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from .utils import sorted_by_key  # noqa

from .station import MonitoringStation


def stations_by_distance(stations, p):
    locations = np.array([station.coord for station in stations])
    # using haversine formula
    distanceToP = 2*6371000*np.arcsin(np.sqrt(np.sin((p[0] - locations[:,0])/2)**2 + np.cos(p[0]) * np.cos(locations[:,0])*np.sin((p[1] - locations[:,1])/2)**2))
    # using r as 6371km
    return distanceToP
    