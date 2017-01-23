import datetime
from ds1054z import DS1054Z
scope = DS1054Z('192.168.0.2')
print('Date now: %s' % datetime.datetime.now())
for i in range(1, 30):
    read_out = scope.get_channel_measurement(1, 'marea', 'CURRent')
print('Date now: %s' % datetime.datetime.now())
