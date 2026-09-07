from fastapi import FastAPI, Form, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from pypdf import PdfReader

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def home():
    return {
        "message": "AI Resume Analyzer API is running!"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


def analyze_resume(resume_text: str, job_description: str):
    """Compare resume text with the job description keywords."""
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    matched_keywords = sorted(
        word.strip(".,:;()[]{}")
        for word in job_words
        if word.strip(".,:;()[]{}") in resume_words
    )
    matched_keywords = sorted(set(filter(None, matched_keywords)))
    score = round(
        len(matched_keywords) / len(job_words) * 100, 2
    ) if job_words else 0

    return {
        "match_score": score,
        "matched_keywords": matched_keywords,
        "missing_keywords": sorted(job_words - set(matched_keywords)),
    }


@app.post("/api/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume."
        )

    try:
        file_content = await resume.read()

        pdf_reader = PdfReader(BytesIO(file_content))

        resume_text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                resume_text += page_text + "\n"

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the PDF."
            )

        result = analyze_resume(
            resume_text,
            job_description,
        )

        return result

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing resume: {str(error)}"
        )