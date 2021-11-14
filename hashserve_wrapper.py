import requests     # http interactions
import hashlib      # to calculate the hash ourselves for verification
import time         # for sleep()
import base64       # to decode our hash in to a string that matches output
from subprocess import check_output     # to get pid and shut down server
import os           # for shutdown request
import signal       # for shutdown request

HOST = '127.0.0.1'
PORT = '55555'
BASEURL = 'http://' + HOST + ':' + PORT + '/'

def hash_post(password):
    Url = BASEURL + 'hash'
    r = requests.post(Url, json={"password":password})
    return (r.json())
    
def hash_get(jobid):
    Url = BASEURL + 'hash' + '/' + str(jobid)
    r = requests.get(Url)
    return (r.text)
    
def calculate_hash(password):
    m = hashlib.sha512()
    b = bytes(password, 'utf-8')
    m.update(b)
    value = m.digest()
    value = str(base64.b64encode(value))[2:-1]
    return(value)

def get_stats():
    Url = BASEURL + 'stats'
    r = requests.get(Url)
    print (r.json())
    
def shutdown_request():  # Windows only unlike the other functions
    pid = check_output(["pidof", 'broken-hashserve_win'])
    if pid is None: 
        print ('Hash server not running at shutdown request')
        return False
    os.kill(pid, signal.SIGTERM)
    return True