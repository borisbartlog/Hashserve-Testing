# a script that runs continuously and randomly submits different requests
# (post, get, stats) to the hashserver without any internal delay

import hashserve_wrapper as hs
import random 
import time
import string   

COUNT = 1000   # total number of requests before exiting
ONLYGET = False # set to True and we only retrieve hashes for existing jobids.
                # Mainly useful to increase overall load when running multiple
                # instances of the script (avoids the five second delay that
                # posting passwords involves). You will also need to set
                # jobcount to some non-zero value as it will not get updated.
if (ONLYGET): jobcount = 4000 # or set to about whatever the current jobid is

def randpass(): # random password generation
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    size = random.randint(3, 24)
    return ''.join(random.choice(chars) for _ in range(size))
    
def verbose_post():
    password = randpass()
    print ('Posting hash request for password ' + password)
    start = time.time()
    jobid = hs.hash_post(password)
    finish = time.time()
    elapsed = finish - start
    print ('Retrieved jobid: ' + str(jobid) + ' in ' + str(elapsed) + ' seconds')
    return (jobid)
    
def retrieve_random():
    jobid = random.randint(1, jobcount)
    print ('Retrieving hash for jobid ' + str(jobid))
    start = time.time()
    pwdhash = hs.hash_get(jobid)
    finish = time.time()
    elapsed = finish - start
    print('Hash: ' + pwdhash)
    print ('Retrieved in ' + str(elapsed) + ' seconds')

# start by posting one password so that if the first random operation is hash
# retrieval, it has something to operate on

verbose_post() 

i = 1

while i < COUNT:
    choice = random.randint(1, 3)
    if (ONLYGET): choice = 2
    if (choice == 1): # post a new password
        jobid = verbose_post()
        jobcount = jobid
    elif (choice == 2): # retrieve a random previously requested hash
        retrieve_random()
    else: hs.get_stats()
        
    