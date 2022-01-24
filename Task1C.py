#Hello felix want to do this one?
#hi
#git add file
#git commit -m "comment"
#git push

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():
    """Requirements for Task 1C"""

    #build list of stations
    stations = build_station_list()

    #create list of stations within radius
    stations_in_r = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)

    #display list of stations
    print(stations_in_r)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()