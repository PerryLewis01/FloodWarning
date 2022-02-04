

import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.station import MonitoringStation

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

def test_stations_by_distance():
    assert len(geo.stations_by_distance(stations, (0, 0))) > 0
    assert round(geo.stations_by_distance(Test_station, (0, 0))[0][2]) == 16

def test_rivers_with_stations():
    assert len(geo.rivers_with_station(stations)) > 0
    assert geo.rivers_with_station(Test_station) == ['River_test']

def test_stations_by_river():
    assert len(geo.stations_by_river(stations)) >0
    assert len(geo.stations_by_river(stations)['River Thames']) > 10
    assert geo.stations_by_river(Test_station) == {'River_test': ['test_station', 'test_station_2']}


def test_stations_within_radius():
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 0)) == 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 10)) > 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 500)) > len(geo.stations_within_radius(stations, 52.2053, 0.1218, 2))

def test_rivers_by_station_number():
    #Felix write your own tests
    pass