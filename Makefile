# Define targets
build: # Target to build the Docker image
  docker build -t my-logistic-regression-app .

run: # Target to run the container
  docker run -p 8081:8080 my-logistic-regression-app

# Optional target for cleaning up (remove the container)
clean:
  docker stop my-logistic-regression-app
  docker rm my-logistic-regression-app

# Dependency for the run target (ensures image is built before running)
run: build

# Default target to run when you simply run 'make'
.DEFAULT_GOAL := run
