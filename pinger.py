import socket
import datetime
from urllib2 import urlopen, URLError, HTTPError
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from settings import *

def sendNotification(failed):
	""" Send an email notification
	:param failed: A list containing the failed sites
	"""
        message = "Failed sites:\n"

        for fail in failed:
                message += fail["site"] + " : " + fail["message"] + "\n"

        msg = MIMEText(message)
        msg["From"] = MAIL_SETTINGS["from"]
        msg["To"] = MAIL_SETTINGS["to"]
        msg["Subject"] = MAIL_SETTINGS["subject"]

        p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
        p.communicate(msg.as_string())


socket.setdefaulttimeout( PING_TIMEOUT )  # timeout in seconds

urls = URLS_TO_PING

failed = []

for url in urls:
    try :
        response = urlopen( url )
    except HTTPError as e:
        err = {
                "message" : 'The server couldn\'t fulfill the request. Reason: ' + str(e.code),
                "site" : url
        }

        failed.append(err)
    except URLError as e:
        err = {
                "message" : 'We failed to reach a server. Reason: ' + str(e.reason),
                "site" : url
        }

        failed.append(err)

if len(failed) > 0 :
        sendNotification(failed)
else :
	print datetime.datetime.now()
