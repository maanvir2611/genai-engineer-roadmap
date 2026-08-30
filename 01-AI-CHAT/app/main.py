from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.test_case import router as test_case_router

app = FastAPI(
    title="AI Chat API",
    description="AI Chat API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(test_case_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Chat API"}
