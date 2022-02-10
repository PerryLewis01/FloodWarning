

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""
    # Build list of stations
    stations = build_station_list()
    
    """for station in stations:
        if not station.typical_range_consistent():
            print("Error Found at:", station.name," with values:",  station.typical_range)
    """
    print(sorted(inconsistent_typical_range_stations(stations)))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
