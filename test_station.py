# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town



def test_relative_water_level():

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

    #station with typical high
    Test_station[0].latest_level = 1.5

    assert MonitoringStation.relative_water_level(Test_station[0]) == 1

    #station with typical low
    Test_station[0].latest_level = 1.2

    assert MonitoringStation.relative_water_level(Test_station[0]) == 0

    assert MonitoringStation.relative_water_level(Test_station[1]) == None