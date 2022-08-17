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