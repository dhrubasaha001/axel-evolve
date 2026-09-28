from pathlib import Path


def check_skills(required_skills):
    file_path = Path("./skills/")
    if not file_path.exists():
        return "Skills directory does not exist."

    skill_directories = {
        directory.name.casefold(): directory
        for directory in file_path.iterdir()
        if directory.is_dir()
    }
    return {
        skill.strip().capitalize(): (
            skill_directories.get(skill.strip().casefold(), Path()) / "skills.md"
        ).exists()
        or (
            skill_directories.get(skill.strip().casefold(), Path()) / "skill.md"
        ).exists()
        for skill in required_skills
    }

def load_skill(skill_name):
    file_path = Path(f"./skills/{skill_name}/skills.md")
    if not file_path.exists():
        file_path = Path(f"./skills/{skill_name}/skill.md")
        if not file_path.exists():
            return f"Skill file for '{skill_name}' does not exist."
    with open(file_path, "r") as skill_file:
        return skill_file.read()
    