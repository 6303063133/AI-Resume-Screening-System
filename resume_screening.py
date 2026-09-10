# AI Resume Screening System
# Author: Supriya Gundepalli

resumes = {
    "Candidate 1": "Python SQL Pandas Data Analysis",
    "Candidate 2": "Java SQL MySQL OOP",
    "Candidate 3": "Python Machine Learning SQL Pandas"
}

required_skills = ["Python", "SQL", "Pandas"]

print("===== AI Resume Screening System =====")

for candidate, resume in resumes.items():
    matched_skills = []

    for skill in required_skills:
        if skill.lower() in resume.lower():
            matched_skills.append(skill)

    score = (len(matched_skills) / len(required_skills)) * 100

    print("\nCandidate:", candidate)
    print("Matched Skills:", matched_skills)
    print("Match Score:", round(score, 2), "%")

    if score >= 70:
        print("Status: Shortlisted")
    else:
        print("Status: Not Shortlisted")
