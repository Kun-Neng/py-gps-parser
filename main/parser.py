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

            if (one_line.find('*') == -1):
                continue

            if (one_line.find('RMC') != -1):
                # print(one_line)
                self.parse_datetime(one_line)
                flag_latlon_ready = True

        if flag_latlon_ready is True:
            self.is_GPS_normal = True
        
        return self.is_GPS_normal
    
    def parse_date(self, date_token) -> str:
        # UTC Date format ddmmyy
        year = int('20' + date_token[4:6])
        month = int(date_token[2:4])
        day = int(date_token[0:2])

        month_str = f'0{month}' if month < 10 else f'{month}'
        day_str = f'0{day}' if day < 10 else f'{day}'
        # print(f'{year}-{month_str}-{day_str}')

        return f'{year}-{month_str}-{day_str}'
    
    def parse_time(self, time_token) -> str:
        # UTC time format hhmmss.sss (000000.000 ~ 235959.999)
        hour = int(time_token[:2])
        minute = int(time_token[2:4])
        second = int(time_token[4:6])
        # msec = int(time_token[7:9])
        # nsec = 1000 * msec

        hour_str = f'0{hour}' if hour < 10 else f'{hour}'
        minute_str = f'0{minute}' if minute < 10 else f'{minute}'
        second_str = f'0{second}' if second < 10 else f'{second}'
        # print(f'{hour_str}:{minute_str}:{second_str}')

        return f'{hour_str}:{minute_str}:{second_str}'
    
    def parse_datetime(self, one_line):
        str_slice = one_line.split(',')

        time_token = str_slice[1]
        date_token = str_slice[9]

        if len(date_token) < 6:
            return None

        time_string = self.parse_date(date_token) + ' ' + self.parse_time(time_token)
        print(time_string)
