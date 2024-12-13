# Financial Web Project Using FastAPI, Vue.js, MySQL, and Apache

This project is a financial management web application built using FastAPI (backend), Vue.js (frontend), MySQL (database), and Apache (HTTP server). To run and manage the project, you need Docker and Docker Compose installed on your machine.

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

```bash
cd financial_project
```

### 3. Run All Docker Containers

To start all containers defined in the docker-compose.yml file (if they are not already running), use:

```bash
docker-compose up --build
```

This command will build the images if they do not already exist and start the containers.

### 4. Run Specific Docker Containers
The project defines the following containers:

* frontend: Vue.js frontend application
* backend: Django backend application
* db: MySQL database
* http: Apache HTTP server acting as a reverse proxy


To start a single Docker container (e.g., only the frontend), specify the container name from the docker-compose.yml file:

```bash

docker-compose up frontend
```

To start multiple containers without running all of them, list the service names separated by spaces:

```bash
docker-compose up frontend backend
```

### 5. Stop and Remove All Containers

To stop and remove all Docker containers, use the following commands:

```bash
docker stop $(docker ps -q)  # Stop all running containers
docker rm $(docker ps -a -q) # Remove all containers
```
Or, if you prefer to use Docker Compose to shut down only the containers defined in this project:

```bash
docker-compose down
```

### 6. View Active Containers

To see a list of active Docker containers, use:

```bash
docker ps
```

This will show the container IDs, names, and other useful information about currently running containers.
Additional Information

### 7. Work Within a Specific Container

To work inside a specific container (e.g., to debug or run commands directly in the backend container), use:

```bash
docker exec -it <container_name_or_id> /bin/bash
```

Replace <container_name_or_id> with the name or ID of the container you want to access. This command opens an interactive terminal session inside the container, allowing you to run commands as if you were working directly on that container.

For example, to access the backend container:

```bash
docker exec -it backend /bin/bash
```

For any further information or issues, please refer to the official Docker documentation or reach out to the project maintainers.

## Functionality

Welcome to our Financial Organizer
This section explains the functions it offers:

### Navigation bar

On the left side of the screen you will find a navigation bar showing the sections available in our Financial Organizer.

### Home

This section will show:
-Your latest movements (income and outlays).
-A graph summarizing your annual movements.

At the bottom of the page, you will find buttons to add income or outlays.

### User settings

Here you can view your personal information, add missing data or edit existing information as needed.

### Change password

In this section you can update your password. To do so, you must first confirm your current password.

### History movements

This section shows a detailed record of your financial movements (income or outlays), depending on the filter you choose. In addition, you can:
-Edit or delete specific movements.
-Perform searches using tags.

### Graphs

Here are graphs summarizing your financial movements. You can visualize them according to different periods: day, week, fortnight, month or year.
-Charts can be bar or line graphs.
-It is possible to save the graphs in PNG format.
-Pie charts are also included to visualize the proportions according to the tags.

