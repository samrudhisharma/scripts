#Shortens given url using bitly api

import bitly_api
import sys

"""
For Login and API_key details:
settings > Advanced Settings > API support > Legacy API Key
"""

Login = "" 
API_key = "" ##please follow instructions above

conn = bitly_api.Connection(Login,API_key)

cmdFormat = "python bitly_url.py [url], e.g. python bitly_url.py https://www.google.com"

if len(sys.argv) !=2:
	print "Error in input format. Please see: "+cmdFormat
	sys.exit(0)

longurl = sys.argv[1]

response = conn.shorten(longurl)

print response['url']
