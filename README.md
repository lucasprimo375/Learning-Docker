# Learning-Docker
Repository to learn Docker from Udemy course by Bogdan Stashchuk

# Important Commands

## Running a container

```bash
docker run <container-name>
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