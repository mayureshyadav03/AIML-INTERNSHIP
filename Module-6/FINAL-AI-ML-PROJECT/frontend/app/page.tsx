"use client";

import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

type AnalysisResult = {
  match_score: number;
  resume_skills: string[];
  job_skills: string[];
  matching_skills: string[];
  missing_skills: string[];
};

export default function Home() {
  const [resume, setResume] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyzeResume() {
    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);
    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch(`${API_URL}/api/analyze`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Analysis failed.");
      }
          

// Convert API response into AnalysisResult format
const resultData: AnalysisResult = {
  match_score: data.match_score,
  resume_skills: data.resume_skills || [],
  job_skills: data.job_skills || [],
  matching_skills: data.matched_keywords || [],
  missing_skills: data.missing_keywords || [],
};


setResult(resultData);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-12 text-white">
      <div className="mx-auto max-w-5xl">

        {/* Header */}
        <div className="mb-10 text-center">
          <p className="mb-3 text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
            AI-Powered Career Tool
          </p>

          <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
            AI Resume Analyzer
          </h1>

          <p className="mx-auto mt-4 max-w-2xl text-slate-400">
            Upload your resume and compare it with a job description
            using NLP and machine learning.
          </p>
        </div>

        {/* Input Section */}
        <div className="grid gap-6 md:grid-cols-2">

          {/* Resume Upload */}
          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="mb-2 text-xl font-semibold">
              📄 Upload Resume
            </h2>

            <p className="mb-5 text-sm text-slate-400">
              Upload your resume in PDF format.
            </p>

            <div className="flex min-h-40 cursor-pointer flex-col items-center justify-center rounded-xl border-2 border-dashed border-slate-700 p-6">
  <span className="mb-2 text-3xl">📁</span>

  <span className="font-medium">
    {resume ? resume.name : "Choose PDF file"}
  </span>

  <span className="mt-1 text-xs text-slate-500">
    PDF only
  </span>

  <input
    type="file"
    accept=".pdf,application/pdf"
    onChange={(event) => {
      const file = event.target.files?.[0];

      if (!file) return;

      if (!file.name.toLowerCase().endsWith(".pdf")) {
        setError("Please select a PDF file.");
        setResume(null);
        return;
      }

      setResume(file);
      setError("");
    }}
    className="mt-4 block w-full text-sm"
  />
</div>
          </div>

          {/* Job Description */}
          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="mb-2 text-xl font-semibold">
              💼 Job Description
            </h2>

            <p className="mb-5 text-sm text-slate-400">
              Paste the job description you want to compare against.
            </p>

            <textarea
              value={jobDescription}
              onChange={(event) => setJobDescription(event.target.value)}
              placeholder="Paste the job description here..."
              className="min-h-40 w-full resize-none rounded-xl border border-slate-700 bg-slate-950 p-4 text-sm text-white outline-none transition placeholder:text-slate-600 focus:border-blue-500"
            />
          </div>
        </div>

        {/* Analyze Button */}
        <div className="mt-6 text-center">
          <button
            onClick={analyzeResume}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-10 py-4 font-semibold transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Analyzing Resume..." : "🤖 Analyze Resume"}
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="mt-6 rounded-xl border border-red-900 bg-red-950/40 p-4 text-center text-red-300">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <section className="mt-12">

            <h2 className="mb-6 text-center text-3xl font-bold">
              Analysis Results
            </h2>

            {/* Score */}
            <div className="mb-6 rounded-2xl border border-slate-800 bg-slate-900 p-8 text-center">
              <p className="text-sm uppercase tracking-widest text-slate-400">
                Resume Match Score
              </p>

              <div className="mt-3 text-7xl font-bold text-blue-400">
                {result.match_score}%
              </div>
            </div>

            {/* Skills */}
            <div className="grid gap-6 md:grid-cols-2">

              {/* Matching */}
              <div className="rounded-2xl border border-green-900 bg-green-950/20 p-6">
                <h3 className="mb-4 text-xl font-semibold text-green-400">
                  ✅ Matching Skills
                </h3>

                <div className="flex flex-wrap gap-2">

                  {(result.matching_skills || []).map((skill) => {
                    return (
                      <span
                        key={skill}
                        className="rounded-full bg-green-900/50 px-4 py-2 text-sm text-green-300"
                      >
                        {skill}
                      </span>
                    );
                  })}
                </div>
              </div>

              {/* Missing */}
              <div className="rounded-2xl border border-red-900 bg-red-950/20 p-6">
                <h3 className="mb-4 text-xl font-semibold text-red-400">
                  ❌ Missing Skills
                </h3>

                <div className="flex flex-wrap gap-2">
                  {(result.missing_skills || []).map((skill) => (
                    <span
                      key={skill}
                      className="rounded-full bg-red-900/50 px-4 py-2 text-sm text-red-300"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            {/* Detected Skills */}
            <div className="mt-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">
              <h3 className="mb-4 text-xl font-semibold">
                🔎 Skills Detected in Resume
              </h3>
                  
              <div className="flex flex-wrap gap-2">
               {(result.resume_skills || []).map((skill) => {
         

  return (
    <span
      key={skill}
      className="rounded-full bg-slate-800 px-4 py-2 text-sm text-slate-300"
    >
      {skill}
    </span>
  );
})}
              </div>
            </div>

          </section>
        )}

        {/* Footer */}
        <footer className="mt-16 text-center text-sm text-slate-600">
          Built with Next.js • FastAPI • Python • NLP • Machine Learning
        </footer>

      </div>
    </main>
  );
}