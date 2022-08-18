## Run container with folder mapping

```bash
docker run -v <this-local-global-path>:<container-global-path> <container-name>
```

## Getting current local global path with bash command (on PowerShell)

```bash
docker run -v  ${PWD}:<container-global-path> <container-name>
```