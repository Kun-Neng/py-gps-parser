from main.parser import Parser


invalid_RMC_message_1 = f'GNRMC,060123.00,A,2451.75159,N,12115.52450,E,0.387,,271021,,,A*6E'
invalid_RMC_message_2 = f'$GNRMC,060123.00,A,2451.75159,N,12115.52450,E,0.387,,271021,,,A'
normal_RMC_message = f'$GNRMC,060123.00,A,2451.75159,N,12115.52450,E,0.387,,271021,,,A*6E'


def test_parse_NMEA():
    parser = Parser()
    assert parser.parse_NMEA('') == False
    assert parser.parse_NMEA(invalid_RMC_message_1) == False
    assert parser.parse_NMEA(invalid_RMC_message_2) == False
    assert parser.parse_NMEA(normal_RMC_message) == True
