import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

#print(redis_client.set('test2', 'hello world2'))

#print(redis_client.get('test'))
print(redis_client.get('a'))

redis_client.close()
