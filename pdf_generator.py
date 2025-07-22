from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_pdf_report(user_name, match_percentage, missing_skills, suggested_skills, filename="analysis_report.pdf"):
    # Create reports directory if not exists
    reports_dir = "app/reports"
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(reports_dir, f"{user_name}_{timestamp}.pdf")

    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Resume Analysis Report")

    # Info section
    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, f"Name: {user_name}")
    y -= 20
    c.drawString(50, y, f"Match Percentage: {match_percentage}%")
    y -= 20
    c.drawString(50, y, f"Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}")
    y -= 20
    c.drawString(50, y, f"Suggested Skills to Learn: {', '.join(suggested_skills) if suggested_skills else 'None'}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 30, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.save()

    return file_path
