import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Important skills we want the analyzer to recognize
SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "react",
    "next.js",
    "node.js",
    "fastapi",
    "flask",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "nlp",
    "git",
    "github",
    "docker",
    "aws",
}


def clean_text(text: str) -> str:
    """Normalize text for analysis."""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(text: str) -> list[str]:
    """Find known skills mentioned in the text."""
    cleaned_text = clean_text(text)

    found_skills = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, cleaned_text):
            found_skills.append(skill)

    return sorted(found_skills)


def calculate_match_score(
    resume_text: str,
    job_description: str,
) -> float:
    """Calculate TF-IDF cosine similarity between resume and job description."""

    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    if not resume_text or not job_description:
        return 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    vectors = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(float(similarity * 100), 2)

def analyze_resume(
    resume_text: str,
    job_description: str,
) -> dict:
    """Analyze a resume against a job description."""

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matching_skills = sorted(resume_skills & job_skills)
    missing_skills = sorted(job_skills - resume_skills)

    match_score = calculate_match_score(
        resume_text,
        job_description,
    )

    return {
        "match_score": match_score,
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
    }
    
    
if __name__ == "__main__":
    resume = """
    I am a Python developer with experience in machine learning,
    pandas, numpy, SQL and data analysis.
    """

    job = """
    We are looking for a Python developer with machine learning,
    SQL, pandas, TensorFlow and Docker experience.
    """

    result = analyze_resume(resume, job)

    print(result)    