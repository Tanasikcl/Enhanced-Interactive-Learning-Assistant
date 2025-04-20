import os
from dotenv import load_dotenv
from google import genai

# ✅ Explicitly load the .env file from parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# ✅ Now get the API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file and path.")

# ✅ Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

def get_research_insights(topic, objectives, subtopics, knowledge_level, learning_format):
    # Construct the detailed prompt with new inputs
    prompt = f"""
    You are an educational AI assistant.

    Topic: {topic}
    Learning Objectives: {objectives}
    Subtopics of Interest: {subtopics}
    Prior Knowledge Level: {knowledge_level}
    Preferred Learning Formats: {', '.join(learning_format)}

    Based on this, generate a structured educational report tailored to the user's background and preferences.
    - Include sections with headings and summaries
    - Provide diagrams (mention them using Markdown or simple ASCII if possible)
    - Add examples or code if requested
    - Cite sources and recommend external resources
    - Make the explanation match the user’s level of expertise
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )

    return response.text
