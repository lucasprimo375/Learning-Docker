# Learning-Docker
Repository to learn Docker from Udemy course by Bogdan Stashchuk

# Important Commands

## Running a container

```bash
docker run <image-name>
```

## Stop a container from running

```bash
docker kill <container-name-or-id>
```

## Run container with external port

```bash
docker run -p <external-port>:<port> <image-name>
```

## Run container with folder mapping

```bash
docker run -v <local-global-path>:<container-global-path> <image-name>
```

## Run container in the background

```bash
docker run -d <image-name>
```

## Run container with specific name
```bash
docker run --name <container-name> <image-name>
```

## Run existing stopped container
```bash
docker start <container-name-or-id>
```

The container will run with the same configuration as it was running before being stopped.

## List running containers

```bash
docker ps
```

or

```bash
docker container ls
```

## List all containers, running or stopped

```bash
docker ps -a
```
or

```bash
docker container ls -a
```

## List images

```bash
docker images
```

## To simulate a terminal inside the container and keep STDIN open

```bash
docker run -it <image-name>
```

## To download image from docker hub

```bash
docker pull <image-name>
```

## Get container logs

```bash
docker logs <container-id>
```

## Remove stopped container from system

```bash
docker rm <container-name-or-id>
```

## Remove all stopped containers from system

```bash
docker container prune
```

## Run command in a running container

```bash
docker exec <running-container-ir-or-name> <command-to-run>
```

```bash
docker container exec <running-container-id-or-name> <command-to-run>
```

To actually see terminal, use -it option.

```bash
docker exec -it <running-container-id-or-name> <command-to-run>
```

To list container environment variables:
```bash
docker exec <running-container-id-or-name> env
```

## Get details on the container

```bash
docker inspect <container-id-or-name>
```

## Setting environment variables

```bash
docker run -e <environment-variable-name>=<environment-variable-value> <image-name>
```

Option -e can be used as many times as needed.

## Setting custom hostname for container

```bash
docker run -h <custom-hostname> <image-name>
```