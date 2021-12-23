class Parser:
    def __init__(self) -> None:
        self.is_GPS_normal = False

    def parse_NMEA(self, messages) -> bool:
        if messages == '':
            return False
        
        str_line_slice = messages.split('\n')
        if len(str_line_slice) == 0:
            return False

        flag_latlon_ready = False
        for one_line in str_line_slice:
            if len(one_line) == 0:
                continue

            if one_line[0] != '$':
                continue

            if (one_line.find("*") == -1):
                continue

            if (one_line.find('RMC') != -1):
                print("%v", one_line)
                flag_latlon_ready = True

        if flag_latlon_ready is True:
            self.is_GPS_normal = True
        
        return self.is_GPS_normal
