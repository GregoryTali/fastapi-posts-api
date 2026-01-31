FastAPI-Posts-API
FastAPI Posts API - Backend Documentation
📋 Project Overview

The FastAPI Posts API is a  project that consumes data from the public JSONPlaceholder API and provides custom endpoints for listing, searching, and retrieving posts with author details. The backend is built using FastAPI and asynchronous HTTP calls for high performance and responsiveness.

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