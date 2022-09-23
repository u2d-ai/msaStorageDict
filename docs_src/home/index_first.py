from msaStorageDict import MSARedisDict
from redis import Redis

# Construct a new MSARedisDict object
settings = MSARedisDict('settings', Redis())

# Assign and retrieve a value from the dict
settings['foo'] = 'bar'
settings['foo']
# >>> 'bar'

# Assign and retrieve another value
settings['dont'] = 'trick'
settings['dont']
# >>> 'trick'

# Delete a value and access receives a KeyError
del settings['foo']
settings['foo']
# >>> KeyError