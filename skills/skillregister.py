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
    skills_directory = Path("./skills")
    skill_directory = next(
        (
            directory
            for directory in skills_directory.iterdir()
            if directory.is_dir()
            and directory.name.casefold() == skill_name.strip().casefold()
        ),
        None,
    ) if skills_directory.exists() else None
    if skill_directory is None:
        return f"Skill file for '{skill_name}' does not exist."
    file_path = next(
        (
            file
            for file in skill_directory.iterdir()
            if file.is_file() and file.name.casefold() == "skill.md"
        ),
        None,
    )
    if file_path is None:
        return f"Skill file for '{skill_name}' does not exist."

    with file_path.open("r", encoding="utf-8") as skill_file:
        return skill_file.read()
