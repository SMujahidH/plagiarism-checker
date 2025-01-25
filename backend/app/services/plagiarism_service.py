import os
import requests
from app.utils.file_handler import extract_text_from_file
from dotenv import load_dotenv
from rapidfuzz import fuzz

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

async def check_plagiarism_service(file):
    """
    Service to handle plagiarism detection.
    """
    # Extract text from the uploaded file
    text = extract_text_from_file(file)

    # Split text into paragraphs
    paragraphs = text.split("\n\n")
    if not paragraphs or not any(paragraphs):
        raise ValueError("No valid text was extracted from the file.")

    overall_results = []
    paragraph_scores = []

    for i, paragraph in enumerate(paragraphs):
        query = " ".join(paragraph.split()[:50])  # Limit to 50 words

        if not query.strip():  # Ensure query is not empty
            continue

        # Query Google Custom Search API
        response = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params={"q": query, "key": GOOGLE_API_KEY, "cx": SEARCH_ENGINE_ID},
        )
        if response.status_code == 400:
            raise ValueError(f"Invalid Google API request for query: {query}")
        response.raise_for_status()
        data = response.json()

        # Calculate similarity
        max_similarity = 0
        matches = []
        for item in data.get("items", []):
            similarity = fuzz.ratio(paragraph, item.get("snippet", ""))
            max_similarity = max(max_similarity, similarity)
            matches.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
                "similarity": f"{similarity}%",
            })

        paragraph_scores.append(max_similarity)
        overall_results.append({
            "paragraph_index": i + 1,
            "paragraph": paragraph,
            "max_similarity": f"{max_similarity}%",
            "matches": matches,
        })

    overall_score = sum(paragraph_scores) / len(paragraph_scores) if paragraph_scores else 0
    is_plagiarized = overall_score > 30  # Define threshold here

    return {
        "overall_score": f"{overall_score:.2f}%",
        "is_plagiarized": is_plagiarized,
        "detailed_results": overall_results,
    }
