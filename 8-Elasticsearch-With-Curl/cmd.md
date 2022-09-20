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

# 4 - Creating indexes from inside Curl container

```bash
curl -XPUT http://elasticsearch:9200/my-index
```

```bash
curl -XGET http://elasticsearch:9200/_cat/indices?v
```

# 5 - Creating documents from inside Curl container

```bash
curl -XPOST http://elasticsearch:9200/my-index/cities/1 -H 'Content-Type: application/json' -d '{"city": "New Jersey"}'
```

```bash
curl -XPOST http://elasticsearch:9200/my-index/cities/1 -H 'Content-Type: application/json' -d '{"city": "Marseille"}'
```

```bash
curl -XPOST http://elasticsearch:9200/my-index/cities/1 -H 'Content-Type: application/json' -d '{"city": "Manchester"}'
```

# 6 - Read mappings from inside Curl container

```bash
curl -XGET http://elasticsearch:9200/my-index/_mapping?pretty
```

# 7 - Get document by ID

```bash
curl -XGET http://elasticsearch:9200/my-index/cities/1?pretty
```

# 8 - Get document by filter

```bash
curl -XGET http://elasticsearch:9200/my-index/my-index/_search?q=city:new
```

# 9 - Get all documents

```bash
curl -XGET http://elasticsearch:9200/my-index/my-index/_search
```