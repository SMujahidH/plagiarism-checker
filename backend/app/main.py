from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.plagiarism import router as plagiarism_router

app = FastAPI()

# Allow requests from specific origins (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Register routers
# Remove the prefix so plagiarism detection becomes the root endpoint
app.include_router(plagiarism_router,prefix="/api/plagiarism", tags=["Plagiarism Detection"])

# Root endpoint (optional, if you still want to keep the welcome message at `/`)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Plagiarism Detection API"}
