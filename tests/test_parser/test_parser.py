from pygpsparser.gpsparser import GPSParser
from ..test_NMEA_message import *


def test_parse_NMEA():
    parser_1 = GPSParser()
    assert parser_1.parse_NMEA('') == False
    assert parser_1.parse_NMEA(invalid_RMC_1) == False
    assert parser_1.parse_NMEA(invalid_RMC_2) == False
    assert parser_1.parse_NMEA(normal_RMC) == True
    assert parser_1.parse_NMEA(normal_GGA) == True
    assert parser_1.parse_NMEA(initial_normal_sentence) == True
    assert len(parser_1.gsv_obj_map['GP']['satellites']) == 9
    assert len(parser_1.gsv_obj_map['GL']['satellites']) == 9

    parser_2 = GPSParser()
    assert parser_2.parse_NMEA(final_normal_sentence) == True
    assert len(parser_2.gsv_obj_map['GP']['satellites']) == 10

def test_parse_date():
    parser = GPSParser()
    assert parser.parse_date('231221') == '2021-12-23'

def test_parse_time():
    parser = GPSParser()
    assert parser.parse_time('062357.00') == '06:23:57'

def test_parse_datetime():
    parser = GPSParser()
    assert parser.parse_datetime(normal_RMC) == '2021-12-23 14:23:57+08:00'

def test_parse_latlon():
    parser = GPSParser()
    assert parser.parse_latlon(normal_RMC, 3, 5) == True
    assert parser.latitude_degree == 25
    assert parser.latitude_minute == 2.3376
    assert parser.longitude_degree == 121
    assert parser.longitude_minute == 33.52528
    assert parser.latlon_radian_RMC == [25.03896, 121.55875466666667]
    assert parser.parse_latlon(normal_GGA, 2, 4) == True

def test_create_satellite():
    parser = GPSParser()
    str_slice = single_GSV.split(',')
    for i_token in range(4):
        satellite = parser.create_satellite(str_slice, i_token)
        # print(satellite)
        if i_token == 0:
            assert satellite['ID'] == '03'
            assert satellite['Elevation'] == 17
            assert satellite['Azimuth'] == 304
            assert satellite['SNR'] is None
        elif i_token == 1:
            assert satellite['ID'] == '10'
            assert satellite['Elevation'] == 6
            assert satellite['Azimuth'] == 174
            assert satellite['SNR'] is None
        elif i_token == 2:
            assert satellite['ID'] == '16'
            assert satellite['Elevation'] == 35
            assert satellite['Azimuth'] == 231
            assert satellite['SNR'] == 34
        elif i_token == 3:
            assert satellite['ID'] == '22'
            assert satellite['Elevation'] == 25
            assert satellite['Azimuth'] == 281
            assert satellite['SNR'] == 26

def test_parse_satellites_in_view():
    parser = GPSParser()
    assert parser.parse_satellites_in_view(single_GSV) == True
