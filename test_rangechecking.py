import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.station import MonitoringStation

#Data to test with
stations = build_station_list()

Test_station = [MonitoringStation(
        station_id=1,
        measure_id=10,
        label='test_station',
        coord=(float(0.1), float(0.1)),
        typical_range=(1.2, 1.5),
        river='River_test',
        town='test_town'),MonitoringStation(
        station_id=2,
        measure_id=20,
        label='test_station_2',
        coord=(float(50), float(0)),
        typical_range=(15, 2),
        river='River_test',
        town='test_town')]

def test_typical_range_consistent():
    assert Test_station[0].typical_range_consistent() == True
    assert Test_station[1].typical_range_consistent() == False