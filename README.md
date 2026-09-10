# AI Resume Screening System

An NLP-based resume screening system that compares candidate resumes with a job description and calculates a similarity score.

## Project Overview

This project uses Natural Language Processing (NLP) techniques to compare resume text with a job description. It helps identify candidates whose resumes are more relevant to the required job.

## Features

- Resume text processing
- Job description comparison
- TF-IDF text vectorization
- Cosine similarity calculation
- Skill matching
- Candidate similarity score
- Shortlisting based on similarity score

## Technologies Used

- Python
- Scikit-learn
- NLP
- TF-IDF
- Cosine Similarity

## How It Works

1. Resume data is provided as text.
2. A job description is defined.
3. TF-IDF converts the text into numerical vectors.
4. Cosine similarity compares resumes with the job description.
5. Matching skills are identified.
6. Candidates are shortlisted based on the similarity score.

## Project Structure

```text
AI-Resume-Screening-System/
│
├── README.md
├── resume_screening.py
└── requirements.txt
