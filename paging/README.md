# Pagerduty integration

## Why?
In September 2020, the wildfire smoke had gotten so bad where I lived that we couldn't always leave the windows open, and the air quality was changing by the hour. But it was also way too hot, so we needed to leave the windows open overnight. As a compromise, I made a PagerDuty integration to alert/wake me when the AQI got too high so I could close the windows.

## What
As currently written, this just makes a page when the AQI gets too bad. It uses the public PurpleAir API.

### Setup
- Go to https://developer.pagerduty.com/sign-up/ and make a PagerDuty developer account.
- Make a new app
- Add Events Integration to the app
- At the bottom, add a test service
- Note the Integration Key. You'll need that for the bot to work.
- Go to the test service. Make yourself perma-oncall, and configure your notification rules appropriately.

- Fire up the paging.py script, paste in your integration key when prompted, and you're all set!

