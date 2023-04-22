# Recipe API Project

This project is a simple API for recipes. It is a REST API that allows you to create, read, update and delete recipes.
Made applying the TDD methodology.

## Technologies

- Django
- PostgreSQL
- Docker
- GitHub Actions

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the repository

   ```bash
    git clone git@github.com:AngelCruzL/recipe-app-api.git
   ```

2. Execute the next command:

   ```bash
    docker-compose up
   ```

## Test

Run the following command to run the tests:

```bash
docker-compose run --rm app sh -c "python manage.py test"
```
