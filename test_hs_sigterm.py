# This script shuts down the hash server (gently, via SIGTERM)
# To verify anything useful it is necessary to be running other tests against
# the server at the same time (e.g. test_hs_loadrunner or similar)

import hashserve_wrapper as hs
import time

if (hs.shutdown_request()): 
    print ('Shutting down hash server...')
else:
    print ('Hash server not running.')
    