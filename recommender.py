def recommend_courses(missing_skills):
    """Return course recommendations for missing skills with title and URL."""
    
    course_data = {
        "python": {
            "title": "Python for Everybody",
            "url": "https://www.coursera.org/specializations/python"
        },
        "sql": {
            "title": "SQL Fundamentals",
            "url": "https://www.datacamp.com/courses/sql-fundamentals"
        },
        "excel": {
            "title": "Advanced Excel Formulas & Functions",
            "url": "https://www.udemy.com/course/microsoft-excel-advanced-excel-formulas-functions/"
        },
        "tableau": {
            "title": "Data Visualization with Tableau",
            "url": "https://www.coursera.org/learn/data-visualization-tableau"
        },
        "power bi": {
            "title": "Power BI: Up & Running",
            "url": "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/"
        },
        "communication": {
            "title": "Improving Communication Skills",
            "url": "https://www.coursera.org/learn/wharton-communication-skills"
        },
        "r": {
            "title": "R Programming Track",
            "url": "https://www.datacamp.com/tracks/r-programming"
        },
        "aws": {
            "title": "AWS Training & Certification",
            "url": "https://aws.amazon.com/training/"
        },
        "snowflake": {
            "title": "Snowflake: Zero to Hero",
            "url": "https://www.udemy.com/course/snowflake-zero-to-hero/"
        },
        "machine learning": {
            "title": "Machine Learning by Andrew Ng",
            "url": "https://www.coursera.org/learn/machine-learning"
        },
        "data analysis": {
            "title": "Data Analysis Specialization",
            "url": "https://www.coursera.org/specializations/data-analysis"
        },
        "a/b testing": {
            "title": "A/B Testing Course",
            "url": "https://www.coursera.org/learn/ab-testing"
        },
        "data cleaning": {
            "title": "Data Cleaning in Python",
            "url": "https://www.datacamp.com/courses/data-cleaning-in-python"
        },
        "statistics": {
            "title": "Statistics and Probability",
            "url": "https://www.khanacademy.org/math/statistics-probability"
        }
    }

    recommendations = {}
    for skill in missing_skills:
        skill_normalized = skill.lower()
        if skill_normalized in course_data:
            recommendations[skill] = course_data[skill_normalized]
        else:
            recommendations[skill] = {
                "title": f"Learn {skill.title()}",
                "url": f"https://www.google.com/search?q={skill.replace(' ', '+')}+online+course"
            }

    return recommendations
