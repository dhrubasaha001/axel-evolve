from taskanalyzer import analyze_task
from skillregister import check_skills

prompt=input("Enter your prompt: ")
result = analyze_task(prompt)
skills = check_skills(result['required_skills'])
print("Task Analysis Result:", result)
print("Availability of that required Skills:", skills)

