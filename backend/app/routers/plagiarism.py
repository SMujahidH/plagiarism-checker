from fastapi import APIRouter, UploadFile, File
from ..services.plagiarism_service import check_plagiarism_service


router = APIRouter()

@router.post("/")
async def check_plagiarism(file: UploadFile = File(...)):
    """
    Endpoint to check plagiarism for an uploaded file.
    """
    return await check_plagiarism_service(file)
