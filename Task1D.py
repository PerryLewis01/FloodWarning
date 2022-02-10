# rivers_with_station(stations):
"""
function returns the names of the rivers with monitoring stations without repeats 
"""

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()
    print("\n***Rivers With Stations***\n")
    rivers = geo.rivers_with_station(stations)
    print(len(rivers) , "stations.")
    print("First 10 Rivers: ")
    print(rivers[:10])

    print("\n\n\n")

    riversStations = geo.stations_by_river(stations)
    print("Stations on the River Thames")
    print(riversStations['River Thames'])

    print("\n\n\n")

    riversStations = geo.stations_by_river(stations)
    print("Stations on the River Aire")
    print(riversStations['River Aire'])

    print("\n\n\n")

    riversStations = geo.stations_by_river(stations)
    print("Stations on the River Cam")
    print(riversStations['River Cam'])



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
