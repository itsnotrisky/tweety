#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = '3l4JpQnclQNoHYfaieCPddRSy'
CONSUMER_SECRET = 'VxRcM3oq4IFJjMH0kNhJ7HNIebfmBgNY5NGzk57VpOvbLahKev'
ACCESS_KEY = '2773134834-qQ4622FFFcIA7rZDAx9yNYK8mxK2lVqRTfPaIK2'
ACCESS_SECRET = 'gfRVj8hWOuZQ4UkIEK4YxRBVbkYnyCq7M2Sad10UIeRfg'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
