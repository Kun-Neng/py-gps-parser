from main.parser import Parser


invalid_RMC_1 = 'GNRMC,062357.00,A,2451.76062,N,12115.52127,E,0.132,,231221,,,A*68'
invalid_RMC_2 = '$GNRMC,062357.00,A,2451.76062,N,12115.52127,E,0.132,,231221,,,A'
normal_RMC = '$GNRMC,062357.00,A,2451.76062,N,12115.52127,E,0.132,,231221,,,A*68'

initial_normal_message = \
'$GNRMC,055020.00,V,,,,,,,231221,,,N*60' \
'$GNVTG,,,,,,,,,N*2E' \
'$GNGGA,055020.00,,,,,0,00,99.99,,,,,,*7A' \
'$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E' \
'$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E' \
'$GPGSV,3,1,09,03,11,316,,10,19,180,,16,22,220,17,22,23,296,21*7B' \
'$GPGSV,3,2,09,25,23,039,26,26,61,239,34,29,28,081,,31,51,345,*79' \
'$GPGSV,3,3,09,32,70,096,*49' \
'$GLGSV,3,1,09,65,63,320,,66,05,333,,71,13,156,,72,62,164,*6B' \
'$GLGSV,3,2,09,74,20,031,,75,52,332,,76,29,260,,84,03,070,*6F' \
'$GLGSV,3,3,09,85,03,123,*52' \
'$GNGL'


def test_parse_NMEA():
    parser = Parser()
    assert parser.parse_NMEA('') == False
    assert parser.parse_NMEA(invalid_RMC_1) == False
    assert parser.parse_NMEA(invalid_RMC_2) == False
    # assert parser.parse_NMEA(normal_RMC) == True
    # assert parser.parse_NMEA(initial_normal_message) == True

def test_parse_date():
    parser = Parser()
    assert parser.parse_date('231221') == '2021-12-23'

def test_parse_time():
    parser = Parser()
    assert parser.parse_time('062357.00') == '06:23:57'

def test_parse_datetime():
    parser = Parser()
    assert parser.parse_datetime(normal_RMC) == '2021-12-23 14:23:57+08:00'

def test_parse_latlon():
    parser = Parser()
    assert parser.parse_latlon(normal_RMC, 3, 5) == True
    assert parser.latlon_radian == [24.862677, 121.25868783333334]
