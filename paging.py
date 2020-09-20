# Using PagerDuty client library
from pdpyras import EventsAPISession

# AQI Notifier integration key
integration_key = input('Integration key? ')
session = EventsAPISession(integration_key)

dedup_key = session.trigger('AQI too high', 'local python script')
# Let the user resolve the session
