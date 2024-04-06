# Koalix CRM Production Docker Container

This repository contains the Docker configuration for creating a production-ready container for the Koalix CRM system.
The Koalix CRM is a small and easy-to-use Customer Relationship Management system, including a basic Accounting Software.

This Docker container is configured with all necessary dependencies and settings, allowing for the rapid deployment of 
the Koalix CRM in a production environment.

## Installation

Before you start, you need both Docker and Docker Compose installed on your system. Docker Compose comes pre-installed 
with Docker for Mac and Windows, but for Linux, you need to install it separately after Docker.

For Windows and Mac users, you can download Docker Desktop from 
[Docker's official website](https://www.docker.com/products/docker-desktop).
For Linux users, instructions vary by distribution. Docker's official website provides detailed instructions 
for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), [Debian](https://docs.docker.com/engine/install/debian/),
[Fedora](https://docs.docker.com/engine/install/fedora/), and [CentOS](https://docs.docker.com/engine/install/centos/).

## Configuration

Download the `docker-compose.yaml` file from this repository and place it in a directory where you'd like to run the
Koalix CRM container.

Before running the containers, adjust a few environment variables in the `docker-compose.yaml` file:

- `DJANGO_SECRET_KEY`: A secret key for a particular Django installation. This is used to provide cryptographic signing,
- and should be set to a unique, unpredictable value.
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: These are the root username, password, and the database name that 
- PostgreSQL will set up at its launch.

Replace the placeholders with actual values.

## Running the Application

Open a terminal and navigate (`cd`) to the directory containing the `docker-compose.yaml` file. Use the following 
command to download all the required images:

docker-compose pull
After the images are downloaded, launch the application using:

docker-compose up

The application should then be accessible at `http://localhost:8000`, or the HOST and PORT you specified.

## Audience

This repository is intended for DevOps engineers, software developers, or IT administrators who need to deploy
Koalix CRM in a production environment quickly and efficiently.

## Feedback

We welcome your feedback and contributions! Please submit issues or pull requests if you have improvements
or find problems.