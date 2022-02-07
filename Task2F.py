from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Task 2F"""

    #create list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #get highest 5 stations
    stations_to_plot = stations_highest_rel_level(stations, 5)

    #check there are actually 5 stations 
    while len(stations_to_plot) > 5:
        #remove last entry
        stations_to_plot.pop()

    for item in stations_to_plot:                
        station = item[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels,4) 

    run()




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()