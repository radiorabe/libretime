###############################################################################
# This file holds the implementations for all the API clients.
#
# If you want to develop a new client, here are some suggestions: Get the fetch
# methods working first, then the push, then the liquidsoap notifier.  You will
# probably want to create a script on your server side to automatically
# schedule a playlist one minute from the current time.
###############################################################################

LIBRETIME_API_VERSION = "2.0"

api_config = {}

api_config['version_url'] = 'version/'
