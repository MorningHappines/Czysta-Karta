#!/usr/bin/env python3
import os
import requests

os.remove('C:\Users\User Name\AppData\Local\Google\Chrome\User Data\Default\History')
path.exists('C:\Users\User Name\AppData\Local\Google\Chrome\User Data\Default\History')

app_key = "YOUR API KEY"
controler = "message"
action = "send"
url = "https://justsend.pl/api/rest/%s/%s/%s" % (controler, action, app_key)

to = "48XXXXXXXXX"
message = "Historia skasowana!"

import urllib
message = urllib.parse.quote(message)
url += "/%s/%s" % (to, message)

r = requests.get(url)
r.text














