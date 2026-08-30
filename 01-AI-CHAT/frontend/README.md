# AI Chat Application

A full-stack AI chat application with React frontend and FastAPI backend.

## Project Structure

- `frontend/` - React + TypeScript + Vite frontend
- `app/` - FastAPI backend with MongoDB

## Prerequisites

- Node.js (for frontend)
- Python 3.9+ (for backend)
- MongoDB (running on localhost:27017)

## Running the Application

### Frontend

Navigate to the frontend directory and run:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`

### Backend

Navigate to the app directory and run:

```bash
cd app
pip install -r requirement.txt
python3 -m uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Tech Stack

- **Frontend**: React, TypeScript, Vite
- **Backend**: FastAPI, Python
- **Database**: MongoDB
