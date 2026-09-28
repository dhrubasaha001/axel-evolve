from agents.taskanalyzer import analyze_task
from skills.skillregister import check_skills,load_skill

# Main File
prompt=input("Enter your prompt: ")

# Analyze the task and check for required skills
result = analyze_task(prompt)
skills = check_skills(result['required_skills'])
print("The Required Skills are: ", result['required_skills'])
for skill, is_available in skills.items():
    if is_available:
        skill_content = load_skill(skill)
        print(f"Skill '{skill}' loaded.")
        print(f"Content of '{skill}':\n{skill_content}\n")

    else:
        print(f"Skill '{skill}' is not available.")

