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


