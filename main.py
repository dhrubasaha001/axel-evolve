from agents.taskanalyzer import analyze_task
from skills.skillregister import check_skills

# Main File
prompt=input("Enter your prompt: ")

# Analyze the task and check for required skills
result = analyze_task(prompt)
skills = check_skills(result['required_skills'])
print("Task Analysis Result:", result)
print("Availability of that required Skills:", skills)

