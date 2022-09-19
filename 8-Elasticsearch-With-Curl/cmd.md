# 1 - Creating new custom bridge network

```bash
docker network create elasticsearch
```

# 2 - Creating Elasticsearch container

```bash
docker run -d --name elasticsearch --network elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.6.2
```

# 3 - Creating Curl container

```bash
docker run --name curl --network elasticsearch -it curlimages/curl sh
```