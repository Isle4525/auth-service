# Auth Service

Microservice for user authentication and authorization, built with FastAPI.

## Features

- User Registration & Login
- JWT-based Authentication
- Password Hashing with Passlib (bcrypt)
- PostgreSQL Database integration (via SQLAlchemy)
- Pydantic schemas for data validation
- Dockerized environment

## Project Structure

```text
auth-service/
├── app/                # Main application entry point and database config
├── core/               # Security and JWT configurations
├── models/             # SQLAlchemy database models
├── routes/             # API route handlers
├── schemas/            # Pydantic data schemas
├── services/           # Business logic
└── docker-compose.yaml # Docker orchestration
```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional)

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Isle4525/auth-service.git
   cd auth-service
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and configure your variables (see `.env.example` if available).

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Running with Docker

```bash
docker-compose up --build
```

## API Documentation

Once the server is running, you can access the interactive API docs:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
