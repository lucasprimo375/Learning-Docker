# Create new custom network

```bash
docker network create redis
```

# Launch Redis container

```bash
docker run --name redis --network redis -d redis
```

# Launch Redis-Commander container

```bash
docker run --name redis-commander --network redis -p 8081:8081 -e REDIS_HOST=redis -d rediscommander/redis-commander
```