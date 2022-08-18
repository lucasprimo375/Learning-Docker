# Learning-Docker
Repository to learn Docker from Udemy course by Bogdan Stashchuk

# Important Commands

## Running a container

```bash
docker run <container-name>
```

## Stop a container from running

```bash
docker kill <container-name-or-id>
```

## Run container with external port

```bash
docker run -p <external-port>:<port> <container-name>
```

## Run container with folder mapping

```bash
docker run -v <local-global-path>:<container-global-path> <container-name>
```

## Run container in the background

```bash
docker run -d <container-name>
```

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

## To execute bash inside the container

```bash
docker run -it <container-name>
```

## To download image from docker hub

```bash
docker pull <image-name>
```

## Get container logs

```bash
docker logs <container-id>
```