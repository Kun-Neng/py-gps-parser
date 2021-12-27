# py-gps-parser
GPS parser module

Steps
-----
* Step 1: import pygpsparser module
```python
from gpsparser import GPSParser
```

* Step 2: prepare GPS sentences, e.g.,
```python
sentence_RMC = '$GNRMC,062357.00,A,2502.3376,N,12133.52528,E,0.132,,231221,,,A*68'
```

* Step 3: create GPSParser instance
```python
gps_parser = GPSParser(local_time_zone = 'Asia/Taipei')
```
> `local_time_zone`: set the local time zone for datetime conversion

* Step 4: get the RMC message
```python
if gps_parser.parse_NMEA(sentence_RMC) is True:
    print(f'local datetime: {gps_parser.local_datetime}')
    print(f'latlon in radian: {gps_parser.latlon_radian}')
```
