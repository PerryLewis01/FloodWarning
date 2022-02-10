# rivers_with_station(stations):
"""
function returns the names of the rivers with monitoring stations without repeats 
"""

from floodsystem.stationdata import build_station_list, update_water_levels

import floodsystem.flood as flood


def run():
    """Requirements for Task 2C"""
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    inflood = flood.stations_highest_rel_level(stations, 10)
    for data in inflood:
        print(data[0], data[1])
    





if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()