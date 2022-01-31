"""Flood Warning System

returns either, "high" "moderate" or "low" risk of flooding

probability of flooding is computed via a range of inputs,
current level over the typical maximum, the higher the current
level the higher the assumed risk of flooding (if in flood flood level high)

relative level, if the level is relatively high a similar equation is used


predicted water level, using a polyfit for the past data predicting the future risk

"""

from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood


def run():
    """Task 2G"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    flood.assess_risk(stations)

    """
    flood_data = flood.assess_risk(stations)

    for data in flood_data:
        print(data[0], data[1], data [2])"""

run()