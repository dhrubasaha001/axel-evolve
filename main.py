from agents.taskanalyzer import analyze_task
from skills.skillregister import check_skills,load_skill
from agents.agentgenerator import generate_agents

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
    else:
        print(f"Skill '{skill}' is not available.")

# Generate agents for the required skills
generate_agents(result['required_skills'])
print("Agents generated for the required skills.")
