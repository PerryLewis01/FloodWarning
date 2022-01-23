from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
import numpy as np

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))
    
    #locations = np.array([station.coord for station in stations])
    #clearprint(locations)

    dist = geo.stations_by_distance(stations, (0,0))
    for i in dist:
        print(i)



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
