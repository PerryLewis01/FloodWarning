from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for i in stations_level_over_threshold(stations, 0.8):
        print("{}  {}".format(i[0].name, i[1]))

    if len(stations_level_over_threshold(stations, 0.8)) == 0 :
        print("No stations over tolerance")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
