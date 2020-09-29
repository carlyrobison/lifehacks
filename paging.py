import time
# Using PagerDuty client library
from pdpyras import EventsAPISession
# Use this helpful Purple Air API client
from purpleair.sensor import Sensor

# AQI Notifier integration key


def trigger_event(session, aqi):
	dedup_key = session.trigger('AQI ' + str(aqi) + ' TOO HIGH', 'local python script')
	# Let the user resolve the session
	return dedup_key

# Sensors nearby
sensor_list = [64729, 35809, 65895, 37621]
# known not working noisebridge sensor: 16915

def get_aqi(sensor_ids):
	pm25s = []
	for s in sensor_ids:
		try:
			sd = Sensor(s).parent.as_dict()
			# print(sd['statistics']['10min_avg'], '\n')
			pm25s.append(sd['statistics']['10min_avg'])
		except ValueError as err:
			print("Error:", err)


	pm25s.sort() # Four values this is quick
	if len(pm25s) > 2:
		# Omit the first and last two values, average, for the PM2.5 near me
		pm25s = pm25s[1:-1]
		my_pm25 = sum(pm25s) / len(pm25s)
	elif len(pm25s) == 1:
		# just take the value
		my_pm25 = pm25s[0]
	else:
		# kinda panic, alert on bad sensor data
		return 503 # like http.cat/503

	my_aqi = aqiFromPM(my_pm25)

	# print("My AQI:", my_aqi)
	return my_aqi


'''                                  AQI

AQI from PM2.5 number
Good                              0 - 50         0.0 - 15.0         0.0 – 12.0
Moderate                        51 - 100           >15.0 - 40        12.1 – 35.4
Unhealthy for Sensitive Groups   101 – 150     >40 – 65          35.5 – 55.4
Unhealthy                                 151 – 200         > 65 – 150       55.5 – 150.4
Very Unhealthy                    201 – 300 > 150 – 250     150.5 – 250.4
Hazardous                                 301 – 400         > 250 – 350     250.5 – 350.4
Hazardous                                 401 – 500         > 350 – 500     350.5 – 500
'''
def aqiFromPM(pm):
    if (pm < 0): return pm
    if (pm > 1000): return "-"

    if (pm > 350.5):
      return calcAQI(pm, 500, 401, 500, 350.5)
    if (pm > 250.5):
      return calcAQI(pm, 400, 301, 350.4, 250.5)
    if (pm > 150.5):
      return calcAQI(pm, 300, 201, 250.4, 150.5)
    if (pm > 55.5):
      return calcAQI(pm, 200, 151, 150.4, 55.5)
    if (pm > 35.5):
      return calcAQI(pm, 150, 101, 55.4, 35.5)
    if (pm > 12.1):
      return calcAQI(pm, 100, 51, 35.4, 12.1)
    if (pm >= 0):
      return calcAQI(pm, 50, 0, 12, 0)

    return "-"

def calcAQI(Cp, Ih, Il, BPh, BPl):
	a = (Ih - Il)
	b = (BPh - BPl)
	c = (Cp - BPl)
	return round((a/b) * c + Il)

dedup_key = None

alert_threshold = int(input('Alert threshold? '))
resolve_threshold = int(input('Resolve threshold? '))
integration_key = input('Integration key? ')
session = EventsAPISession(integration_key)
while True:
	aqi = get_aqi(sensor_list)
	print(time.ctime(), "\tAQI:", aqi)
	if dedup_key is not None and aqi < resolve_threshold:
		session.resolve(dedup_key)
		dedup_key = None
		print("Resolving because of low AQI")
	elif dedup_key is None and aqi > alert_threshold:
		print("Alerting because of high AQI")
		dedup_key = trigger_event(session, aqi)
		print("Made event with dedup key", dedup_key)
	time.sleep(300) # Sleep about 5 minutes
