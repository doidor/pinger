Simple site pinger
===

There're lots of online services which help you ping your sites and get a report when one is down. AFAIK none of them is free. This is a super simple tool to help you check your websites and report back if there are some issues. If everything goes well, it will output the current time so you can store it in a log file or something.

### Requirements

1. You need to have sendmail installed
2. Python3 (for urllib2)

### Setup

1. Clone the repo
2. Update the settings.py file with your data
3. python pinger.py
4. ???
5. PROFIT!!

I run this tool as a cron job once every 5 minutes. This is how you set it up:

	*/5 * * * * /usr/bin/python /<path_to_your_pinger>/pinger.py > pinger_log

I'm not a super great python dev so feel free to ping me if you find something wrong.
