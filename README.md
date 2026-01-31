FastAPI-Posts-API
FastAPI Posts API - Backend Documentation
📋 Project Overview

The FastAPI Posts API is a technical test project that consumes data from the public JSONPlaceholder API and provides custom endpoints for listing, searching, and retrieving posts with author details. The backend is built using FastAPI and asynchronous HTTP calls for high performance and responsiveness.

🚀 Features

List Posts: Retrieve all posts, with optional filtering by user.

Search Posts: Search posts by keyword in title or body.

Single Post Retrieval: Get details of a single post along with author information.

Asynchronous API Calls: Fetch external data efficiently using httpx.

Error Handling: Graceful handling of missing or invalid resources.

🏗️ Technology Stack

Backend Framework: FastAPI

HTTP Client: HTTPX (async support)

Server: Uvicorn

Language: Python 3.9+

Database: N/A (data fetched from external API)

Authentication: N/A (public API)

⚙️ Setup Instructions
1️⃣ Prerequisites

Python 3.9+

Virtualenv (recommended)

2️⃣ Installation
# Clone the repository
git clone https://github.com/your-username/fastapi-posts-api.git
cd fastapi-posts-api

# Create a virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload

3️⃣ Environment Variables

No environment variables required for this test API. Optional settings can be added for logging or external API URLs.

🗂️ Project Structure
fastapi-posts-api/
├── app/
│   ├── __init__.py        # Package initialization
│   └── main.py            # FastAPI application and routes
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

🔐 Authentication

This API does not implement authentication; all endpoints are publicly accessible.

Optional: JWT or OAuth2 can be integrated in future versions for protected endpoints.

📊 API Endpoints
| Method | Endpoint       | Description                              |
| ------ | -------------- | ---------------------------------------- |
| GET    | /posts/        | List all posts (filter by user optional) |
| GET    | /posts/search/ | Search posts by keyword in title/body    |
| GET    | /posts/{id}/   | Retrieve a single post with author info  |


Note: All endpoints fetch data from JSONPlaceholder and return JSON responses.

Author
GREGORY TALI
