import sys
from pathlib import Path

# Ensure the project root is importable when this script is run directly.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def load_agent(agent_name):
    try:
        agent_module = __import__(f"agents.generated.{agent_name}_agent", fromlist=["run"])
        return agent_module
    except ImportError as e:
        print(f"Error loading agent '{agent_name}': {e}")
        return None

def run_agent(agent, task, skill_content):
    try:
        result = agent.run(task, skill_content)
        return result
    except Exception as e:
        print(f"Error running agent for skill '{agent.SKILL_NAME}': {e}")
        return None

