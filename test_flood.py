from cgi import test
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
import floodsystem.flood as flood
#Data to test with
stations = build_station_list()
update_water_levels(stations)
Test_station = [MonitoringStation(
        station_id=1,
        measure_id=10,
        label='test_station',
        coord=(float(0.1), float(0.1)),
        typical_range=(1.2, 1.5),
        river='River_test',
        town='test_town'),
        MonitoringStation(
        station_id=2,
        measure_id=20,
        label='test_station_2',
        coord=(float(50), float(0)),
        typical_range=(15, 2),
        river='River_test',
        town='test_town')]

def test_stations_highest_rel_level():
    #assert len(flood.stations_highest_rel_level(stations, 10)) == 10
    Test_station[0].latest_level = 1.4
    Test_station[1].latest_level = 255
    assert flood.stations_highest_rel_level(Test_station, 1) == [('test_station', -0.10000000000000009)]

