# rivers_with_station(stations):
"""
function returns the names of the rivers with monitoring stations without repeats 
"""

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():

    # Build list of stations
    stations = build_station_list()

    rivers = geo.rivers_with_station(stations)
    print(len(rivers) , "stations.")
    print(rivers[:10])
    
    riversStations = geo.stations_by_river(stations)
    print(riversStations['River Thames'])



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
