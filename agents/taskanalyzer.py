import ollama
import json

def analyze_task(prompt):
    response = ollama.chat(
    model="llama3",
    messages=[
        {
        "role": "system", 
        "content": """
        You are a Axel Evolve Task Analyzer Agent , your task is to analyze the prompt given by the user and provide a detailed analysis of the task, including its complexity, potential challenges, and any relevant skills that can help in understanding the task better. Please provide your analysis in a clear and concise JSON format only . And give the required skills in a JSON Format.
        Follow the JSON Format:
            Task_Analysis_Result: {
                "task_analysis": {....},
                "complexity_level": "high/medium/low",
                "potential_challenges": {....},            
                "required_skills": [...],
            }
        Strictly follow the JSON format and do not include any additional text or explanations outside of the JSON structure.
        Strictly avoid any text outside of the JSON structure.
        Do not answer anything outside of the JSON structure and dont interract with the user.

        Example of the JSON format:
        User Prompt: write a python calculator code
        AI Ouput:
        Task_Analysis_Result: {
            "task_analysis": "The user wants to write a Python calculator code.",
            "complexity_level": "low",
            "potential_challenges": "The user may not be familiar with Python syntax or the specific requirements of a calculator.",
            "required_skills": ["Python", "programming fundamentals"],
        }
        """,
    },{
        "role": "user",
        "content": prompt
        }
    ]
    )
    output = response["message"]["content"]
    output = output.replace("Task_Analysis_Result:", "").strip()
    output = json.loads(output)
    return output