from cgi import test
from distutils.command.build import build
from turtle import update
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
import floodsystem.flood as flood
import numpy as np
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
        town='test_town'),
        MonitoringStation(
        station_id=3,
        measure_id=30,
        label='test_station_3',
        coord=(float(56), float(0)),
        typical_range=(1, 19),
        river='River_test',
        town='test_town')]

def test_stations_highest_rel_level():
    #assert len(flood.stations_highest_rel_level(stations, 10)) == 10
    Test_station[0].latest_level = 1.4
    Test_station[1].latest_level = 255
    assert flood.stations_highest_rel_level(Test_station, 1) == [('test_station', -0.10000000000000009)]


def test_stations_level_over_threshold():
    Test_station[0].latest_level = 10
    Test_station[1].latest_level = 255
    Test_station[2].latest_level = 255

    print(flood.stations_level_over_threshold(Test_station, 0.1)[:])
    print(flood.stations_level_over_threshold(Test_station, 0.1)[:])

    assert flood.stations_level_over_threshold(Test_station, 1.1)[0][1] > flood.stations_level_over_threshold(Test_station, 1.1)[1][1]



#Test for 2G

def test_assess_risk():
    stations = build_station_list()
    update_water_levels(stations)
    assert len(flood.assess_risk(stations)) > 0
    assert type(flood.assess_risk(stations)) == np.ndarray

test_assess_risk()