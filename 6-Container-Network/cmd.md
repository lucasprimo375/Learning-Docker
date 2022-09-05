# List networks

```bash
docker network ls
```

# Get network details

```bash
docker network inspect <network-name-or-id>
```

# Create new network

```bash
docker network create <network-custom-name>
```

# Run container is specific network

```bash
docker run --network <network-name-or-id> <image-name-or-id>
```