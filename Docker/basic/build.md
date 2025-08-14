# Execute the following to build the image
```
docker build -t hello-docker .
```

## Meaning
- `-t hello-docker` -> tags the image so you can run it by name
- `.` means "look for the Dockerfile in the current directory"

## Run the Container
```
docker run hello-docker
```

## Output
```
Hello from Docker!
```