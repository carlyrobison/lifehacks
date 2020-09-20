import time
# Using PagerDuty client library
from pdpyras import EventsAPISession

# AQI Notifier integration key
integration_key = input('Integration key? ')
session = EventsAPISession(integration_key)

def trigger_event(session, aqi):
	dedup_key = session.trigger('AQI ' + str(aqi) + ' TOO HIGH', 'local python script')
	# Let the user resolve the session
	return dedup_key

def get_aqi():
	pass


while True:
	print(time.ctime())
	# time.sleep(60) # Sleep about 60 seconds
	time.sleep(1)
