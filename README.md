# Financial Web Project Using Django, Vue.js, MySQL, and Apache

This project is a financial management web application built using Django (backend), Vue.js (frontend), MySQL (database), and Apache (HTTP server). To run and manage the project, you need Docker and Docker Compose installed on your machine.

## Prerequisites

To use this project, make sure you have **Docker** and **Docker Compose** installed.

If they are not installed:
- Follow the official Docker documentation to install Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Follow the official Docker Compose documentation to install Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## User Guide

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/arturoglcc/financial_project.git
```

### 2. Change to the Project Directory

Navigate into the project directory:

bash ```
cd financial_project
```

### 3. Run All Docker Containers

To start all containers defined in the docker-compose.yml file (if they are not already running), use:

bash ```
docker-compose up --build
```

This command will build the images if they do not already exist and start the containers.

### 4. Stop and Remove All Containers

To stop and remove all Docker containers, use the following commands:

bash ```
docker stop $(docker ps -q)  # Stop all running containers
docker rm $(docker ps -a -q) # Remove all containers
```
Or, if you prefer to use Docker Compose to shut down only the containers defined in this project:

bash```
docker-compose down
```

### 5. View Active Containers

To see a list of active Docker containers, use:

bash```
docker ps
```

This will show the container IDs, names, and other useful information about currently running containers.
Additional Information

For any further information or issues, please refer to the official Docker documentation or reach out to the project maintainers.
