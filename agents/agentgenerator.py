from pathlib import Path

def generate_agents(required_skills):
    generated_agents_path = Path("./agents/generated/")
    generated_agents_path.mkdir(parents=True, exist_ok=True)

    for skill in required_skills:
        agent_name = skill.strip().casefold().replace(" ", "_")
        agent_file_path = generated_agents_path / f"{agent_name}_agent.py"

        with agent_file_path.open("w", encoding="utf-8") as agent_file:
            agent_file.write(
                f"SKILL_NAME = {skill.strip()!r}\n\n"
            )
            agent_file.write(
                "def run(task, skill_content):\n"
                "    return f\"Agent received task: {task}\"\n"
            )

        print(f"Generated agent for skill '{skill}' at: {agent_file_path}")

