import hashserve_wrapper as hs

print('Shutting down hash server:')
result = hs.http_shutdown()
print (result)
