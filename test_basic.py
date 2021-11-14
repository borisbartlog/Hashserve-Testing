import hashserve_wrapper as hs

password = 'ningauble'
print ('Posting hash request for password ' + password)
jobid = hs.hash_post(password)
print ('Retrieved jobid: ' + str(jobid))
print ('Requesting hash')
pwdhash = hs.hash_get(jobid)
print (pwdhash)
print ('Checking hash')
myhash = hs.calculate_hash(password)
if myhash == pwdhash: print ('Hash is correct: PASS')
else: print ('Hashes do not match: Server hash is ' + pwdhash + '\n' + 'Calculated value is ' + myhash + '\n' + 'FAIL')
