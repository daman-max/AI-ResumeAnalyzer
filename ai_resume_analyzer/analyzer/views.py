from django.shortcuts import render
from .models import Resume
from .resume_parser import extract_text_from_pdf
from .skill_extractor import extract_skills

def upload_resume(request):
    if request.method == "POST":
        file = request.FILES['resume']
        resume = Resume.objects.create(file=file)

        # Full path of uploaded resume
        pdf_path = resume.file.path

        # Extract text
        extracted_text = extract_text_from_pdf(pdf_path)
        skills = extract_skills(extracted_text)

        return render(request, "analyzer/result.html", {
            "text": extracted_text[:3000],  # show first part only
            "skills": skills
        })

    return render(request, "analyzer/upload.html")
