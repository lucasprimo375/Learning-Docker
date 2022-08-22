# Running container with custom command
```bash
docker run <image-name> <custom-command>
```

# Commands for this case
```bash
docker run -v ${PWD}:"/app" python python3 /app/hello-world.py
```

```bash
docker run -v ${PWD}:"/app" -w /app python python3 hello-world.py
```

-w <string> stands for the working directory inside the container to execute the command.