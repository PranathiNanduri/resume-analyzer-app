# 📄 Resume Analyzer with AI Feedback

An intelligent and interactive Resume Analyzer that compares any resume against any job description (JD) to provide:

- ✅ Skill matching analysis
- 📊 Match percentage and suitability score (with weighted scoring)
- 🔍 Highlighted missing and matched skills
- 💡 Personalized AI feedback & learning recommendations
- 📥 PDF report download
- 📧 Optional email report sending

Built with **Python**, **Flask**, and **OpenAI GPT**, this app provides accurate insights for both job seekers and HR professionals.

---

## 🚀 Features

- 📁 **Upload Resume** (PDF format)
- 📝 **Paste or Upload Job Description**
- 🧠 **Skill Extraction** using NLP
- 📐 **Weighted Skill Matching** (Must-Have vs Good-to-Have)
- 🔍 **Detailed Match Report**
- 🧾 **AI Feedback** using GPT
- 🖨️ **PDF Report Generation**
- 📬 **Email Report Delivery** (Optional)
- 🎨 **Modern UI/UX** with Streamlit/Flask

---

## 🧠 How It Works

1. **Resume Parsing**  
   Extracts text and skills using `textract`, custom regex, and NLP.

2. **JD Parsing**  
   Parses pasted JD text or batch folder upload to extract relevant job skills.

3. **Skill Classification**  
   Matches resume skills with job description keywords using `weights.json`.

4. **Weighted Scoring Logic**  
   - Must-Have Skills: 70% weight  
   - Good-to-Have Skills: 30% weight  
   (You can configure this)

5. **AI Feedback**  
   Generates personalized feedback using OpenAI's GPT API (if quota available).

6. **Report**  
   Shows detailed stats: skill match %, missing/matched skills, feedback, and download/email options.

---

## 📦 Project Structure

