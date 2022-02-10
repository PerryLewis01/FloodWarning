from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))
    
    #locations = np.array([station.coord for station in stations])
    #print(locations)

    dist = geo.stations_by_distance(stations, (52.2053,0.1218))
    for i in range(10):
        print(dist[i][0].name, dist[i][1])
        

    #print(dist[:10])



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
