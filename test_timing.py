# check of hash server timing requirements

import hashserve_wrapper as hs
import time

password = 'sheelba'
failures = 0

# check the time required to obtain jobid

print ('Posting hash request for password ' + password)
start = time.time()
jobid = hs.hash_post(password)
finish = time.time()
elapsed = finish - start

# the use of 0.5 seconds is sort of fragile here, test will incorrectly failure
# under high network latency. Better would be to check the latency first and 
# incorporate that value in to the check.

if (elapsed < 0.5): 
    print ('Jobid returned immediately')
else:
    print ('Jobid returned after ' + str(elapsed) + ' seconds (failure)')
    failures = failures + 1
  
# Now see whether it actually waits five seconds before calculating hash
  
print ('Retrieved jobid: ' + str(jobid))
print ('Immediately requesting hash')
pwdhash = hs.hash_get(jobid)
print ('Checking hash')
myhash = hs.calculate_hash(password)
if myhash == pwdhash: 
    print ('Hash is correct but retrieved prematurely')
    failures = failures + 1

# check again after five seconds

print ('Waiting five seconds')
time.sleep(5)
print ('Retrieving hash after expected interval')
pwdhash = hs.hash_get(jobid)
print ('Checking hash')
myhash = hs.calculate_hash(password)
if myhash == pwdhash: 
    print ('Hash is correct')
else:
    print ('Hash does not match expected value')
    failures = failures + 1
    
if (failures == 0): print ('PASS')
else: print ('FAIL: ' + str(failures) + ' failures')
