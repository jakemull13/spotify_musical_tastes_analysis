# shows audio analysis for the given track
from __future__ import print_function    # (at top of module)
import json
import time
import sys


tid = id
start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(json.dumps(analysis, indent=4))
print("analysis retrieved in %.2f seconds" % (delta,))