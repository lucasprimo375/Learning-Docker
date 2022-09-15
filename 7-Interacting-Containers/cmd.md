# Creating custom network for all containers

```bash
docker network create <network-name>
```

# Starting all containers

## MYSQL container

```bash
docker run --network <network-name> -e MYSQL_ROOT_PASSWORD=<root-password> -e MYSQL_DATABASE=<database-name> -e MYSQL_USER=<user-name> -e MYSQL_PASSWORD=<user-password> --name <mysql-container-name> mysql:<tag>
```

## Wordpress container

```bash
docker run --network <network-name> -p <external-port>:80 --name <wordpress-container-name> -d wordpress:<tag>
```

## PHPMyAdmin container

```bash
docker run --network <network-name> -p <external-port>:80 -e PMA_HOST=<mysql-container-name> phpmyadmin:<tag>
```