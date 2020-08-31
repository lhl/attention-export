#!/usr/bin/python3

import json
import os
from   pprint import pprint
import psaw
import sys
import time

'''
https://pushshift.io/what-is-pushshift-io/
https://pushshift.io/api-parameters/
https://files.pushshift.io/reddit/

https://github.com/dmarx/psaw

/reddit/comment/search?

sort=asc
sort_type=[created_utc]
before=[epoch]
author=randomfoo2

ERROR comment dhum8ac...
'''

api = psaw.PushshiftAPI()
# gen = api.search_comments(author='randomfoo2', before='1495394156')
# pprint(next(gen))
# pprint(len(list(gen)))
gen = api.search_comments(author='randomfoo2', before='1446592512')
pprint(len(list(gen)))
