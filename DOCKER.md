# Docker Setup Guide

This project includes Docker support for containerized deployment and development.

## Prerequisites

- Docker installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop))
- Docker Compose (included with Docker Desktop)

## Quick Start with Docker Compose

### 1. Build and Run

```bash
cd api_project
docker-compose up -d
```

The API will be available at `http://localhost:8000`

### 2. Initialize Database

```bash
docker-compose exec api python3 init_sample_data.py
```

### 3. View Logs

```bash
docker-compose logs -f api
```

### 4. Stop the Container

```bash
docker-compose down
```

## Manual Docker Commands

### Build the Image

```bash
docker build -t api_project:latest .
```

### Run the Container

```bash
docker run -p 8000:8000 \
  -v $(pwd)/app:/app/app \
  --name api_project \
  api_project:latest
```

### Run with Database Initialization

```bash
docker run -p 8000:8000 \
  -v $(pwd):/app \
  --name api_project \
  api_project:latest

# In another terminal:
docker exec api_project python3 init_sample_data.py
```

### Access Docker Container Shell

```bash
docker exec -it api_project bash
```

### Stop and Remove Container

```bash
docker stop api_project
docker rm api_project
```

## Docker Features

✅ **Multi-stage build** - Optimized image size (reduced dependencies layer)  
✅ **Non-root user** - Security best practice  
✅ **Health checks** - Automatic container health monitoring  
✅ **Volume mounts** - Live code reloading in development  
✅ **Environment variables** - Configurable via `.env`  

## Testing in Docker

```bash
# Run tests in container
docker-compose exec api pytest -v

# Or with coverage
docker-compose exec api pytest --cov=app
```

## Docker Compose Services

- **api**: FastAPI application running on port 8000

## Environment Variables

Configure in `docker-compose.yml` or create `.env`:

```env
DEBUG=False
DATABASE_URL=sqlite:///./app.db
```

## Troubleshooting

### Port 8000 Already in Use

Change the port in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Use 8001 instead
```

### Database Not Persisting

Ensure volumes are mounted:

```bash
docker-compose down -v  # Remove volumes
docker-compose up -d    # Recreate
```

### Clear All Docker Resources

```bash
docker-compose down --rmi all -v
```
