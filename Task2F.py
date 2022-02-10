from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation

def run():
    """Task 2F"""

    #create list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #get highest 5 stations
    stations_to_plot = (stations_level_over_threshold(stations,0.1))[0:4]

    count = 0

    for item in stations_to_plot:
        #Find how to call measure id
        station = item[0]
        #print(station)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)         
        count += 1
        if count == 5:
            break
    run()




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()